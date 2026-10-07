import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, rm } from 'node:fs/promises';
import { join } from 'node:path';
import { tmpdir } from 'node:os';
import { SessionStore } from '../core/store.mjs';
import { Assistant } from '../core/assistant.mjs';
import { chooseRoute } from '../core/router.mjs';
test('routes image to vision, code to coder with local fallback, and marks research limits',()=>{
  assert.equal(chooseRoute('что здесь?',true,['qwen2.5vl:7b']).model,'qwen2.5vl:7b');
  assert.equal(chooseRoute('отладь код',false,['qwen2.5-coder:14b','qwen3:14b']).model,'qwen2.5-coder:14b');
  assert.equal(chooseRoute('отладь код',false,['qwen3:14b']).model,'qwen3:14b');
  assert.equal(chooseRoute('найди новости',false,['qwen3:14b']).toolsAvailable,false);
  assert.throws(()=>chooseRoute('фото',true,['qwen3:14b']));
});
test('stores separate conversations, restores context after restart and deletes locally',async()=>{
  const root=await mkdtemp(join(tmpdir(),'clawiq-core-'));
  try{
    const store=new SessionStore(root), a=await store.create(), b=await store.create();let sent;
    const fetchImpl=async(url,options)=>url.endsWith('/api/tags')?{ok:true,json:async()=>({models:[{name:'qwen3:14b'}]})}:{ok:true,json:async()=>{sent=JSON.parse(options.body);return{message:{content:'Привет'}};}};
    const assistant=new Assistant(store,{fetchImpl});
    await assistant.send({sessionId:a.id,text:'Привет'});
    const restored=new Assistant(new SessionStore(root),{fetchImpl});
    await restored.send({sessionId:a.id,text:'Продолжим'});
    assert.deepEqual(sent.messages.slice(1).map(m=>m.content),['Привет','Привет','Продолжим']);
    assert.equal((await store.get(b.id)).messages.length,0);
    assert.equal((await store.get(a.id)).messages.length,4);
    await store.delete(a.id);assert.equal((await store.list()).length,1);
    assert.throws(()=>store.path('../private'));
  }finally{await rm(root,{recursive:true,force:true});}
});
test('failed request is persisted but excluded from subsequent context',async()=>{
  const root=await mkdtemp(join(tmpdir(),'clawiq-failure-'));
  try{const store=new SessionStore(root),s=await store.create();let failed=true,body;
    const fetchImpl=async(url,options)=>url.endsWith('/api/tags')?{ok:true,json:async()=>({models:[{name:'qwen3:14b'}]})}:{ok:!failed,status:503,json:async()=>{body=JSON.parse(options.body);return {message:{content:'Ответ'}};}};
    const assistant=new Assistant(store,{fetchImpl});await assert.rejects(assistant.send({sessionId:s.id,text:'Первый'}));
    assert.equal((await store.get(s.id)).messages[0].status,'failed');failed=false;
    await assistant.send({sessionId:s.id,text:'Повтор'});assert.equal(body.messages.length,2);assert.equal(assistant.busy,false);
  }finally{await rm(root,{recursive:true,force:true});}
});
