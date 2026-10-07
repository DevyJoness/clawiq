const { app, BrowserWindow, ipcMain, dialog, Menu } = require('electron');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const fs = require('node:fs/promises');
const { randomUUID } = require('node:crypto');
const smoke = process.argv.includes('--smoke-test');
let window, assistant, store;
const images = new Map();
app.setName('ClawIQ');
if (!app.requestSingleInstanceLock()) app.quit();
else {
  app.on('second-instance', () => { if(window){window.restore();window.show();window.focus();} });
  app.whenReady().then(start).catch(error => { console.error(error.message); if(!smoke)dialog.showErrorBox('ClawIQ не запустился',error.message);app.exit(1); });
}
function handle(channel, callback) {
  ipcMain.handle(channel, async (event, ...args) => {
    if(event.sender !== window.webContents || event.senderFrame !== window.webContents.mainFrame) throw new Error('Untrusted caller');
    try { return { ok: true, data: await callback(...args) }; }
    catch(error) { return { ok: false, error: error.message }; }
  });
}
async function start() {
  const { SessionStore } = await import(pathToFileURL(path.join(__dirname,'../../core/store.mjs')).href);
  const { Assistant } = await import(pathToFileURL(path.join(__dirname,'../../core/assistant.mjs')).href);
  const root = smoke ? await fs.mkdtemp(path.join(app.getPath('temp'),'clawiq-smoke-')) : path.join(app.getPath('userData'),'sessions');
  store = new SessionStore(root); assistant = new Assistant(store);
  Menu.setApplicationMenu(null);
  window = new BrowserWindow({title:'ClawIQ',width:1250,height:850,minWidth:860,minHeight:650,show:!smoke,backgroundColor:'#10141c',
    webPreferences:{preload:path.join(__dirname,'preload.cjs'),contextIsolation:true,nodeIntegration:false,sandbox:true,webSecurity:true}});
  window.webContents.setWindowOpenHandler(() => ({action:'deny'}));
  window.webContents.on('will-navigate',event=>event.preventDefault());
  window.webContents.session.setPermissionRequestHandler((_c,_p,done)=>done(false));
  handle('clawiq:status',()=>assistant.status()); handle('clawiq:list',()=>store.list());
  handle('clawiq:create',()=>store.create()); handle('clawiq:get',id=>store.get(id));
  handle('clawiq:delete',id=>{ if(assistant.busy)throw new Error('Дождитесь ответа.');return store.delete(id); });
  handle('clawiq:image',async()=>{
    const result = await dialog.showOpenDialog(window,{properties:['openFile'],filters:[{name:'Изображения',extensions:['png','jpg','jpeg']}]});
    if(result.canceled)return null;
    const selected=result.filePaths[0],stat=await fs.stat(selected);
    if(stat.size>10*1024*1024)throw new Error('Максимальный размер изображения — 10 МБ.');
    const bytes=await fs.readFile(selected);
    const png=bytes.subarray(0,8).equals(Buffer.from([137,80,78,71,13,10,26,10]));
    const jpeg=bytes[0]===255 && bytes[1]===216 && bytes[2]===255;
    if(!png&&!jpeg)throw new Error('Поддерживаются изображения PNG и JPEG.');
    images.clear(); const id=randomUUID();images.set(id,{name:path.basename(selected),base64:bytes.toString('base64')});
    return {id,name:path.basename(selected)};
  });
  handle('clawiq:send',async input=>{
    if(!input||typeof input!=='object')throw new Error('Invalid request');
    const image=input.imageId?images.get(input.imageId):undefined;
    if(input.imageId&&!image)throw new Error('Выберите изображение заново.');
    const result=await assistant.send({sessionId:input.sessionId,text:input.text,image}); images.clear();return result;
  });
  await window.loadFile(path.join(__dirname,'ui/index.html'));
  if(smoke) {
    const result=await window.webContents.executeJavaScript(`(async()=>{const created=await window.clawiq.create();const saved=await window.clawiq.get(created.data.id);const listed=await window.clawiq.list();await window.clawiq.remove(created.data.id);return {title:document.title,chat:!!document.querySelector('#composer'),session:saved.data.id===created.data.id,list:listed.data.length>0};})()`);
    if(result.title!=='ClawIQ'||!result.chat||!result.session||!result.list)throw new Error(JSON.stringify(result));
    console.log('PASS ClawIQ desktop IPC, sessions and isolated chat UI');
    const screenshot=path.join(app.getPath('temp'),'clawiq-desktop.png');
    try {
      await fs.writeFile(screenshot,(await window.webContents.capturePage()).toPNG()); console.log('Screenshot: '+screenshot);
    } catch(error) { console.warn('Optional screenshot unavailable: '+error.message); }
    app.quit();
  }
}
app.on('window-all-closed',()=>app.quit());
