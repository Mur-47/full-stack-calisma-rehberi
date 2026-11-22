# C# ile davranışı modellemek: OOP, generics ve LINQ

Önceki API'yi kurdun. Şimdi birkaç dosya büyüdüğünde kodu nasıl okunabilir tutacağını çalış. Bu bölümdeki hedefin bir deseni ezberlemek değil; bir nesnenin hangi veriyi koruduğunu, hangi davranışı sunduğunu ve nerede test edileceğini söyleyebilmek.

## Kapsülleme: geçerli durumu sınıfın içinde tut

Bir alanı herkes değiştirebiliyorsa iş kuralını her çağıranın hatırlaması gerekir. Örneğin negatif dakika kabul etmeyen bir görev tasarlayalım. Constructor ilk geçerli durumu kurar; metot sonraki geçerli duruma geçirir.

```csharp
public sealed class WorkItem
{
    public string Title { get; }
    public int Minutes { get; private set; }

    public WorkItem(string title)
    {
        if (string.IsNullOrWhiteSpace(title))
            throw new ArgumentException("Başlık gerekli.", nameof(title));
        Title = title.Trim();
    }

    public void AddMinutes(int minutes)
    {
        if (minutes <= 0)
            throw new ArgumentOutOfRangeException(nameof(minutes));
        Minutes = checked(Minutes + minutes);
    }
}
```

`private set`, dış kodun Minutes değerini doğrudan değiştirmesini engeller. `checked` tam sayı taşmasını yakalar. `sealed` bu sınıftan alt sınıf türetilmesini kapatır. Her sınıfta aynı seçimleri kullanmak yerine ihtiyacı düşün: burada davranışı küçük ve sabit tutuyoruz.

Elle dene: yeni görev oluştur, 20 dakika ekle, ardından -5 eklemeyi dene. İlk işlemden sonra Minutes=20; ikinci işlem exception üretmeli ve değer 20 kalmalı. Bu son cümle test beklentindir.

## Interface, composition ve kalıtım

Interface bir sözleşmedir. `IClock.UtcNow` çağıran kod, saatin sistemden mi testten mi geldiğini bilmeden zamanı okur. Composition, bir nesnenin başka bir nesneyle işbirliği yapmasıdır. Kalıtım ise bir türün başka türün davranışını genişletmesidir. Çoğu iş uygulamasında bağımlılığı interface üzerinden vermek, büyük bir kalıtım ağacından daha kolay test edilir.

```csharp
public interface IClock
{
    DateTimeOffset UtcNow { get; }
}

public sealed class FixedClock(DateTimeOffset value) : IClock
{
    public DateTimeOffset UtcNow => value;
}
```

Test saatini sabitleyince gece yarısı, ay sonu ve süre aşımı senaryolarını günün belli saatini beklemeden sınarsın. Kodu okurken `DateTime.Now` görürsen hangi saat diliminin iş kuralına ait olduğunu sor. Anı UTC olarak saklamakla kullanıcının yerel gününü hesaplamak ayrı kararlardır.

## Generics: tür bilgisini koruyan tekrar kullanım

`List<WorkItem>` yalnız WorkItem elemanları taşır. `List<object>` kullanırsan her okumada türü yeniden kontrol etmen gerekir. Generics, aynı yapı veya algoritmayı farklı türlerle çalıştırırken bu bilgiyi derleme aşamasında korur.

```csharp
public record Page<T>(IReadOnlyList<T> Items, int Total);

var page = new Page<string>(new[] { "Hazır", "Bekliyor" }, 2);
Console.WriteLine(page.Items[0]);
```

Çıktı `Hazır` olur. Page içindeki T burada string'dir. Aynı kayıt biçimini API'de `Page<JobResponse>` olarak da kullanabilirsin. Henüz tek yerde kullanılan üç satır için büyük bir generic altyapı kurmak yerine, ortak veri biçimi ortaya çıktığında soyutlama yap.

## LINQ: filtrele, dönüştür, sonra çalıştır

```csharp
var jobs = new[]
{
    new { Title = "A", Minutes = 20 },
    new { Title = "B", Minutes = 5 },
    new { Title = "C", Minutes = 35 }
};
var titles = jobs.Where(x => x.Minutes >= 20)
    .OrderByDescending(x => x.Minutes)
    .Select(x => x.Title)
    .ToArray();
Console.WriteLine(string.Join(",", titles));
```

