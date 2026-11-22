# Değişiklikler

## v0.2.0 — 23 Kasım 2026

- PR #1'deki PowerShell UTF-8, C# üst düzey deyim sırası, PORT, URL kodlama ve Git laboratuvarı düzeltmeleri alındı.
- Kişiye/kuruma özel yayın denetimi terimleri Git dışında tutulan yerel dosyaya veya ortam değişkenine taşındı. Kaynak kod ve PDF aynı politikayla taranıyor; terim değerleri hata çıktısına yazılmıyor.
- Node gövde sınırı erken 413 ve bağlantı kapatmayla uygulanıyor. Bitmeyen büyük istek için regresyon kontrolü eklendi; HTTP denetimi kendi boş portunu seçiyor.
- .NET yanıtları JobResponse DTO kullanıyor. Context üzerindeki firma kimliğiyle query filter örneği ve ExecuteUpdate/Delete/ExecuteSql ayrımı düzeltildi.
- Dockerfile non-root kullanıcı ve `/data` sahipliği içeriyor; resmî imajın varsayılan HTTP portu açıklandı. Actions örneği checkout v6 / setup-dotnet v5 kullanıyor.
- Çalışan .NET API, migration, lock dosyaları, xUnit testleri ve TRX doğrulama betiği eklendi.
- OOP, generics, LINQ, xUnit, ILogger, ProblemDetails, Git kurtarma, Linux/SSH ve TypeScript/Express dersleri eklendi. TypeScript/Express örneği lock dosyası ve HTTP testleri içeriyor.
- Hitap sen biçiminde birleştirildi; tekrar eden olumsuz açıklamalar azaltıldı. Örnek alanı genel cihaz/görev takibine çevrildi.
- PDF kaynak metinden yeniden üretildi. Ayrıntılı çalıştırma kanıtları ve sınırlar VALIDATION.md içinde.

Eski v0.1.0 etiketi, release dosyası ve Git geçmişi değiştirilmedi. Bu sürümdeki gizlilik düzenlemesi ileriye dönüktür.

## v0.1.0 — 22 Kasım 2026

İlk açık baskı: beş kaynak dosyası, 38 bölüm, bağımlılıksız Node örneği, 24 haftalık rota ve bitirme projesi.
