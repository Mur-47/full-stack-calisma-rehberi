# Doğrulama kapsamı — v0.2.0

Tarih: **23 Kasım 2026**. Ortam: Windows, .NET SDK **10.0.401**, EF Core
**10.0.15**, Node.js **24.22.2**, Python **3.11**, ReportLab **5.1.0**,
pypdf **7.1.1**. Denemeler sentetik verilerle ayrı çalışma alanında yapıldı.

## PR #1'in altı düzeltmesi

İncelenen head: `07aeed2f4bc3c3248c42f10efa1dc3e5c8da6883`.
[PR #1](https://github.com/Mur-47/full-stack-calisma-rehberi/pull/1)
birleştirildi; merge commit: `d2c7a355e53fad5704f5bdace54e03b6a76dbcbb`.

- Üç PowerShell isteğinde UTF-8 charset var. Ayrı sentetik HTTP alıcısına Windows PowerShell ile Türkçe JSON gönderildi; sunucu doğru karakterleri okudu ve 201 döndü.
- C# sınıfının ayrı dosyada veya üst düzey deyimlerden sonra tutulması açıklaması kaynakta doğrulandı. Bu ilk kısa kesit için ayrı bir CS8803 negatif derleme denemesi çalıştırılmadı; yeni .NET projesi derlendi ve test edildi.
- PORT ortam değişkeni ayrı boş portla çalıştırılarak doğrulandı.
- İki city URL'sinde encodeURIComponent kullanımı kaynakta doğrulandı.
- Git laboratuvarında $lab yeniden tanımı kaynakta doğrulandı.
- Conflict deneyinde title.txt hedefi kaynakta doğrulandı.

Bu head'de `node verify.mjs`: **6/6 birim testi, 8/8 HTTP kontrolü**. Aşağıdaki yeni sürüm sonuçları bundan ayrı koşulardır.

## Yeni sürümde çalıştırılanlar

Komutlar aksi belirtilmedikçe repo kökünden çalıştırılır.

### Yayın denetimi

```powershell
python -m unittest discover -s scripts -p 'test_*.py'
python scripts/build_pdf.py
python scripts/check_publication.py
git diff --check
```

- Yayın denetimi birim testleri: **8/8**.
- check_publication yerel, Git tarafından dışlanan özel terim dosyasıyla çalıştırıldı. Kaynak dosyalar, yerel Markdown bağlantıları ve PDF metni geçti. Özel terimler bu rapora veya betiğe yazılmadı.
- PDF yeniden üretildi: **127 sayfa, 44 bölüm, yaklaşık 34.500 kelime**. Türkçe metin çıkarma, yer imleri ve kenar taşması kontrol edildi. Tüm sayfalar PNG'ye render edildi; genel sayfa düzenleri ve örnek sayfalar görsel incelendi.
- git diff --check geçti. Otomatik kontrol tek başına içerik doğruluğunu ölçmez; görsel ve teknik kontroller birlikte kullanıldı.

### Bağımlılıksız Node örneği

```powershell
cd examples/node-is-listesi
node verify.mjs
```

**6/6 birim testi + 10/10 HTTP kontrolü; başarısız/atlanmış 0.** Büyük gövde 413; son parçası gönderilmeyen büyük akış da yanıt alıyor. Geçersiz JSON 400. Betik kendine boş port seçiyor ve yalnız kendi sürecini kapatıyor.

### Gerçek .NET API ve xUnit

```powershell
cd examples/dotnet-study
dotnet tool restore
dotnet ef migrations add InitialJobs --project StudyApi --startup-project StudyApi --context StudyDb
python verify.py
dotnet list StudyLab.sln package --include-transitive --vulnerable --format json
```

Migration üretimi bu sürümü hazırlarken **bir kez** çalıştırıldı; migration dosyaları depoya eklendi. Depoyu kullanan kişi InitialJobs'i yeniden üretmez. `verify.py`, locked restore ve gerçek dotnet test koşusunu çalıştırır, yeni TRX dosyasını okur: **20/20 xUnit testi; başarısız/atlanmış 0**.

Kapsam: HTTP durumları, UTF-8 JSON, DTO alan sınırı, version yarışı, iki context ile gerçek SQLite concurrency, migration tekrar uygulandığında verinin korunması, iki firma/model önbelleği, filtreli ExecuteUpdate/Delete, filtresiz raw SQL ve okuma filtresinin INSERT koruması olmaması. Beklenmeyen DB arızasında Production ortamında genel ProblemDetails yanıtı da test edildi. OOP, generics, LINQ ve sabit saat örnekleri test edildi.

NuGet denetimi koşu anında bilinen güvenlik açığı bildirmedi. Bu sonuç yeni duyurularla değişebilir; bağımlılık raporunu güncel ortamda tekrar oku.

### TypeScript ve Express

```powershell
cd examples/ts-express
npm ci --ignore-scripts
npm test
```

**TypeScript strict derlemesi geçti; 3/3 HTTP testi; başarısız/atlanmış 0.** Express 5.3.0, TypeScript 7.0.2. Doğru DTO, fazladan girdi alanları, yanlış tür, boş/uzun başlık, bozuk JSON, büyük gövde, health ve 404 senaryoları kapsanıyor. npm denetimi koşu anında bilinen açık bildirmedi.

## Çalıştırılmayanlar ve kalan sınırlar

- Docker motoru/CLI bu çalışma ortamında erişilebilir değildi. Dockerfile, non-root kullanıcı, `/data` sahipliği ve port ayarları kod üzerinden incelendi; **Docker build, Compose migration/up ve Caddy akışı çalıştırılmadı**.
- Linux/macOS, gerçek SSH bağlantısı, systemd servisi ve internet dağıtımı denenmedi.
- Git stash/reflog/bisect/cherry-pick derslerinin tüm komut dizileri bu yayın için baştan sona otomatik çalıştırılmadı.
- Kitaptaki her bağımsız kod kesiti derlenmedi. Çalışan örnek projelerin sonuçları, bütün kitabın her olası girdide doğrulandığı anlamına gelmez.
- Mini API'lerde kimlik doğrulaması yok. TenantStudyDb yalnız filtre davranışı laboratuvarıdır; firma izolasyonunun tamamlanmış ürün uygulaması olarak sunulmaz.
- Yükseltme testi mevcut ilk migration'ın tekrar uygulanmasını sınar. Henüz ikinci şemaya eski veriden geçiş senaryosu yok.
- GitHub Actions üzerinde bu sürümün CI koşusu yapılmadı; yukarıdaki sonuçlar CO'nun yerel koşularıdır. Claude'un önceki teslim beyanları bunlarla birleştirilmedi.
- v0.1.0 etiketi ve eski Git geçmişi yeniden yazılmadı. Özel terimlerin kaynak betikten kaldırılması ileriye dönük düzeltmedir.

Rehber uygulama ve geri bildirimle geliştirilen öğrenme malzemesidir. Örnekleri yerel laboratuvarda kullan; gerçek ürün için yetki, veri koruma, operasyon ve bağımlılık kararlarını ayrıca tasarla.
