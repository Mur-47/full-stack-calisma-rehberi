import http from 'node:http';
import { readFile } from 'node:fs/promises';
import { createStore, InputError } from './domain.mjs';

const store = createStore();
const files = new Map([
  ['/', ['index.html', 'text/html; charset=utf-8']],
  ['/app.mjs', ['app.mjs', 'text/javascript; charset=utf-8']],
  ['/styles.css', ['styles.css', 'text/css; charset=utf-8']]
]);

function json(response, status, value) {
  response.writeHead(status, {
    'Content-Type': 'application/json; charset=utf-8',
    'Cache-Control': 'no-store'
  });
  response.end(JSON.stringify(value));
}

async function bodyJson(request) {
  const chunks = [];
  let size = 0;
  let tooLarge = false;
  for await (const chunk of request) {
    size += chunk.length;
    if (size > 8192) {
      tooLarge = true;
      chunks.length = 0;
    }
    if (!tooLarge) chunks.push(chunk);
  }
  if (tooLarge) {
    throw new InputError('İstek gövdesi çok büyük.');
  }
  try {
    return JSON.parse(Buffer.concat(chunks).toString('utf8'));
  } catch {
    throw new InputError('Geçerli JSON gönderin.');
  }
}

const server = http.createServer(async (request, response) => {
  try {
    const url = new URL(request.url, 'http://127.0.0.1:5310');
    if (request.method === 'GET' && files.has(url.pathname)) {
      const [name, type] = files.get(url.pathname);
      const data = await readFile(new URL('./public/' + name,
        import.meta.url));
      response.writeHead(200, { 'Content-Type': type });
      response.end(data);
      return;
    }
    if (request.method === 'GET' && url.pathname === '/api/jobs') {
      json(response, 200, store.list());
      return;
    }
    if (request.method === 'POST' && url.pathname === '/api/jobs') {
      const type = request.headers['content-type'] ?? '';
      if (!type.startsWith('application/json')) {
        json(response, 415, { error: 'JSON gerekli.' });
        return;
      }
      const job = store.add(await bodyJson(request));
      json(response, 201, job);
      return;
    }
    const match = /^\/api\/jobs\/(\d+)\/complete$/.exec(url.pathname);
    if (request.method === 'POST' && match) {
      const id = Number(match[1]);
      const job = store.complete(id);
      json(response, job ? 200 : 404,
        job ?? { error: 'İş bulunamadı.' });
      return;
    }
    json(response, 404, { error: 'Adres bulunamadı.' });
  } catch (error) {
    if (error instanceof InputError) {
      json(response, 400, { error: error.message });
    } else {
      console.error('İstek işlenemedi:', error.message);
      json(response, 500, { error: 'Sunucu hatası.' });
    }
  }
});

server.requestTimeout = 10000;
server.headersTimeout = 10000;
server.listen(5310, '127.0.0.1', () => {
  console.log('Eğitim: http://127.0.0.1:5310');
});
