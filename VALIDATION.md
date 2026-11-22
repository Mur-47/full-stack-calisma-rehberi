# Doğrulama kapsamı

İlk baskı sentetik, yerel verilerle hazırlandı. Gerçek uygulama deposu,
üretim sunucusu veya müşteri verisi yayımlanmadı.

## Çalıştırılanlar

- Kitaptan çıkarılan Node örneğinde 6 birim testi ve 8 HTTP senaryosu.
- C# StudyApi model/endpoint örneklerinin derleme kontrolü.
- PDF için sayfa render kontrolü, Türkçe karakter/metin çıkarma,
  taşma ve bağlantı denetimi.
- Genel sürüm hazırlanırken Node örneği ve PDF üretimi yeniden doğrulanır.

## Sınırlar

Her kod bloğu otomatik test edilmedi. Docker/Compose/Caddy laboratuvarları,
Linux/macOS ortamları ve gerçek internet dağıtımı bu ilk açık sürüm için
baştan sona çalıştırılmış değildir. .NET paketi seçerken kitapta açıklanan
transitif bağımlılık güvenlik uyarılarını ve güncel NuGet denetimini okuyun;
örneği doğrudan üretime taşımayın.

Başarılı derleme güvenlik veya üretim uygunluğu kanıtı değildir. Bu rehber
geri bildirime açık öğrenme malzemesidir; profesyonel yeterlilik garantisi
veya bağımsız güvenlik denetimi değildir.
