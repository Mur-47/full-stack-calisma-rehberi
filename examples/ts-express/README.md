# TypeScript ve Express girişi

Node.js 24+ ve npm gerekir. Bellekte görev listesi tutan, yalnız localhost'ta çalışan öğretim örneği.

```powershell
npm ci
npm test
npm start
```

Test komutu TypeScript `strict` derlemesini ve üç HTTP testini çalıştırır. Normal sunucu 5312 portunu kullanır; `PORT` değişkeniyle değiştirebilirsin. Testler kendi boş portlarını seçer.

`src/app.ts` uygulamayı kurar ve unknown girdiyi doğrular. `src/server.ts` dinleyiciyi başlatır. TypeScript kaynakları `dist` klasörüne JavaScript olarak derlenir; bu çıktı Git'e eklenmez. TypeScript türleri HTTP girdisini çalışma zamanında doğrulamaz; parseTitle bu işi ayrıca yapar.

Kimlik doğrulaması ve kalıcı veritabanı içermez. Denemelerde sentetik veri kullan. Özgün örnek kodlar [MIT](../../LICENSE-CODE) lisansındadır. Bağımlılıkların kendi lisansları geçerlidir.
