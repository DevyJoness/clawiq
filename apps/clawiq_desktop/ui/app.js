const $ = id => document.getElementById(id);
let current, image, busy = false;
async function call(promise) { const result = await promise; if(!result.ok)throw new Error(result.error); return result.data; }
function error(message) { $('error').textContent=message; $('error').hidden=!message; }
function setBusy(value) { busy=value; for(const id of ['send','new','delete','attach','clear-image'])$(id).disabled=value; $('send').textContent=value?'Отвечаю…':'Отправить ↗'; }
async function list() {
  const sessions=await call(window.clawiq.list()); $('sessions').replaceChildren();
  for(const session of sessions){const button=document.createElement('button');button.textContent=session.title;button.classList.toggle('active',session.id===current?.id);button.addEventListener('click',async()=>{if(busy)return;try{current=await call(window.clawiq.get(session.id));image=null;renderImage();render();await list();}catch(e){error(e.message);}});$('sessions').append(button);}
}
function render() {
  $('messages').replaceChildren(); if(!current?.messages.length)return;
  for(const message of current.messages){const node=document.createElement('article');node.className='message '+message.role;
    const heading=document.createElement('h3');heading.textContent=message.role==='user'?'Вы':'ClawIQ';
    const body=document.createElement('div');body.className='body';body.textContent=message.content;node.append(heading,body);
    if(message.imageName){const name=document.createElement('p');name.className='route';name.textContent='Изображение: '+message.imageName+' (не сохранено)';node.append(name);}
    if(message.route){const route=document.createElement('div');route.className='route';route.textContent=message.route.kind+' → '+message.route.model+' · локально\n'+message.route.reason;node.append(route);}
    if(message.status==='failed'||message.status==='pending'){const note=document.createElement('p');note.className='failed';note.textContent='Ответ не завершён. Повторите запрос.';node.append(note);}
    $('messages').append(node);
  } $('messages').scrollTop=$('messages').scrollHeight;
}
async function status(){const s=await call(window.clawiq.status());$('status').textContent=s.available?'Ollama доступна · '+s.models.join(' · '):'Ollama недоступна. Запустите Ollama; история доступна без модели.';}
function renderImage(){$('image-name').textContent=image?.name??'';$('clear-image').hidden=!image;}
$('refresh').addEventListener('click',()=>status().catch(e=>error(e.message)));
$('new').addEventListener('click',async()=>{try{current=await call(window.clawiq.create());$('messages').replaceChildren();image=null;renderImage();error('');await list();$('prompt').focus();}catch(e){error(e.message);}});
$('attach').addEventListener('click',async()=>{try{image=await call(window.clawiq.pickImage());renderImage();}catch(e){error(e.message);}});
$('clear-image').addEventListener('click',()=>{image=null;renderImage();});
$('delete').addEventListener('click',async()=>{if(!current||!confirm('Удалить этот разговор с компьютера?'))return;try{await call(window.clawiq.remove(current.id));current=null;$('messages').replaceChildren();image=null;renderImage();await list();}catch(e){error(e.message);}});
$('composer').addEventListener('submit',async event=>{event.preventDefault();const text=$('prompt').value.trim();if(!text||busy)return;error('');setBusy(true);
  try{if(!current)current=await call(window.clawiq.create());current=await call(window.clawiq.send({sessionId:current.id,text,imageId:image?.id}));$('prompt').value='';image=null;renderImage();render();await list();}
  catch(e){error(e.message);if(current){current=await call(window.clawiq.get(current.id));render();await list();}}
  finally{setBusy(false);}
});
$('prompt').addEventListener('keydown',event=>{if(event.key==='Enter'&&!event.shiftKey){event.preventDefault();$('composer').requestSubmit();}});
document.querySelectorAll('[data-prompt]').forEach(button=>button.addEventListener('click',()=>{$('prompt').value=button.dataset.prompt;$('prompt').focus();}));
(async()=>{await status();await list();})().catch(e=>error(e.message));
