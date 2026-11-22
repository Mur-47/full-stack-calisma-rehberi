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

function bodyJson(request, response) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    let size = 0;
    const cleanup = () => {
      request.off('data', data);
      request.off('end', end);
      request.off('error', fail);
      request.off('aborted', aborted);
    };
    const fail = error => { cleanup(); reject(error); };
    const aborted = () => fail(new InputError('İstek kesildi.'));
    const data = chunk => {
      size += chunk.length;
      if (size > 8192) {
        cleanup();
        chunks.length = 0;
        request.pause();
        // Send 413 before closing the socket; do not drain an endless body.
        response.setHeader('Connection', 'close');
        response.once('finish', () => request.destroy());
        json(response, 413, { error: 'İstek gövdesi çok büyük.' });
        reject(new InputError('İstek gövdesi çok büyük.'));
        return;
      }
      chunks.push(chunk);
    };
    const end = () => {
      cleanup();
      try { resolve(JSON.parse(Buffer.concat(chunks).toString('utf8'))); }
      catch { reject(new InputError('Geçerli JSON gönderin.')); }
    };
    request.on('data', data);
    request.once('end', end);
    request.once('error', fail);
    request.once('aborted', aborted);
  });
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
      const job = store.add(await bodyJson(request, response));
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
    if (response.writableEnded || response.destroyed) return;
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
const port = Number(process.env.PORT ?? '5310');
if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error('PORT geçersiz.');
server.listen(port, '127.0.0.1', () => {
  console.log(`Eğitim: http://127.0.0.1:${port}`);
});