Sonuç `C,A`. Önce hangi satırların kaldığını, sonra sıralamayı, sonra seçilen alanı kağıda yaz. `IEnumerable<T>` bellekte gezinme sözleşmesidir. EF sorgusundaki `IQueryable<T>` ise sağlayıcının SQL'e çevireceği ifadeyi taşır. `ToList` ile veriyi erkenden belleğe aldığında bundan sonraki LINQ işlemleri artık o listededir.

Alıştırma: sadece en uzun görevin başlığını al. Çözüm: OrderByDescending sonrasında `Select(x => x.Title).FirstOrDefault()` kullan. Boş dizide sonucu null bekle; onu çağıran kodda ele al.

# xUnit ile gerçek test projesi ve API doğrulaması

## Çalışan projeyi aç

Depodaki `examples/dotnet-study/StudyLab.sln`, kitapta kurduğun StudyApi'nin aynı model ve endpoint dosyalarını içerir. StudyApi.Tests ayrı bir xUnit projesidir. `.csproj` içindeki ProjectReference uygulama kodunu test projesine bağlar. Test dosyasının adı tek başına onu çalıştırmaz; test SDK'sı, adapter ve test işaretleri birlikte gerekir.

Repo kökünden:

```powershell
Set-Location examples/dotnet-study
dotnet tool restore
dotnet restore StudyLab.sln --locked-mode
dotnet test StudyLab.sln -c Release --no-restore
python verify.py
```

`verify.py` aynı testleri yeniden çalıştırır; günlük kullanımda iki komuttan birini seç. Betik ayrıca TRX içindeki toplam, başarısız ve atlanan sayısını kontrol eder. Örneklerin bellekteki ya da geçici klasördeki sentetik SQLite verileri test bitince kapanır. Gerçek bağlantı bilgisi gerekmez.

## Arrange, Act, Assert

```csharp
[Fact]
public void Positive_minutes_are_added()
{
    // Arrange: başlangıç koşulu
    var item = new WorkItem("Sentetik görev");
    // Act: tek davranış
    item.AddMinutes(20);
    // Assert: gözlenebilir sonuç
    Assert.Equal(20, item.Minutes);
}
```

Fact tek bir senaryodur. Theory ve InlineData aynı beklentiyi farklı girdilerle çalıştırır. Testi önce yanlış beklentiyle çalıştırıp kırmızı sonucu gör; ardından doğru beklentiye dön. Böylece testin gerçekten yürüdüğünü de kontrol edersin. Bu deneyi kendi dalında yap, kırık testi teslim etme.

## Birim testi ile entegrasyon testi

WorkItem testi birim testidir. API testinde WebApplicationFactory uygulamanın gerçek giriş noktasını açar; HTTP istemcisiyle POST gönderir, JSON yanıtını okur ve SQLite üzerinde sonucu sınar. Ağ portu açmadan test host'u içinde istek gönderilir. Böylece yönlendirme, JSON dönüşümü ve EF erişimi birlikte denenir.

Bu örnekte doğrulanan davranışlardan bazıları:

- Boş başlık 400; olmayan kayıt 404; eski version ile güncelleme 409.
- POST yanıtında yalnız Id, Title, Completed ve Version alanları var.
- İstemcinin eklediği id/version/completed alanları yeni kaydın başlangıç değerlerini değiştirmiyor.
- İki context aynı satırı okuduğunda ilk yazma kazanıyor; ikinci SaveChanges concurrency hatası üretiyor.
- Migration boş geçici DB'ye uygulanıyor; tekrar uygulamada mevcut kayıt korunuyor.

Son madde yalnız mevcut migration'ın tekrar uygulanmasını sınar. İkinci şema değişikliğini eklediğinde eski sürümde veri oluşturup yeni sürüme yükselten ayrı bir test yaz. SQLite InMemory sağlayıcısı yerine gerçek SQLite motoru kullanmamızın nedeni, SQL davranışını ve ilişkisel kısıtları da görmek.

## Model önbelleği ve iki firma testi

