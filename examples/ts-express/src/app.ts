import express, { type ErrorRequestHandler } from 'express';

type JobResponse = { id: number; title: string };

function parseTitle(input: unknown): string {
  if (typeof input !== 'object' || input === null || !('title' in input)
      || typeof input.title !== 'string') {
    throw new Error('Başlık metin olmalı.');
  }
  const title = input.title.trim();
  if (title.length < 3 || title.length > 80) {
    throw new Error('Başlık 3-80 karakter olmalı.');
  }
  return title;
}

export function createApp() {
  const app = express();
  const jobs: JobResponse[] = [];
  app.disable('x-powered-by');
  app.use(express.json({ limit: '8kb' }));
  app.get('/health', (_request, response) => { response.json({ status: 'ok' }); });
  app.get('/api/jobs', (_request, response) => { response.json(jobs); });
  app.post('/api/jobs', (request, response) => {
    let title: string;
    try { title = parseTitle(request.body as unknown); }
    catch { response.status(400).json({ error: 'Başlık 3-80 karakter metin olmalı.' }); return; }
    const job: JobResponse = { id: jobs.length + 1, title };
    jobs.push(job);
    response.status(201).json(job);
  });
  app.use((_request, response) => { response.status(404).json({ error: 'Adres bulunamadı.' }); });
  const errors: ErrorRequestHandler = (error: unknown, _request, response, next) => {
    if (response.headersSent) { next(error); return; }
    const status = typeof error === 'object' && error !== null && 'status' in error ? error.status : 500;
    const safeStatus = status === 413 ? 413 : status === 400 ? 400 : 500;
    response.status(safeStatus).json({ error: safeStatus === 413 ? 'Gövde çok büyük.' : safeStatus === 400 ? 'Geçerli JSON gönder.' : 'Sunucu hatası.' });
  };
  app.use(errors);
  return app;
}
