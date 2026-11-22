import { test } from 'node:test';
import assert from 'node:assert/strict';
import { createApp } from '../dist/app.js';

async function withServer(action) {
  const server = createApp().listen(0, '127.0.0.1');
  await new Promise(resolve => server.once('listening', resolve));
  try { await action(`http://127.0.0.1:${server.address().port}`); }
  finally { await new Promise((resolve, reject) => server.close(error => error ? reject(error) : resolve())); }
}

test('valid input returns DTO, trims title and ignores extra fields', async () => withServer(async base => {
  const response = await fetch(base + '/api/jobs', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ title: '  Örnek görev  ', id: 99, tenantId: 'other' }) });
  assert.equal(response.status, 201);
  assert.deepEqual(await response.json(), { id: 1, title: 'Örnek görev' });
  assert.equal((await (await fetch(base + '/api/jobs')).json()).length, 1);
}));

test('invalid input and malformed JSON return 400', async () => withServer(async base => {
  for (const input of [{title:42},{title:' '},{title:'x'.repeat(81)},null]) {
    const response = await fetch(base+'/api/jobs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(input)});
    assert.equal(response.status,400);
  }
  assert.equal((await fetch(base+'/api/jobs',{method:'POST',headers:{'Content-Type':'application/json'},body:'{bad'})).status,400);
}));

test('oversized JSON is 413, health and missing route keep their status', async () => withServer(async base => {
  assert.equal((await fetch(base+'/api/jobs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({title:'x'.repeat(9000)})})).status,413);
  assert.equal((await fetch(base+'/health')).status,200);
  assert.equal((await fetch(base+'/missing')).status,404);
}));
