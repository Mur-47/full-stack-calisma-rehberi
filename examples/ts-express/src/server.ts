import { createApp } from './app.js';

const port = Number(process.env.PORT ?? '5312');
if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error('PORT geçersiz.');
createApp().listen(port, '127.0.0.1', () => {
  console.log(`Eğitim: http://127.0.0.1:${port}`);
});
