import fs from 'node:fs';
import net from 'node:net';
import path from 'node:path';
import { spawn, spawnSync } from 'node:child_process';
import assert from 'node:assert/strict';
import http from 'node:http';
import { fileURLToPath } from 'node:url';
const folder=path.dirname(fileURLToPath(import.meta.url));
const test=spawnSync(process.execPath,['--test','domain.test.mjs'],{cwd:folder,encoding:'utf8',windowsHide:true});

assert.equal(test.status,0);
console.log(test.stdout.split('\n').slice(-9).join('\n'));
const portProbe = net.createServer();
await new Promise((resolve, reject) => {
  portProbe.once('error', reject);
  portProbe.listen(0, '127.0.0.1', resolve);
});
const port = portProbe.address().port;
await new Promise(resolve => portProbe.close(resolve));
const child=spawn(process.execPath,['server.mjs'],{cwd:folder,env:{...process.env,PORT:String(port)},windowsHide:true,stdio:'ignore'});
try {
 let ready=false;
 for(let i=0;i<30;i++) {
  if(child.exitCode!==null)throw Error('Server exited');
  try{const r=await fetch(`http://127.0.0.1:${port}/api/jobs`);if(r.ok){ready=true;break}}catch{}
  await new Promise(r=>setTimeout(r,100));
 }
 assert.ok(ready);const base=`http://127.0.0.1:${port}`;let count=0;
 let r=await fetch(base+'/');assert.equal(r.status,200);assert.ok((await r.text()).includes('Sentetik iş listesi'));count++;
 r=await fetch(base+'/api/jobs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({title:'  Sentetik bakım  '})});assert.equal(r.status,201);const job=await r.json();assert.equal(job.title,'Sentetik bakım');count++;
 r=await fetch(base+'/api/jobs/'+job.id+'/complete',{method:'POST'});assert.equal((await r.json()).done,true);count++;
 r=await fetch(base+'/api/jobs/999/complete',{method:'POST'});assert.equal(r.status,404);count++;
 r=await fetch(base+'/api/jobs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({title:9})});assert.equal(r.status,400);count++;
 r=await fetch(base+'/api/jobs',{method:'POST',headers:{'Content-Type':'text/plain'},body:'{}'});assert.equal(r.status,415);count++;
 r=await fetch(base+'/api/jobs',{method:'POST',headers:{'Content-Type':'application/json'},body:'{"title":"'+'x'.repeat(9000)+'"}'});assert.equal(r.status,413);count++;
 // Never send the final chunk: the server must still respond promptly.
 await new Promise((resolve,reject)=>{
  const request=http.request(base+'/api/jobs',{method:'POST',headers:{'Content-Type':'application/json'},timeout:3000},response=>{
   try {assert.equal(response.statusCode,413);response.resume();response.once('end',resolve);}catch(error){reject(error);}
  });
  request.once('error',reject);
  request.once('timeout',()=>request.destroy(new Error('Oversized body was not stopped')));
  request.write('x'.repeat(9000));
 });count++;
 r=await fetch(base+'/api/jobs',{method:'POST',headers:{'Content-Type':'application/json'},body:'{broken'});assert.equal(r.status,400);count++;
 r=await fetch(base+'/api/jobs');assert.equal((await r.json()).length,1);count++;

 console.log('PASS: '+count+' HTTP checks');
} finally {
 child.kill();await new Promise(resolve=>{child.once('exit',resolve);setTimeout(resolve,2000)});
}
