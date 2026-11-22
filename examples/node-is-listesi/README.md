# Yerel Node.js iş listesi

Kitabın JavaScript mini uygulamasının aynı kaynak dosyalarıdır.
Node 24+ kullanın; dış npm bağımlılığı yoktur.

```powershell
npm test
npm start
```

Adres: http://127.0.0.1:5310. Kapatmak için Ctrl+C.
Sunucu kapalıyken `node verify.mjs` 6 birim testi ve 10 HTTP kontrolünü
çalıştırır; yalnız kendi başlattığı süreci kapatır. Test betiği kendi boş portunu seçer. Veriler bellektedir, oturum/yetki yoktur; gerçek veri
kullanmayın ve internete açmayın. Lisans: [MIT](../../LICENSE-CODE).