TenantFilterTests, aynı model önbelleğini paylaşan iki context'i A ve B kimliğiyle açar. Her biri kendi satırını görür. Ek testler ExecuteUpdate ve ExecuteDelete'ın firma filtresini koruduğunu; raw SQL'in ise filtre eklemediğini gösterir. Bir başka test, yalnız okuma filtresi olan modelin başka firma kimliğiyle INSERT'i engellemediğini görünür kılar. Sonuçtan öğrenilecek iş: gerçek üründe yazma koruması da tasarlanmalıdır.

Hata avı: `_tenantId` yerine ilk context'ten alınmış sabit bir Guid ile filtre kurmayı dene. B testi A'nın satırını görüyorsa hata API'de değil modelin parametre bağlamındadır. Değişikliği geri al ve iki testi birlikte yeşil gör.

# ILogger ve ProblemDetails: hatayı okunabilir kılmak

## Anlamlı olay alanları

`ILogger<Program>` olayın kaynağını belirtir. Şablondaki JobId ayrı alan olarak tutulabilir; günlükte başlığı veya bütün istek gövdesini taşımaya gerek yoktur.

```csharp
// Endpoint parametrelerine ILogger<Program> logger eklediğinde:
logger.LogInformation("Study job created: {JobId}", job.Id);
```

Bilgi düzeyi normal olayı, Warning beklenen fakat dikkat isteyen durumu, Error işlenemeyen arızayı anlatır. Her başarılı satırı Error yazmak gerçek hatayı bulmayı zorlaştırır. Hata ayıklarken önce zaman aralığı, endpoint ve istek kimliğiyle daralt; sonra uygulamana ait ilk anlamlı stack frame'i oku.

## Ortak hata zarfı

Program.cs örneğinde `AddProblemDetails()` servisi ve `UseExceptionHandler()` middleware'i vardır. Beklenmeyen arızalar Production ortamında genel bir hata yanıtına çevrilir. Beklenen bir iş kuralı için ayrıca şu biçimi kullanabilirsin:

```csharp
return Results.Problem(
    statusCode: 409,
    title: "Kayıt değişti",
    detail: "Güncel kaydı yükleyip tekrar dene.");
```

ProblemDetails; type, title, status, detail ve instance gibi ortak alanlar kullanır. Hassas SQL, dosya yolu, token veya stack trace'i istemciye yazma. Kitaptaki mevcut doğrulama endpoint'leri basit error nesnesi döndürüyor; bu örnekle onları dönüştürmek ayrı, testli bir API sözleşmesi değişikliğidir. Framework farklı hata kaynaklarını kendiliğinden senin seçtiğin tek biçime dönüştürmeyebilir; her yanıt türünü test et.

Alıştırma: başlık doğrulamasının 400 yanıtını ProblemDetails'e dönüştür. Çözümde status 400 ve sabit, anlaşılır title bekle; girdi başlığını hata detail alanına kopyalama. Sonra mevcut HTTP testini yeni sözleşmeye göre güncelle.

# Git kurtarma atölyesi: değişikliği kaybetmeden ilerlemek

Bu komutları önceki Git laboratuvarındaki deneme deposunda çalış. Her adımın başında `git status` oku. Çalışma ağacı dosyaları, index ve commit geçmişi üç ayrı alan olarak düşünülür.

## Stash: bitmemiş işi geçici sakla

```powershell
git status
git stash push -u -m 'yarim form denemesi'
git stash list
git stash show --stat 'stash@{0}'
git stash apply 'stash@{0}'
git status
```

`-u` untracked dosyaları da alır; ignored dosyalar bu seçeneğe dahil olmaz. Apply kaydı listeden silmeden uygular. Sonucu kontrol ettikten sonra `git stash drop 'stash@{0}'` ile o kaydı kaldırabilirsin. Çatışma çıkarsa dosyadaki iki niyeti okuyup çöz. Stash bu bilgisayardadır; ekip arkadaşına aktarılacak iş için commit ve dal daha izlenebilir olur.

## Reflog: eski HEAD'i bul

```powershell
git reflog --date=iso -n 12
```

Reflog yerel referans hareketlerini listeler. Aradığın commit'i bulunca önce `git show <buldugun-sha>` ile içeriğine bak. Sonra `git branch rescue/onceki-is <buldugun-sha>` komutu o commit'e bir dal adı verir. Böylece mevcut çalışma ağacını sıfırlamadan kayda erişirsin. Süresi dolmuş veya temizlenmiş nesnelerin kurtarılması garanti edilemez; reflog yedeğin yerini tutmaz.

