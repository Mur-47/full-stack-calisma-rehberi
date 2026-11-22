# Sıfırdan Mid-Level'a Yazılım (Kitap 2)

Hazırlayan: **Murat AKTAŞ** ([Mur-47](https://github.com/Mur-47))

Bu depodaki ikinci kitap: aynı hedefe (sıfırdan orta seviye geliştiriciye) daha geniş ve derin bir anlatımla giden, yaklaşık **770 sayfalık** Türkçe bir çalışma kitabı. Konular kurgusal bir örnek proje (**AsansörTakip**: asansör bakım firmaları için bir web uygulaması) üzerinden anlatılır.

- **[PDF'yi aç veya indir](sifirdan-mid-level-yazilim.pdf)**
- [Tarayıcıda oku (tek HTML dosyası)](index.html): GitHub HTML'i kod olarak gösterir. Dosyayı indirip tarayıcıda aç.

## İçerik

- **Bölüm 0:** Bu kitapla nasıl çalışılır. Çalışma yöntemi, çalışma defteri, 16 haftalık plan, bitirme projesi ve puanlama.
- **Bölüm 1:** Programlama temelleri, terminal, Git (kurtarma araçları dahil), GitHub, web nasıl çalışır.
- **Bölüm 1B:** JSON, REST API tasarımı, curl / Invoke-RestMethod, ağ kaynaklı hatalar.
- **Bölüm 2:** HTML/CSS özeti, JavaScript (sıfırdan ileri), DevTools ile hata ayıklama, Node.js, npm, Express.
- **Bölüm 2B:** TypeScript, React, MongoDB/Mongoose, MERN, ön yüz güvenliği.
- **Bölüm 3:** .NET, C#, OOP, LINQ, async/await, SOLID, DI, ASP.NET Core, kimlik doğrulama.
- **Bölüm 3B:** SQL, ORM, EF Core, test (xUnit, WebApplicationFactory), .NET'te hata ayıklama, mülakat soruları.
- **Bölüm 4:** Linux, Docker, Compose, HTTPS, dağıtım, CI/CD, test stratejisi.
- **Bölüm 4B:** Güvenlik (OWASP), mimari, hata ayıklama ustalığı ve hata avı vakaları, kariyer, komut kartları, sözlük.

Her konu aynı sırayla ilerler: ne işe yarar → nasıl çalışır → satır satır açıklanmış kod → nerede kullanılır → sık hatalar → alıştırmalar ("hata bul" türü dahil). Çözümler bölüm sonlarındadır.

## İki kitap nasıl birlikte kullanılır?

- Depodaki ana rehber ([../README.md](../README.md)) kısa ve yoğundur. Çalışma düzeni ve bitirme projesiyle bir yol haritası gibi kullanılabilir.
- Bu kitap aynı konuları çok daha ayrıntılı açar. Bir konuda takıldığında ya da derinleşmek istediğinde buraya bak.

## Doğrulama ve sorumluluk

Örneklerin büyük kısmı yazım sırasında bir Windows makinede çalıştırıldı: .NET 10, EF Core, Node 24, PowerShell 5.1, Git, Playwright/Edge. Çalıştırılamayanlar (örneğin Docker daemon gerektirenler) metinde belirtildi. Yine de hata içerebilir; sürümler ve hata mesajları zamanla değişir. Hata bulursan bölüm, beklenen ve gerçek sonuçla birlikte issue aç.

## Lisans

Depo lisansıyla aynıdır:
- Metin ve PDF: **CC BY 4.0**
- Kod örnekleri: **MIT**

Bkz. [../LICENSE](../LICENSE) ve [../LICENSE-CODE](../LICENSE-CODE).
