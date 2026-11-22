import fs from 'node:fs';
import net from 'node:net';
import path from 'node:path';
import { spawn, spawnSync } from 'node:child_process';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';
const folder=path.dirname(fileURLToPath(import.meta.url));
const test=spawnSync(process.execPath,['--test','domain.test.mjs'],{cwd:folder,encoding:'utf8',windowsHide:true});

assert.equal(test.status,0);
console.log(test.stdout.split('\n').slice(-9).join('\n'));
const portProbe = net.createServer();
await new Promise((resolve, reject) => {
  portProbe.once('error', reject);
  portProbe.listen(5310, '127.0.0.1', resolve);
});
await new Promise(resolve => portProbe.close(resolve));
const child=spawn(process.execPath,['server.mjs'],{cwd:folder,windowsHide:true,stdio:'ignore'});
try {
 let ready=false;
 for(let i=0;i<30;i++) {
  if(child.exitCode!==null)throw Error('Server exited');
  try{const r=await fetch('http://127.0.0.1:5310/api/jobs');if(r.ok){ready=true;break}}catch{}
  await new Promise(r=>setTimeout(r,100));
 }
 assert.ok(ready);const base='http://127.0.0.1:5310';let count=0;
 let r=await fetch(base+'/');assert.equal(r.status,200);assert.ok((await r.text()).includes('Sentetik iş listesi'));count++;
 r=await fetch(base+'/api/jobs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({title:'  Sentetik bakım  '})});assert.equal(r.status,201);const job=await r.json();assert.equal(job.title,'Sentetik bakım');count++;
 r=await fetch(base+'/api/jobs/'+job.id+'/complete',{method:'POST'});assert.equal((await r.json()).done,true);count++;
 r=await fetch(base+'/api/jobs/999/complete',{method:'POST'});assert.equal(r.status,404);count++;
 r=await fetch(base+'/api/jobs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({title:9})});assert.equal(r.status,400);count++;
 r=await fetch(base+'/api/jobs',{method:'POST',headers:{'Content-Type':'text/plain'},body:'{}'});assert.equal(r.status,415);count++;
 r=await fetch(base+'/api/jobs',{method:'POST',headers:{'Content-Type':'application/json'},body:'{"title":"'+'x'.repeat(9000)+'"}'});assert.equal(r.status,400);count++;
 r=await fetch(base+'/api/jobs');assert.equal((await r.json()).length,1);count++;

 console.log('PASS: '+count+' HTTP checks');
} finally {
 child.kill();await new Promise(resolve=>{child.once('exit',resolve);setTimeout(resolve,2000)});
}
