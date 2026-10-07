const { contextBridge, ipcRenderer } = require('electron');
contextBridge.exposeInMainWorld('clawiq', Object.freeze({
  status: () => ipcRenderer.invoke('clawiq:status'),
  list: () => ipcRenderer.invoke('clawiq:list'),
  create: () => ipcRenderer.invoke('clawiq:create'),
  get: id => ipcRenderer.invoke('clawiq:get', id),
  remove: id => ipcRenderer.invoke('clawiq:delete', id),
  send: input => ipcRenderer.invoke('clawiq:send', input),
  pickImage: () => ipcRenderer.invoke('clawiq:image')
}));
