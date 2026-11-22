# Kalıcı görev listesi — .NET laboratuvarı

Kitaptaki StudyApi kodunun çalıştırılabilir kopyası. .NET 10 SDK gerekir. EF Core ve SQLite paketleri kesin sürümle, transitif bağımlılıklar `packages.lock.json` ile tutulur.

```powershell
dotnet tool restore
dotnet restore StudyLab.sln --locked-mode
python verify.py
```

Python 3.11+ doğrulama betiği locked restore yapar, xUnit testlerini çalıştırır ve TRX içinden sıfır/atlanmış testleri reddeder. Alternatif: `dotnet test StudyLab.sln -c Release`.

## API'yi elle aç

```powershell
dotnet ef database update --project StudyApi --context StudyDb
dotnet run --project StudyApi --urls http://127.0.0.1:5311
```

Varsayılan DB, komutun çalışma dizinindeki `study.db` dosyasıdır. Farklı konum için `DatabasePath` ortam değişkenini ayarla. Geçici öğrenme verisi kullan. Testler API'nin bu dosyasını kullanmaz; her testin ayrı geçici DB'si vardır.

`StudyApi/TenantStudyDb.cs`, firma filtresinin context/model önbelleği davranışı için ayrı bir laboratuvardır. Ana API'ye kimlik doğrulaması veya yetkilendirme sağlamaz. Testler okuma filtresinin INSERT yazma koruması olmadığını da gösterir.

## Docker

`StudyApi` klasöründeki Dockerfile non-root kullanıcı ve yazılabilir `/data` dizini içerir. Compose yalnız loopback portu yayımlar. Önce `docker compose config`, ardından kitapta anlatıldığı gibi build, migration ve up adımlarını kullan. Gerçek uygulama volume'u bağlama.

## Kaynak eşliği

Model, Program.cs, TenantStudyDb ve Dockerfile kod blokları kitaptaki örneklerle birlikte güncellenir. [Doğrulama kapsamı](../../VALIDATION.md) içinde gerçekten çalıştırılan kontroller ve platform sınırları yazılıdır. Özgün örnek kodlar [MIT](../../LICENSE-CODE) lisansındadır.