## Cherry-pick: tek commit'i taşı

```powershell
git switch -c fix/tek-duzeltme
git cherry-pick <duzeltme-sha>
```

Cherry-pick commit'in değişikliğini mevcut dalın üzerine uygular ve genellikle yeni kimlikli bir commit oluşturur. Ön koşul olan başka commit'ler varsa onları da anlamalısın. Çatışmada `git status`, çözülmüş dosyalar için `git add`, ardından `git cherry-pick --continue` kullanılır. İşlemden vazgeçersen `git cherry-pick --abort` o devam eden işlemi geri alır.

## Bisect: hatayı getiren commit'i daralt

```powershell
git bisect start
git bisect bad
git bisect good <calisan-eski-sha>
# Git'in seçtiği commit'te aynı küçük testi çalıştır.
# Sonuca göre yalnız birini kullan:
git bisect good
# veya: git bisect bad
# Arama bitince:
git bisect reset
```

Git aralığı ikiye bölerek aday seçer. Testin sonucu kararlı olmalı; her commit'te farklı veri kullanırsan sonuç şaşar. Test komutun güvenilir çıkış kodu üretiyorsa `git bisect run node regression.mjs` ile otomatikleştirebilirsin: 0 iyi, 1-127 arası (125 hariç) kötü; 125 bu commit'i atla demektir. Başlamadan bitmemiş dosyalarını sakla, bitince reset ile başlangıç dalına dön.

# Linux ve SSH: uzak makinede yönünü bulmak

## Önce sadece oku

Terminal açınca hangi bilgisayarda, hangi kullanıcıyla ve hangi klasörde olduğunu öğren. Aşağıdaki komutlar Bash/Linux içindir; PowerShell sözdizimiyle karıştırma.

```bash
whoami
hostname
pwd
ls -la
df -h
free -h
ps -ef
ss -ltn
```

pwd çalışma dizinini, df disk alanını, free belleği, ss dinleyen TCP adreslerini gösterir. `127.0.0.1:8080` yalnız yerel erişimi, `0.0.0.0:8080` bütün IPv4 arayüzlerinde dinlemeyi ifade eder. Bir sürecin varlığını gördüğünde hemen kill kullanmak yerine PID, sahip ve başlatma biçimini kontrol et.

## İzinler ve servis günlükleri

`rwx` okuma, yazma ve yürütme bitleridir. Bir script'i çalıştırabilmek için dosya izni kadar dizinlere erişim de gerekir. Her şeye `chmod 777` vermek yerine hangi kullanıcının hangi klasöre yazması gerektiğini belirle. Örnek container'da uygulama dosyaları okunur, SQLite dizini uygulama kullanıcısına yazılabilir olmalıdır.

```bash
systemctl status study-api --no-pager
journalctl -u study-api --since '10 minutes ago' --no-pager
```

Bu komutlar yalnız bu isimde systemd servisi kurulmuşsa anlamlıdır; kitap otomatik servis kurmaz. Önce hizmetin mevcut olup olmadığını öğren. Günlük çıktısını paylaşırken bağlantı sırlarını ve kişisel verileri maskele.

## SSH bağlantısı

```bash
ssh -i ~/.ssh/study_key learner@host.example
```

host.example yer tutucudur; sahip olduğun deneme makinesinin adresini kullan. İlk bağlantıda host anahtarının parmak izini güvenilir ayrı kanaldan doğrula. Private key bilgisayarında kalır; sunucuya public key eklenir. Parola istemini yanlış kullanıcı veya yanlış anahtar da tetikleyebilir. `ssh -v` teşhise yardım eder, fakat çıktısını herkese açık loga kopyalamadan önce incele.

Alıştırma: bir dosyayı silmeden, taşıma yapmadan ve servis yeniden başlatmadan makinenin çalışma dizinini, disk durumunu ve dinleyen portlarını yaz. Hedefin ilk aşamada dağıtım yapmak değil, ortamı doğru tarif etmektir. Bu baskıda gerçek SSH sunucusuna bağlanma ve Linux servis kurulumu çalıştırılmadı.

# TypeScript ve Express: JavaScript'in üzerine iki araç

## TypeScript hangi bilgiyi ekler?

TypeScript, JavaScript'e derleme aşamasında tür denetimi ekler. Çalışan HTTP isteğinin gerçek gövdesini yine doğrulamalısın. Dış girdiyi unknown kabul edip daraltmak, türü görmezden gelen any kullanmaktan daha açıklayıcıdır.

```typescript
function titleFrom(value: unknown): string {
  if (typeof value !== 'object' || value === null ||
      !('title' in value) || typeof value.title !== 'string') {
    throw new Error('Başlık metin olmalı.');
  }
  const title = value.title.trim();
  if (title.length < 3 || title.length > 80) {
    throw new Error('Başlık 3-80 karakter olmalı.');
  }
  return title;
}
```

İlk if türü daraltır. Trim ve uzunluk kontrolü iş kuralını uygular. `as SomeType` yazmak veriyi dönüştürmez veya doğrulamaz; derleyiciye verdiğin bir iddiadır. HTTP sınırında gerçek kontrolü çalıştır.

## Express hangi parçayı düzenler?

Node çalışma ortamıdır; Express HTTP yönlendirme ve middleware çatısını sağlar. Depodaki `examples/ts-express` aynı küçük görevi bu çatıyla gösterir. `express.json({ limit: '8kb' })` gövde ayrıştırmasını sınırlar. Hata middleware'i dört parametre alır ve diğer rotalardan sonra eklenir. Express 5'te async route'un reddedilen Promise'i hata zincirine aktarılır; kendi yanıtını gönderdikten sonra ikinci yanıt göndermemeye dikkat et.

Repo kökünden:

```powershell
Set-Location examples/ts-express
npm ci
npm test
npm start
```

npm test önce TypeScript derlemesini, sonra HTTP testlerini çalıştırır. Varsayılan adres http://127.0.0.1:5312; farklı port için `PORT` ayarlanabilir. Test kendi boş portunu kullanır. Veriler bellektedir ve uygulama yerel öğrenme içindir.

## Üç küçük görev ve çözüm

1. Gövdeye `{ "title": 42 }` gönder. Beklenen 400. Çözüm: unknown girdide title türünü kontrol et; string olmadığı durumda trim çağırma.
2. Bilerek tür hatası ekle: `const minutes: number = '20';`. Beklenen TypeScript derleme hatası. Çözüm: sayısal bir literal kullan veya dış girdiyi doğrulayarak dönüştür. Sonra örneği eski haline getir.
3. JSON gövdesini 8 KB'dan büyük gönder. Beklenen 413. Çözüm: error middleware'inde body parser'ın durumunu koru; bütün hataları 500'e çevirme.

Yeni bir framework öğrendiğinde aynı özelliğin veri yolunu tekrar çiz: istek, JSON ayrıştırma, doğrulama, iş kuralı, DTO, yanıt. Araç adları değişse de bu zinciri izleyebilmek kod okumayı taşınabilir bir beceri yapar.

## Kaynaklar ve bir sonraki deneme

- C# türleri ve dil temelleri: https://learn.microsoft.com/dotnet/csharp/fundamentals/
- ASP.NET Core entegrasyon testleri: https://learn.microsoft.com/aspnet/core/test/integration-tests
- xUnit başlangıç: https://xunit.net/docs/getting-started/v2/getting-started
- ProblemDetails ve hata işleme: https://learn.microsoft.com/aspnet/core/fundamentals/error-handling
- EF Core global sorgu filtreleri: https://learn.microsoft.com/ef/core/querying/filters
- EF Core toplu işlemler: https://learn.microsoft.com/ef/core/saving/execute-insert-update-delete
- Git kurtarma araçları: https://git-scm.com/docs/git-stash ve https://git-scm.com/docs/git-reflog
- Git bisect ve cherry-pick: https://git-scm.com/docs/git-bisect ve https://git-scm.com/docs/git-cherry-pick
- OpenSSH kılavuzu: https://www.openssh.com/manual.html
- TypeScript tür daraltma: https://www.typescriptlang.org/docs/handbook/2/narrowing.html
- Express hata işleme: https://expressjs.com/en/5x/guide/error-handling/

Bu bölümü bitirince görevini seç: bir test ekle, küçük bir hatayı o testle yakala, düzelt ve PR açıklamasına önce/sonra davranışını yaz. Çözümün değeri, okuduğun sayfa sayısıyla birlikte kendi ürettiğin kanıtla görünür olur.
