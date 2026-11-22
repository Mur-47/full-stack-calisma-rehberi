# Sunucu tarafını anlamak: C#, .NET ve bir isteğin yolculuğu

Bu bölümde bilgisayarın arkasında çalışan tarafı kuracağız. Bir kullanıcı ekranda “İşi tamamla” düğmesine bastığında tarayıcı tek başına güvenilir bir kayıt tutamaz. Kullanıcının kim olduğunu, hangi firmanın işini değiştirebildiğini, kaydın başka biri tarafından değiştirilip değiştirilmediğini ve değişikliğin kalıcı olarak yazılıp yazılmadığını sunucu denetler. Bu sorumluluğa backend, yani arka uç denir.

Bir asansör bakım firmasının ofisini düşünün. Ön yüzdeki form, görevliye verilen kağıttır. API, kağıdın hangi masaya gideceğini belirleyen gişedir. İş kuralı, görevlinin uyguladığı prosedürdür. Veritabanı, düzenli arşivdir. Docker ise ofisin bütün işleyişini başka binada aynı biçimde kurabilmek için hazırlanan paketlemeye benzer. Benzetme başlangıç içindir: Docker gerçek bir bina, veritabanı da sadece dosya dolabı değildir. Teknik ayrıntıları birazdan ayıracağız.

Okuma sonunda bir terimi ezberlemiş olmanız yetmez. Bir API isteğini takip ederek şu soruları cevaplayabilmelisiniz: İstek hangi endpoint'e girdi? Verisi nerede doğrulandı? Kimlik nereden geldi? Hangi SQL çalıştı? Hangi satır değişti? Hata olduğunda kullanıcıya ne, günlüğe ne yazıldı? Tekrar gönderilen istek ikinci kez para veya stok hareketi oluşturabilir mi? Orta seviyeye giden yol, bu soruları gerçek kod üzerinde cevaplayabilmekten geçer.

## C#, .NET, ASP.NET Core aynı şey değildir

C# bir programlama dilidir. Değişken, koşul, döngü, sınıf, metot ve tür sistemini bu dilin kurallarıyla yazarsınız. JavaScript nasıl bir dilse C# da dildir. C# kodunu bir tarayıcının sıradan JavaScript motoruna verip çalıştıramazsınız.

.NET, C# gibi dillerle yazılan programların geliştirilmesini ve çalışmasını sağlayan platformdur. Çalışma zamanı, standart kütüphaneler, derleme araçları ve paketleme olanakları içerir. Runtime, hazırlanmış uygulamayı çalıştırır. SDK ise geliştirme araçlarını ve runtime'ı içerir. Yalnız runtime kurulu bir bilgisayar uygulamayı çalıştırabilir fakat kaynak kodunu derlemek için gereken SDK bulunmayabilir.

ASP.NET Core, .NET üzerinde web uygulaması ve API geliştirmek için kullanılan çerçevedir. HTTP isteğini okuma, endpoint eşleştirme, kimlik doğrulama, günlükleme ve bağımlılıkları sağlama gibi ortak işleri düzenler. Her C# uygulaması web uygulaması değildir; bir yedekleme aracı da C# olabilir. Her .NET uygulaması ASP.NET Core kullanmaz.

.NET Framework, ağırlıkla eski Windows uygulamalarında karşılaşılan ayrı ürün hattıdır. Modern .NET ile ad benzerliği vardır fakat “Framework 4.8” ile “.NET 10” aynı sürüm dizisinin ardışık iki halkası değildir. Eski bir projeyi okurken hedef çerçeveyi proje dosyasından kontrol edin. İnternette bulduğunuz yıllanmış ASP.NET MVC veya EF6 örneğini modern ASP.NET Core projesine aynen taşımanız derleme ve davranış sorunları yaratabilir.

Bu kitabın C# uygulama örnekleri .NET 10 hedefler. Bu, her bilgisayarda kendiliğinden kurulu olduğu anlamına gelmez. PowerShell'de önce şunları çalıştırın:

```powershell
dotnet --info
dotnet --list-sdks
```

İlk komut ortam bilgilerini, ikinci komut kullanılabilir SDK'ları gösterir. Çıktı sürüm ve kurulum yoluna göre değişir. Buradaki hedef, `10.0` ailesinden SDK bulunmasıdır. `dotnet` tanınmıyorsa önce resmi .NET kurulumunu ve terminalin PATH bilgisini kontrol edin. Yeni kurulumdan sonra eski terminal penceresi yeni PATH'i görmeyebilir. Proje klasöründe `global.json` varsa SDK seçimini o dosya etkiler. Rastgele kaldırmak yerine dosyanın ne istediğini okuyun.

## C# kodunu ilk kez okumak

Yeni bir öğrenme klasöründe şu denemeyi yapın. Gerçek uygulamanın kaynak klasöründe veya canlı veri dizininde çalışmayın.

```powershell
New-Item -ItemType Directory -Force C:\KodAtolyesi | Out-Null
Set-Location C:\KodAtolyesi
dotnet new console -n IlkCSharp -f net10.0
Set-Location IlkCSharp
```

`Program.cs` içeriğini şu hale getirin:

```csharp
string building = "Örnek Apartmanı";
int floorCount = 8;
bool maintenanceDue = true;

Console.WriteLine(building);
Console.WriteLine($"Kat sayısı: {floorCount}");

if (maintenanceDue)
{
    Console.WriteLine("Bakım planına ekle.");
}
```

`string` metin, `int` tam sayı, `bool` doğru veya yanlış bilgisidir. C# türleri derleme sırasında kontrol eder. `floorCount = "sekiz";` yazarsanız türler uyuşmadığı için program derlenmez. Bu, uygulama sunucuda çalışırken müşterinin karşılaşacağı hata değildir; geliştirme sırasında yakalanan hatadır. Derleme hatası ile çalışma zamanı hatasını ayırın.

```powershell
dotnet run
```

Ekranda apartman adı, kat sayısı ve bakım cümlesi görünmelidir. Sonra koşulu `false` yapıp yeniden çalıştırın. Son cümlenin kaybolmasının nedenini bir cümleyle açıklayın. Bu küçük değişiklik, kopyaladığınız kodu gerçekten anlamanız için ilk kontroldür.

## Metot, parametre ve dönüş değeri

Metot, isim verilmiş iş parçasıdır. Aynı hesabı farklı yerlerde tekrar yazmak yerine bir kez tanımlarsınız. Parametre, metodun dışarıdan aldığı bilgidir. Dönüş değeri, hesap sonunda dışarı verdiği sonuçtur.

```csharp
static long CalculateTotal(long unitPriceCents, int quantity)
{
    if (quantity < 0)
    {
        throw new ArgumentOutOfRangeException(nameof(quantity));
    }

    return checked(unitPriceCents * quantity);
}

long total = CalculateTotal(12500, 3);
Console.WriteLine(total);
```

Sonuç `37500` olur; bu örnekte kuruş cinsinden 375 liradır. Para örneğinde `long` kullanmamızın nedeni kesirli ikili sayı gösteriminin bazı ondalık değerleri tam tutmamasıdır. Bütün finansal tasarımlar mutlaka bu biçimi kullanır demiyoruz; para birimi, yuvarlama ve veritabanı türü bilinçli seçilmelidir. Kuruş tutan bir projede 125 lirayı `125` olarak göndermek yüz kat hata doğurur.

`checked`, taşmanın sessizce yanlış sayıya dönmesini önler. `throw`, işlemin geçerli biçimde devam edemediğini belirtir. Her metotta exception fırlatmak iyi tasarım değildir. Kullanıcının geçersiz form girdisi için anlaşılır doğrulama yanıtı, beklenmeyen arıza için exception ve merkezi hata yönetimi kullanmak farklı sorumluluklardır.

## Sınıf, nesne, record ve nullable

Sınıf bir veri veya davranış tipini tanımlar; nesne onun bellekteki örneğidir. İki iş emri aynı sınıftan üretilebilir ama farklı kimlik ve başlık taşır.

```csharp
public class Job
{
    public int Id { get; set; }
    public string Title { get; set; } = "";
    public bool Completed { get; set; }
    public DateTime? CompletedAt { get; set; }
}
```

`public`, dışarıdan erişime izin verir. `get` okuma, `set` atama erişimidir. `DateTime?`, tarih bilgisinin boş olabileceğini belirtir. Bitmemiş işte `CompletedAt` bulunmaması doğaldır. Boş tarihi `DateTime.MinValue` gibi anlamsız bir değerle doldurmak yerine “değer yok” durumunu açık modellemek daha okunaklıdır.

```csharp
var first = new Job { Id = 1, Title = "Kapı kontrolü" };
var second = first;
second.Title = "Kilit kontrolü";
Console.WriteLine(first.Title);
```

Çıktı `Kilit kontrolü` olur. İkinci değişken yeni iş kopyası değildir; aynı nesneye başka referanstır. JavaScript'teki nesne referansı mantığıyla benzerlik kurabilirsiniz. Nesne kopyalamak, veritabanında yeni kayıt oluşturmak ve başka değişkene referans atamak ayrı işlemlerdir.

`record`, özellikle veri taşımak için kullanışlı C# türüdür. Örneğin API girdisini şöyle tanımlayabiliriz:

```csharp
public record CreateJobInput(string Title);
```

Bu tür, veritabanındaki Job sınıfının tamamını istemciye açmamak için kullanılacaktır. “DTO” sözcüğünü gördüğünüzde korkmayın: Data Transfer Object, katmanlar arasında taşınacak veri biçimi demektir. Bir nesnenin bütün alanlarını her yere taşımak zorunda değilsiniz.

## async ve await: beklemek ile hesaplamak farklıdır

Veritabanı, ağ ve dosya işlemleri zaman alabilir. ASP.NET Core bir istekte veritabanını beklerken iş parçacığını gereksiz yere bloke etmemelidir. `Task` gelecekte tamamlanacak işi, `await` o işin sonucunun asenkron biçimde beklenmesini ifade eder.

```csharp
var jobs = await db.Jobs
    .OrderBy(x => x.Id)
    .Take(20)
    .ToListAsync(cancellationToken);
```

Burada beklenen iş veritabanı sorgusudur. `.Result` veya `.Wait()` ekleyerek asenkron kodu zorla bloklamak, özellikle web sunucusunda gereksiz iş parçacığı tüketebilir. `async` sözcüğü bir işlemi otomatik olarak hızlı veya paralel yapmaz. Bir milyon elemanı hesaplayan saf CPU döngüsü, önüne async yazınca daha az hesap yapmaz.

CancellationToken, isteğin artık sonucuna ihtiyaç kalmadığını işbirlikçi olarak bildirebilir. Kullanıcı sayfadan ayrıldığında sorgunun sonsuza kadar devam etmesini istemeyebilirsiniz. Ancak iptal geldi diye daha önce tamamlanmış veritabanı yazmasını otomatik olarak geri alınmış sanmayın. İşlemin hangi aşamada olduğunu ve transaction sınırını incelemelisiniz.

# HTTP API: isteği al, doğrula, uygula, cevapla

API, başka yazılımın uygulamanızla konuşmak için kullandığı arayüzdür. Web API'de bu konuşma çoğunlukla HTTP istekleri üzerinden yapılır. Bir endpoint, belirli HTTP metodu ve adres biçiminin birlikte tanımladığı işlem kapısıdır. `GET /api/jobs/12` ile `DELETE /api/jobs/12` aynı adresi kullanabilir ama aynı işlem değildir.

REST, kaynaklar üzerinden tutarlı API tasarlamaya ilişkin bir yaklaşım ailesidir; JSON döndüren her adres kusursuz REST sayılmaz. İlk aşamada hedefiniz etiket tartışması değil, anlaşılır ve öngörülebilir sözleşmedir. Okumayı GET, oluşturmayı POST, belirli kaynağın değişimini PUT veya PATCH gibi uygun yöntemlerle ifade edin. Bu yöntemlerin güvenli/idempotent anlamlarını kendi işinizde gerçekten koruyun.

## İstek gövdesi, rota ve sorgu parametresi

Şu istekte üç ayrı bilgi taşıma yeri vardır:

```text
PUT /api/jobs/12?notify=false
Content-Type: application/json

{"title":"Kapı kontrolü","completed":true,"version":2}
```

`12` rota parametresidir; hangi işin değiştiğini söyler. `notify=false` sorgu parametresidir. JSON, istek gövdesidir. Content-Type gövdenin nasıl yorumlanacağını belirtir. İstemcinin body göndermesi tek başına JSON olduğu anlamına gelmez; sunucunun desteklediği biçimle uyuşmalıdır.

Şifre, token veya kişisel bilgiyi gelişigüzel URL'ye koymayın. URL tarayıcı geçmişi, erişim günlükleri ve ara sistemler üzerinden daha fazla yerde tutulabilir. Ayrıca body kullanmak da tek başına güvenlik sağlamaz: HTTPS, log politikası ve erişim kontrolü ayrı konulardır.

## Durum kodlarını ayırt etmek

`200`, başarılı okuma veya sonuç döndürme için yaygındır. `201`, yeni kaynak oluşturulduğunu; `204`, başarılı fakat gövdesiz yanıtı anlatır. `400`, gönderilen isteğin kabul edilmediğini; `401`, kimliğin doğrulanmadığını; `403`, doğrulanmış kimliğin bu işleme yetkili olmadığını göstermek için kullanılır. `404`, kaynak bulunmadığında; `409`, güncel durumla çakışmada uygundur. `500`, beklenmeyen sunucu hatasıdır.

Her hataya 200 döndürüp JSON içine `success:false` koyarsanız tarayıcı araçları, önbellekler ve izleme sistemleri gerçeği zor anlar. Her doğrulama hatasına 500 döndürürseniz de kullanıcı kaynaklı girdiyi sunucu arızası gibi gösterirsiniz. Kod seçimleri API sözleşmesinin parçasıdır.

Bir kullanıcı başka firmanın kayıt kimliğini denediğinde 404 dönmek, kaydın varlığını açıklamamayı sağlayabilir. Fakat bu karar “bütün yetki hataları 404 olmalı” diye genellenmez. Önce güvenlik modeli, sonra tutarlı sözleşme belirlenir. Güvenlik açısından önemli ayrım, yanıtın kaç olduğundan önce izinsiz kayda gerçekten erişilmemesidir.

## DTO neden koruyucu bir sınırdır?

Şu endpoint tehlikeli bir başlangıçtır:

```csharp
app.MapPost("/api/users", (AppUser user) => Save(user));
```

`AppUser` içinde Role, TenantId, Active veya PasswordHash bulunuyorsa, istemcinin değiştirmemesi gereken alanları da kabul ediyor olabilirsiniz. Buna overposting veya mass assignment ailesinden sorunlar denir. İstemciye yalnız işlem için gerekli alanları sunun:

```csharp
public record InviteMemberInput(string Email, string DisplayName);
```

Rol atama ayrı bir yetki denetiminden geçebilir. TenantId, doğrulanmış oturumdan gelir; kullanıcı gövdesine güvenerek firma seçtirilmez. DTO otomatik güvenlik duvarı değildir, fakat kabul edilen veri alanlarını açık hale getirir. Sunucu yine yetki, uzunluk, biçim ve iş kuralını denetlemelidir.

## Validation: biçim doğru, iş doğru mu?

`title` değerinin boş olmaması biçim doğrulamasıdır. “Tamamlanmış işi fatura kesinleştikten sonra tekrar açamazsın” ise iş kuralıdır. “Bu kişi o firmanın yöneticisi mi?” yetki kontrolüdür. Üçünü aynı kontrol sanmayın.

Tarayıcıdaki `required`, `minlength` ve JavaScript doğrulaması kullanıcıya erken geri bildirim verir. Kullanıcı bu kontrolleri DevTools veya başka HTTP istemcisiyle aşabilir. Sunucuda aynı sınırların ve asıl iş kurallarının uygulanması zorunludur. İki taraftaki kurallar farklıysa kullanıcı “hepsi yeşil ama işlem reddediliyor” sorunu yaşar. Şifre karakterleri veya tarih dilimleri gibi konularda, yalnız aynı sayıları yazmak aynı algoritmayı uygulamak değildir.

Mini projede doğrulamayı elle yazacağız. Büyük projelerde DataAnnotations, endpoint filtreleri veya özel doğrulayıcılar kullanılabilir. ASP.NET Core sürümüne ve kullandığınız endpoint yaklaşımına göre otomatik doğrulamanın nasıl devreye girdiğini öğrenin; “DTO'ya attribute koydum, her koşulda kendiliğinden çalışır” varsayımı yapmayın. En sağlam kanıt, hatalı gövde gönderen bir testin beklenen 400'ü almasıdır.

# Bağımlılık enjeksiyonu ve middleware

## DI, sihirli parametre sağlamak değildir

Dependency Injection, bir nesnenin ihtiyaç duyduğu başka nesneleri kendi içinde gelişigüzel üretmek yerine dışarıdan almasıdır. Örneğin endpoint'in veritabanı bağlamına ihtiyacı varsa `new AppDb()` yazmak yerine parametreden alabilir. ASP.NET Core bu nesneyi servis kayıtlarına bakarak sağlar.

```csharp
builder.Services.AddDbContext<StudyDb>(options =>
    options.UseSqlite("Data Source=study.db"));

app.MapGet("/api/jobs", async (StudyDb db) =>
    await db.Jobs.AsNoTracking().ToListAsync());
```

İlk parça, StudyDb'nin nasıl oluşturulacağını kaydeder. İkinci parça bu kaydı kullanır. Constructor injection aynı fikri sınıflar arasında uygular. Testte gerçek e-posta göndericisi yerine sahte gönderici verebilmek de bu ayrım sayesinde kolaylaşır.

Servis ömrü önemlidir. Singleton genellikle uygulama boyunca tek örnektir. Scoped web uygulamasında çoğunlukla istek kapsamıyla ilişkilidir. Transient her çözümlemede yeni örnek verir. DbContext tipik olarak scoped kullanılır. DbContext'i singleton alanına saklamak, hem kapsam hem eşzamanlı kullanım sorunları doğurabilir. “Her şeyi tek nesne yaparsam hızlı olur” iyi bir varsayım değildir.

DbContext aynı anda birden fazla işlemi güvenle yürütmek için tasarlanmış bir nesne değildir. Aynı context üzerinde birden fazla sorguyu aynı anda başlatıp `Task.WhenAll` kullanmanız hata yaratabilir. Asenkron yazmak ile aynı bağlantıda paralel iş başlatmak farklıdır. Önce ölçün, sonra doğru kapsam ve ayrı context gereksinimini değerlendirin.

## Middleware bir kontrol zinciridir

Middleware, isteği endpoint'e ulaşmadan önce veya yanıt dönerken işleyen ara katmandır. Bir güvenlik kontrol noktaları dizisi gibi düşünebilirsiniz. Günlükleme, hata yakalama, kimlik doğrulama ve yetki kontrolü bu zincirde yer alabilir.

```csharp
app.Use(async (context, next) =>
{
    var watch = System.Diagnostics.Stopwatch.StartNew();
    await next(context);
    Console.WriteLine(
        $"{context.Request.Method} " +
        $"{context.Response.StatusCode} {watch.ElapsedMilliseconds}");
});
```

Bu örnek süreyi göstermek içindir; üretimde yapılandırılmış logger kullanılır. Şifreyi veya bütün gövdeyi yazdırmayın. `await next(context)` çağrısı zincirin sonraki parçasına geçer. Çağırmazsanız istek orada kesilir. Sıralama yanlışsa endpoint kimlik oluşmadan yetki kontrol etmeye çalışabilir veya hata yakalayıcı beklediğiniz hatayı göremeyebilir.

Bir isteğin 403 aldığını gördüğünüzde yalnız endpoint kodunu okumayın. Daha önceki middleware, tenant erişim politikası, CSRF filtresi veya ilk şifre değiştirme zorunluluğu isteği durdurmuş olabilir. Debugger'da endpoint'e breakpoint koyup hiç ulaşılmadığını görmek bu ayrımı hızlı yakalatır.

## Authentication, authorization, tenant kontrolü

Authentication, “Sen kimsin?” sorusudur. Authorization, “Bu işlemi yapabilir misin?” sorusudur. Multi-tenant kontrolü ise “Hangi firmanın hangi kaydına bu yetkiyi uyguluyorsun?” sorusunu ekler. Yönetici rolü taşımak, bütün firmaların yöneticisi olmak anlamına gelmez.

Cookie ile kimlik doğrulamada tarayıcı oturum çerezini gönderir. Sunucu çerezin bütünlüğünü ve oturum koşullarını kontrol eder. JWT gibi bearer token yaklaşımında token'ın imzası, süresi, hedefi ve diğer koşulları kontrol edilir. Sadece Base64 içeriğini okumak doğrulama değildir. Bu kitap size kendi kriptografik oturum sisteminizi sıfırdan yazdırmaz; yerleşik ve bakımı yapılan mekanizmaları anlamayı hedefler.

Bir policy, belirli yetki koşullarını isimlendirir. Endpoint'e RequireAuthorization eklemek ile düğmeyi gizlemek aynı şey değildir. Tarayıcı düğmesini kaldırmak kullanıcı deneyimi sağlar; asıl izin sunucuda uygulanır. Aksi durumda kullanıcı doğrudan HTTP isteğiyle görünmeyen işlemi yapabilir.

# SQL ve SQLite: kalıcı veriyi düşünmek

## Tablo, satır ve anahtar

Veritabanı, sadece diske kaydedilmiş nesne listesi değildir. İlişkisel veritabanında tablolar, veri türleri, kısıtlar ve sorgu dili bulunur. Tablo bir kayıt tipini, satır bir kaydı, sütun kaydın bir özelliğini temsil eder. Primary key, satırı benzersiz tanımlar.

Bir apartmanın adı değişebilir; müşterinin e-postası düzeltilebilir. Bu nedenle iş kimliğini başlık gibi değişebilir bir alana bağlamamak önemlidir. `Id=12`, “Kapı kontrolü” başlığı değiştirilse bile aynı işi tanımlar. Kimlik kullanıcıya gösterilse bile güvenlik anahtarı sayılmaz. Tahmin edilemeyen GUID kullanmak da yetki kontrolünün yerine geçmez.

SQLite, veritabanını bir dosyada tutabilen ilişkisel bir motordur. Öğrenme ve bazı gerçek uygulamalar için kullanışlıdır. SQL Server veya PostgreSQL gibi ayrı sunucu süreçleriyle çalışmak zorunlu değildir. Bu kolaylık, bütün verileri rastgele ağ klasörüne koyabileceğiniz veya aynı dosyaya sınırsız eşzamanlı yazma yapabileceğiniz anlamına gelmez. Erişim modeli ve yedekleme yöntemi seçilen motorla uyumlu olmalıdır.

## Bir tabloyu SQL ile okumak

```sql
SELECT Id, Title, Completed
FROM Jobs
WHERE Completed = 0
ORDER BY Id
LIMIT 20;
```

SQL'i yukarıdan aşağıya ezberlemek yerine soruya çevirin: Hangi tablodan? Hangi koşuldaki satırlar? Hangi alanlar? Hangi sıralama? En çok kaç kayıt? Bu sorgu bütün iş verisini çekmez; yalnız istenen sütunları ve açık ilk 20 işi getirir.

`SELECT *` öğrenirken hızlıdır fakat API'de bilinçsizce kullanmak gereksiz veya gizli alanların taşınmasına yol açabilir. Bir kullanıcı kaydında şifre özeti bulunuyorsa “zaten hash” diyerek istemciye göndermemelisiniz. API yanıtı için açık alan seçimi yapın.

## İlişkiler ve JOIN

Müşteri ile asansör arasında birden çoğa ilişki olabilir: Bir müşterinin birden fazla asansörü bulunabilir. Asansör satırında CustomerId, Customers tablosundaki Id'ye işaret eder. Bu yabancı anahtar ilişkisidir. Her asansörde müşterinin bütün adını, adresini ve telefonunu tekrar saklamak güncelleme sorunları yaratabilir.

```sql
SELECT e.Id, e.Code, c.Name AS CustomerName
FROM Elevators AS e
INNER JOIN Customers AS c ON c.Id = e.CustomerId
ORDER BY e.Id;
```

JOIN iki tabloyu ilişki üzerinden birleştirir. INNER JOIN eşleşen satırları getirir. LEFT JOIN, soldaki satır eşleşmese bile onu korumak için kullanılabilir. “Bazı işler listede kayboldu” hatasında JOIN türüne bakmak değerlidir. İsteğe bağlı atanan personeli INNER JOIN ile bağlarsanız atanmamış işler kaybolabilir.

Normalizasyon, aynı gerçeği gereksiz yerlerde tekrar tutmayı azaltma yaklaşımıdır. Her veriyi ayrı tabloya parçalamak da otomatik iyi tasarım değildir. Tarihsel belge üzerinde o andaki müşteri unvanını korumak için kopya alan gerekebilir. “Güncel kayıt” ile “imzalanmış belgenin o anki görüntüsü” farklı iş gereksinimleridir.

## Kısıt ve index

NOT NULL boş değeri engeller. UNIQUE bir alanın veya alan grubunun tekrarını engeller. Foreign key ilişkisiz kaydı engelleyebilir. Uygulamada kontrol yapmak yararlıdır fakat eşzamanlı iki istek yüzünden kontrol ile kayıt arasında yarış olabilir. Veritabanı kısıtı son güvenlik katmanı olabilir.

Index, kitap sonundaki dizine benzer: her sayfayı baştan sona aramak yerine gereken bölüme daha hızlı erişirsiniz. Ancak her ek index yazma sırasında güncellenir ve yer tüketir. Her sütuna index eklemek çözüm değildir. Sık kullanılan filtre/sıralama ile veri dağılımını birlikte düşünün.

Firma işlerini TenantId ve CreatedAt ile listeliyorsanız bileşik index anlamlı olabilir. Sıra önemlidir; `(TenantId, CreatedAt)` ile `(CreatedAt, TenantId)` her sorguda eşdeğer değildir. Sorgu planını incelemeyi öğrenin. Önce bir milyon kayıt simülasyonu yapmadan küçük tabloda hız gördüm diye üretim performansına güvenmeyin.

## Transaction: birlikte olsun ya da hiç olmasın

Bir stok çıkışında miktarı düşürüp hareket kaydını yazmanız gerekir. İlk işlem başarılı, ikinci işlem başarısız olursa stok açıklamasız değişmiş olur. Transaction, ilgili veritabanı işlemlerini tek tutarlılık sınırında toplar.

```csharp
await using var tx = await db.Database.BeginTransactionAsync();
stock.Quantity -= input.Quantity;
db.Movements.Add(new StockMovement
{
    StockItemId = stock.Id,
    Quantity = -input.Quantity
});
await db.SaveChangesAsync();
await tx.CommitAsync();
```

Bu yalnız örnek bir kesittir; miktar sınırı, yetki ve eşzamanlılık ayrıca gerekir. Bir SaveChanges içindeki ilişkili değişiklikler çoğu ilişkisel sağlayıcıda transaction ile korunabilir. Birden fazla SaveChanges, başka servis çağrısı ve dosya yazması bir araya geldiğinde sınırları ayrıca tasarlamalısınız.

Veritabanı transaction'ı gönderilmiş e-postayı geri alamaz. Transaction açıkken kullanıcıya mail yollayıp sonra DB işlemi başarısız olursa gerçek dünya ile kayıt ayrılır. Outbox yaklaşımında gönderilecek iş önce aynı transaction içinde kaydedilir, ayrı süreç bunu kontrollü biçimde gönderir. Bu kavramı bilmiyorsanız en azından “DB rollback oldu, dış dünyadaki her şey de geri döndü” yanılgısından kaçının.

# ORM, Entity Framework ve EF Core

## ORM hangi sorunu çözer?

ORM, Object-Relational Mapping demektir. C# nesneleri ile ilişkisel veritabanı tabloları arasındaki dönüşümü yönetmeye yardımcı olur. SQL yazmayı tamamen ortadan kaldıran bir sihir değildir. Hangi sorgunun üretildiğini, ne kadar veri taşındığını ve hangi kısıtın çalıştığını anlamanız gerekir.

```csharp
var jobs = await db.Jobs
    .Where(x => !x.Completed)
    .OrderBy(x => x.Id)
    .Select(x => new { x.Id, x.Title })
    .Take(20)
    .ToListAsync();
```

Bu LINQ ifadesi, EF Core tarafından desteklenen kısımlarıyla SQL'e çevrilebilir. LINQ yalnız EF'e ait değildir; bellekteki diziler üzerinde de kullanılır. Aynı görünümlü ifade, hangi veri kaynağı üzerinde çalıştığına göre bellekte veya veritabanında yürüyebilir. Kod okurken `.ToList()` çağrısının nerede olduğunu bu yüzden önemseyin.

Entity Framework denildiğinde bazen genel ürün ailesi, bazen klasik EF6 kastedilir. EF Core modern .NET için ayrı geliştirilmiş ORM hattıdır; EF6'nın sadece adı değişmiş sonraki sürümü değildir. DbContext gibi kavramlar benzer olsa da paket, sağlayıcı, davranış ve destek ayrıntıları farklı olabilir. Projenin `.csproj` ve paketlerini okuyarak hangisini kullandığını anlayın.

## DbContext ve DbSet

DbContext, belirli bir çalışma kapsamındaki veritabanı işlemlerini ve değişiklikleri takip eder. DbSet, belirli entity türü için sorgu/yazma giriş noktasıdır. “Entity”, veritabanında kimliği olan model nesnesi diye düşünülebilir.

```csharp
public class StudyDb(DbContextOptions<StudyDb> options)
    : DbContext(options)
{
    public DbSet<StudyJob> Jobs => Set<StudyJob>();
}
```

`DbSet<StudyJob>` tüm işleri o anda belleğe yüklemiş bir liste değildir. Sorgu tanımı oluşturmanıza izin verir. `ToListAsync`, `SingleAsync`, `CountAsync` gibi işlemler yürütmeyi tetikleyebilir. `Where` eklediğiniz her satırda hemen sunucuya gidildiğini varsaymayın.

Entity framework'ün işini doğru görmek için üç ayrı nesneyi düşünün: veritabanındaki satır, context tarafından takip edilen nesne ve API'den döndürdüğünüz DTO. Bazen değerleri aynı görünür ama aynı şey değillerdir. Kullanıcıdan dönen JSON'u doğrudan “veritabanının kendisi” saymak ciddi hatadır.

## Tracking ve AsNoTracking

Tracking açık sorguda EF Core entity'nin başlangıç değerlerini izleyebilir. Nesnenin Title özelliğini değiştirip SaveChanges çağırdığınızda uygun UPDATE üretir. AsNoTracking ise salt okunur sorguda bu izleme yükünü azaltabilir.

```csharp
var job = await db.Jobs.SingleAsync(x => x.Id == id);
job.Title = "Yeni başlık";
await db.SaveChangesAsync();
```

Aynı sorguyu AsNoTracking ile çekip nesnenin özelliğini değiştirmek, kendiliğinden veritabanını güncellemez. Hata ararken önce “Bu nesne takip ediliyor mu?” sorusunu sorun. Sonra “SaveChanges gerçekten çağrıldı mı?” ve “Başarısız oldu mu?” sorularına geçin. Bir nesnenin debugger'da yeni değer göstermesi, diske yazıldığının kanıtı değildir.

Tracking aynı context'te kimliği aynı nesnenin tekrarlanmasını da etkiler. Uzun ömürlü context eski değerleri bellekte tutabilir. Web isteği kapsamındaki kısa ömür, hem kaynak yönetimini hem akıl yürütmeyi kolaylaştırır. Her isteğe yeni context yaklaşımı, her kullanıcıya ayrı veritabanı dosyası oluşturmak anlamına gelmez.

## LINQ sorgusunu yavaşlatan sınır

```csharp
// Öğretici kötü örnek:
var everyJob = await db.Jobs.ToListAsync();
var openJobs = everyJob.Where(x => !x.Completed).Take(20);
```

Burada filtre uygulanmadan bütün tablo belleğe gelmiştir. Elli kayıtla fark etmezsiniz, yüz bin kayıtta ağ, bellek ve yanıt süresi artar. Önce Where/OrderBy/Select/Take, sonra ToListAsync kullanmak çoğu liste sorgusunda daha uygundur.

Bu da sınırsız sıralama ve filtrelerin her zaman ucuz olduğu anlamına gelmez. Doğru index yoksa veritabanı yine çok satır tarayabilir. ORM kodu okunabilir hale getirir; işin maliyetini ortadan kaldırmaz. Gerekli alanları seçmek, sayfalama ve sorgu planını incelemek orta seviye veri erişim becerileridir.

## N+1 problemi

Bir müşteri listesi için bir sorgu, ardından her müşterinin asansörleri için bir sorgu çalışıyorsa 100 müşteri için 101 sorgu oluşabilir. Buna N+1 denir. Kodda küçük bir foreach gibi görünür fakat veritabanına çok sayıda gidiş geliş yaratır.

Çözüm her zaman dev bir Include zinciri değildir. Yalnız sayı gerekiyorsa Count projeksiyonu, yalnız kısa özet gerekiyorsa Select, ilişkiyi gerçekten okumak gerekiyorsa uygun Include veya toplu sorgu düşünülebilir. Çok sayıda Include da gereksiz satır çoğalmasına ve büyük veri taşınmasına neden olabilir. İhtiyacınız olan sonucu önce tarif edin, sonra sorguyu seçin.

Hata avı için EF günlüklerini geliştirme ortamında okuyun. Tek sayfa açılışında benzer SELECT sorguları onlarca kez tekrar ediyorsa N+1 şüphesi doğar. Sensitive data logging gibi seçenekleri gerçek kişisel veriyle gelişigüzel açmayın. Sorgu biçimini görmek ile kullanıcı verisini günlüğe dökmek farklıdır.

# Elle kurulacak mini API: kalıcı iş listesi

Bu laboratuvar, önceki kavramları birleştiren bağımsız bir projedir. Gerçek bir uygulama deposunun içinde değiştirilmesi gereken bir dosya yoktur. Proje tek kullanıcı için tasarlanmış yerel öğrenme uygulamasıdır; kimlik doğrulaması yoktur. İnternete açmayın, gerçek müşteri verisi girmeyin. Firma izolasyonunu ayrı bölümde tartışacağız. Bu sınırı özellikle belirtiyoruz: basit örneğin çalışması, üretim güvenliğine hazır olduğu anlamına gelmez.

## Adım 1: proje ve paketleri kur

PowerShell'de kendi öğrenme klasörünüzü seçin. Aşağıdaki komutlar yeni bir StudyApi klasörü oluşturur. Aynı isimli bir klasörünüz zaten varsa başka isim seçin; içeriğinin üzerine gelişigüzel yazmayın.

```powershell
Set-Location C:\KodAtolyesi
dotnet new web -n StudyApi -f net10.0
Set-Location StudyApi
dotnet add package Microsoft.EntityFrameworkCore.Sqlite --version "10.0.*"
dotnet add package Microsoft.EntityFrameworkCore.Design --version "10.0.*"
dotnet new tool-manifest
dotnet tool install dotnet-ef --version "10.0.*"
```

Burada 10.0.* aynı major/minor ailesindeki kullanılabilir yama sürümünü seçmek içindir. İlk restore sonrasında hangi sürümlerin çözüldüğünü inceleyin; EF Core sağlayıcı, Design ve dotnet-ef aracını uyumlu tutun. Paket sürümü ile .NET SDK sürümü aynı kavram değildir. Gerçek projede seçtiğiniz kesin sürümleri ve lock dosyasını gözden geçirerek sabitleyin; kontrolsüz kayan sürümleri dağıtımın tek tarifi yapmayın.

Bu kitabın kod derleme kontrolünde eski 10.0.0 paketiyle transitive SQLite bileşeni için NU1903 güvenlik uyarısı görüldü. Bu nedenle ilk sürümü körlemesine kopyalamak yerine güncel yama ve bağımlılık denetimi önemlidir. `dotnet list package --include-transitive --vulnerable` ile raporu okuyun. Yeni yama seçmek bütün transitif açıkların kendiliğinden kapandığı garantisi değildir; yüksek önem dereceli uyarıyı bastırmadan ilgili duyuru ve uyumlu düzeltmeyi inceleyin. Laboratuvar yalnız sentetik yerel veri içindir; güvenlik uyarılı paketi üretime taşımayın.

`dotnet new web`, boş ASP.NET Core başlangıcı oluşturur. Bu örnekte controller klasörü veya `[ApiController]` kullanmıyoruz; Minimal API ile çalışacağız. Başka eğitimde `dotnet new webapi` veya controller şablonu görmeniz mümkündür. Farklı şablonların dosyalarını rastgele karıştırmayın. `StudyApi.csproj` içindeki hedef `net10.0` olmalıdır.

## Adım 2: model ve context

Proje kökünde `StudyDb.cs` oluşturup tamamını yazın:

```csharp
using Microsoft.EntityFrameworkCore;

public class StudyJob
{
    public int Id { get; set; }
    public string Title { get; set; } = "";
    public bool Completed { get; set; }
    public int Version { get; set; } = 1;
}

public class StudyDb(DbContextOptions<StudyDb> options)
    : DbContext(options)
{
    public DbSet<StudyJob> Jobs => Set<StudyJob>();

    protected override void OnModelCreating(ModelBuilder model)
    {
        model.Entity<StudyJob>().Property(x => x.Title)
            .HasMaxLength(200);
        model.Entity<StudyJob>().Property(x => x.Version)
            .IsConcurrencyToken();
    }
}

public record CreateJobInput(string? Title);
public record UpdateJobInput(
    string? Title, bool Completed, int Version);
```

Version alanını birazdan çakışma yakalamak için kullanacağız. HasMaxLength, EF modelinin bir kısıtını ifade eder; SQLite'ın tür sistemi nedeniyle her model sınırının veritabanında beklediğiniz sert sınırla uygulanacağını varsaymayın. Endpoint'te başlık uzunluğunu ayrıca kontrol edeceğiz. API doğrulaması kullanıcıya doğru hata verir; DB kısıtları ise veri tutarlılığı için başka bir katmandır.

## Adım 3: endpoint'leri yaz

`Program.cs` içeriğini tamamen aşağıdaki kodla değiştirin. Bu, kendi yeni StudyApi projeniz içindir; gerçek uygulama dosyasını değiştirmiyoruz.

```csharp
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);
var path = builder.Configuration["DatabasePath"] ?? "study.db";
var fullPath = Path.GetFullPath(path);
Directory.CreateDirectory(Path.GetDirectoryName(fullPath)!);

builder.Services.AddDbContext<StudyDb>(options =>
    options.UseSqlite($"Data Source={fullPath}"));

var app = builder.Build();

if (args.Contains("--migrate"))
{
    using var scope = app.Services.CreateScope();
    var db = scope.ServiceProvider.GetRequiredService<StudyDb>();
    await db.Database.MigrateAsync();
    return;
}

app.MapGet("/health", () => Results.Ok(new { status = "ok" }));

app.MapGet("/api/jobs", async (StudyDb db, CancellationToken ct) =>
{
    var rows = await db.Jobs.AsNoTracking()
        .OrderBy(x => x.Id)
        .Take(100)
        .Select(x => new
        {
            x.Id, x.Title, x.Completed, x.Version
        })
        .ToListAsync(ct);
    return Results.Ok(rows);
});

app.MapGet("/api/jobs/{id:int}", async (
    int id, StudyDb db, CancellationToken ct) =>
{
    var row = await db.Jobs.AsNoTracking()
        .SingleOrDefaultAsync(x => x.Id == id, ct);
    return row is null
        ? Results.NotFound()
        : Results.Ok(row);
});

app.MapPost("/api/jobs", async (
    CreateJobInput input, StudyDb db, CancellationToken ct) =>
{
    var title = input.Title?.Trim();
    if (string.IsNullOrEmpty(title) || title.Length > 200)
    {
        return Results.BadRequest(new
        {
            error = "Başlık 1-200 karakter olmalı."
        });
    }

    var job = new StudyJob { Title = title };
    db.Jobs.Add(job);
    await db.SaveChangesAsync(ct);
    return Results.Created($"/api/jobs/{job.Id}", job);
});

app.MapPut("/api/jobs/{id:int}", async (
    int id, UpdateJobInput input, StudyDb db, CancellationToken ct) =>
{
    var title = input.Title?.Trim();
    if (string.IsNullOrEmpty(title) || title.Length > 200)
    {
        return Results.BadRequest(new
        {
            error = "Başlık 1-200 karakter olmalı."
        });
    }

    var job = await db.Jobs.SingleOrDefaultAsync(x => x.Id == id, ct);
    if (job is null) return Results.NotFound();
    if (job.Version != input.Version)
    {
        return Results.Conflict(new
        {
            error = "İş değişmiş. Yenileyip tekrar deneyin."
        });
    }

    job.Title = title;
    job.Completed = input.Completed;
    job.Version++;
    try
    {
        await db.SaveChangesAsync(ct);
    }
    catch (DbUpdateConcurrencyException)
    {
        return Results.Conflict(new
        {
            error = "Başka işlem işi değiştirdi. Yenileyin."
        });
    }

    return Results.Ok(job);
});

app.Run();
```

İlk okumada her satırı ezberlemeye çalışmayın. Önce dört endpoint'i bulun. Sonra her birinde kullanıcı girdisi, veritabanı okuma/yazma ve yanıt satırını farklı renkle işaretleyin. Bir POST isteğinin `Title` değerinin nereden girip nereye yazıldığını parmağınızla takip edin. Kod okuma, metne bakmak değil veri akışını izlemektir.

## Adım 4: şemayı kur ve uygulamayı başlat

```powershell
dotnet build
dotnet ef migrations add InitialJobs
dotnet ef database update
dotnet run --urls http://127.0.0.1:5311
```

Derleme sıfır hata ile tamamlanmalıdır. Migration komutu Migrations klasörü üretir. Database update, yerel study.db üzerinde gerekli tabloyu oluşturur. Son komut sunucuyu başlatır; bu terminal açıkken ikinci PowerShell penceresinde istek gönderebilirsiniz. Durdurmak için yalnız bu öğrenme terminalinde Ctrl+C kullanın. Başka uygulamanın sürecini durdurmayın.

```powershell
Invoke-RestMethod http://127.0.0.1:5311/health

$body = @{ title = "Örnek asansör kapı kontrolü" } |
    ConvertTo-Json
Invoke-RestMethod http://127.0.0.1:5311/api/jobs `
    -Method Post -ContentType application/json -Body $body

Invoke-RestMethod http://127.0.0.1:5311/api/jobs
```

İlk yanıtın status değeri ok olmalıdır. POST yanıtında Id, Title, Completed=false ve Version=1 alanlarını görürsünüz. Kimlik değeri önceki denemelere göre değişebilir; her zaman 1 olacağını varsaymayın. Listede eklediğiniz başlık bulunmalıdır. Sunucuyu durdurup yeniden başlattığınızda kayıt hâlâ varsa kalıcı veritabanı kullanımını gözlemlemiş olursunuz.

## Adım 5: güncelle ve çakışmayı gözle

Önce listeden gerçek kimlik ve sürümü okuyun. Aşağıdaki örnekte id=1 ve version=1 varsayılmıştır; kendi çıktınıza göre değiştirin.

```powershell
$body = @{
    title = "Kapı kontrolü tamamlandı"
    completed = $true
    version = 1
} | ConvertTo-Json

Invoke-RestMethod http://127.0.0.1:5311/api/jobs/1 `
    -Method Put -ContentType application/json -Body $body
```

Yanıtta Version=2 görmelisiniz. Aynı eski gövdeyi tekrar gönderin. Bu kez 409 beklenir. PowerShell hata nesnesi gösterebilir; tarayıcı Network paneli veya başka HTTP istemcisiyle yanıt gövdesini de inceleyebilirsiniz. Sunucu çökmedi; eski sürümle yapılan güncellemeyi bilinçli reddetti.

Burada iki koruma vardır. Baştaki Version karşılaştırması istemcinin zaten eski kaldığını yakalar. IsConcurrencyToken ve exception yakalama ise okuma ile yazma arasındaki kısa zamanda başka istek değişiklik yaparsa çakışmayı yakalar. Yalnız ilk if kontrolü yarış durumunu tamamen kapatmaz.

## Adım 6: yanlış girdiyi bilerek gönder

```powershell
$bad = @{ title = "   " } | ConvertTo-Json
Invoke-RestMethod http://127.0.0.1:5311/api/jobs `
    -Method Post -ContentType application/json -Body $bad
```

400 beklenir. Şimdi 201 karakterlik başlık gönderin. Yine 400 beklenir. Sonra olmayan bir Id okuyun, 404 bekleyin. Bu küçük testler “mutlu yol” dışında davranışı düşünmenizi sağlar. İyi geliştirici yalnız doğru formun çalışmasını değil, yanlış isteklerin güvenli ve anlaşılır reddedilmesini de tasarlar.

# Migration ve snapshot: kod ile şema birlikte yürür

## Model değişince veritabanı kendiliğinden değişmez

C# sınıfına bir Description özelliği eklediğinizde derleme başarılı olabilir. Fakat mevcut SQLite tablosunda Description sütunu bulunmayabilir. Kod modeli ile veritabanı şeması iki farklı yerde yaşar. Migration, bu ikisini sürümlü biçimde eşleştirmenin aracıdır.

StudyJob'a şu alanı ekleyin:

```csharp
public string Description { get; set; } = "";
```

Ardından:

```powershell
dotnet ef migrations add AddJobDescription
dotnet ef migrations list
dotnet ef migrations script
dotnet ef database update
```

Migration dosyasında ne eklendiğini okuyun. Henüz gerçek veritabanına uygulamadan üretilen SQL'i anlamaya çalışın. Özellikle kolon silme, tip değiştirme ve yeniden adlandırmada otomatik çıkarımı gözle kontrol edin. Bir alanı yeniden adlandırdığınızda araç her zaman iş niyetinizi bilmez; yanlışlıkla eski sütunu silip yeni sütun ekleyen migration veri kaybına yol açabilir.

## Snapshot ne işe yarar?

Model snapshot, EF Core'un mevcut modelin önceki bilinen yapısını kod olarak tutmasına yardım eder. Yeni migration oluşturulurken güncel model ile bu görünüm karşılaştırılır. Snapshot veritabanı yedeği değildir. İçinde müşterilerin kayıtları bulunmaz. Snapshot'ı kopyalayarak kayıp veriyi geri getiremezsiniz.

Migration dosyası bir değişiklik adımıdır; snapshot son model görünümüdür; canlı veritabanı ise gerçek şema ve veriyi taşır. Üçünü ayırmak hataları daha hızlı çözmenizi sağlar. “Dosyada sütun var” ile “üretim DB'sinde sütun var” aynı kanıt değildir. “CI yükseltme testi geçti” ile “canlı migration tamamlandı” da ayrı durumlardır.

## Uygulanmış migration'ı değiştirme tehlikesi

Bir migration başka ortamda uygulanmışsa dosyasını geriye dönük değiştirmek ortamların aynı isim altında farklı şemalara sahip olmasına neden olabilir. Genellikle yeni düzeltme migration'ı eklenir. Henüz yalnız sizin yeni öğrenme veritabanınızda bulunan, paylaşılmamış migration için geri alma/yeniden üretme öğrenilebilir; fakat bu akışı canlı veriye taşıyacak otomatik refleks geliştirmeyin.

Geri alma bazen veri kaybeder. Eklediğiniz sütunu kaldıran Down metodu o sütundaki gerçek bilgiyi silebilir. “Rollback komutu var” güvenli geri dönüş planı olduğu anlamına gelmez. Önce yedek, geri yükleme denemesi, uygulama uyumu ve işlem süresi düşünülmelidir. Finans ve stok geçmişi gibi verilerde geri alma yerine ileri düzeltme gerekebilir.

## Yükseltme testi nasıl düşünülür?

Boş DB üzerinde son şemayı kurmak yalnız bir senaryodur. Gerçek kullanıcı eski şema ve verilerle yükselir. İyi bir yükseltme testi eski migration'a kadar bir sentetik DB kurar, örnek kayıt ekler, yeni migration'ları uygular ve kaydın anlamının korunduğunu doğrular. Yeni sütunun doğru varsayılanı, index ve kısıtların varlığı da kontrol edilir.

Örneğin eski işi tamamlanmış olarak kaydettiyseniz yükseltmeden sonra Completed değerinin false'a dönmemesini beklersiniz. Bir yeni alanın varsayılanının yanlış olması derlemeyle yakalanmaz. Model ve migration arasındaki farkı okuma, veritabanı kullanan geliştiricinin temel becerisidir.

# Veri doğruluğu: eşzamanlılık, tekrar istek ve firma sınırı

## Çift tıklama ile yarış aynı şey değildir

Kullanıcı kaydet düğmesine iki kez basabilir. Ağ kopunca istemci aynı isteği tekrar yollayabilir. Proxy zaman aşımından sonra önceki isteğin sunucuda tamamlanıp tamamlanmadığını istemci bilmeyebilir. Düğmeyi devre dışı bırakmak yararlıdır ama bu sorunları tek başına çözmez.

Idempotency, aynı iş niyeti tekrar ulaştığında işlemin bir kez etkili olmasını hedefler. Örneğin stok çıkışına requestId verilir; sunucu aynı firma ve işlem kimliğiyle daha önce tamamlanan işi tanır. DB'de UNIQUE(TenantId, RequestId) gibi bir koruma, iki eşzamanlı isteğin ikisinin de “daha önce yok” kontrolünü geçmesini engelleyebilir.

RequestId ile Version farklı şeydir. RequestId aynı niyetin tekrarını ayırt eder. Version, kullanıcının hangi kayıt durumuna göre değişiklik yaptığını belirtir. Bir finans veya stok işleminde ikisi birden gerekebilir. Rastgele her retry'da yeni requestId üretmek tekrar korumasını bozar; aynı niyetin tekrarında aynı kimlik korunmalıdır.

## Çok firmalı uygulamada tenant

Tenant, aynı uygulamada birbirinden ayrılmış müşteri/kurum alanıdır. Bir bakım uygulamasında her firma bir tenant olarak düşünülebilir. Aynı kod ve DB birden fazla firmaya hizmet verebilir; bu, firmaların birbirinin müşterisini görmesi gerektiği anlamına gelmez.

Şu tasarım güvenli değildir:

```csharp
// Kötü fikir: firma seçimini gövdedeki değere bırakmak.
public record CreateInput(Guid TenantId, string Title);
```

İstemci başka TenantId yazarak başka firma adına kayıt oluşturabilir. Sunucu, firmanın kimliğini doğrulanmış oturumdan veya açıkça tanımlanmış, yetkilendirilmiş platform işleminden çıkarmalıdır. İstemci tarafından gönderilen değer bir “kimlik iddiası”dır; kanıt değildir.

## Query filter okuma için yardımcıdır, bütün güvenlik değildir

```csharp
// Kavramsal kesit; doğrulanmış oturum altyapısı gerektirir.
model.Entity<Job>().HasQueryFilter(x =>
    x.TenantId == tenantContext.Id);
```

Bu filtre normal sorgulara firma koşulu eklenmesini kolaylaştırır. Ancak yazma denetimini kendiliğinden tamamlamaz. Yeni entity'nin TenantId'si kimden alınıyor? Mevcut bir nesnenin TenantId'si değiştirilebiliyor mu? IgnoreQueryFilters kullanan platform raporu yalnız izinli alanları mı okuyor? Raw SQL veya toplu güncelleme merkezi korumayı atlıyor mu? Bunlar ayrıca cevaplanmalıdır.

Global filtreyi kaldıran satır gördüğünüzde otomatik olarak her kullanımın saldırı olduğunu söylemeyin; platform sayımları gibi haklı ihtiyaç olabilir. Fakat açık yetki, minimum veri projeksiyonu ve firma sınırı kanıtı arayın. Normal firma endpoint'inde “kolay olsun” diye filtre kaldırmak kırmızı bayraktır.

## İki firmalı test zorunluluğu

Yalnız Firma A'nın kendi işini görmesini test ederseniz izolasyon konusunda eksik kanıt üretirsiniz. A ve B adında iki sentetik firma kurun. Her birine ayırt edilebilir müşteri ve iş ekleyin. A oturumuyla B'nin liste, tek kayıt, güncelleme, silme, dışa aktarma ve dosya bağlantılarını deneyin. B'nin kaydı değişmemeli; uygun ret yanıtı dönmelidir.

Bir endpoint yalnız toplu sayım döndürse bile ilişki üzerinden veri sızabilir. Başlıklar kapalıyken müşteri telefonu yanıtın başka bir alanında bulunabilir. JSON yanıtını gerçek alan listesiyle inceleyin. Yetki testi tek düğmenin görünmediğini kontrol eden tarayıcı testiyle sınırlanamaz.

# Temel uygulama güvenliği

## Güvenlik bir özellik kutucuğu değildir

HTTPS kullanmak gereklidir fakat yanlış yetkili endpoint'i düzeltmez. ORM kullanmak bazı SQL injection risklerini azaltabilir fakat kullanıcının gönderdiği başlığı innerHTML ile basarsanız XSS riski sürer. Güçlü şifre, çalınmış oturumun her koşulda güvenli olduğu anlamına gelmez. Katmanları ayrı düşünün.

Kimlik, yetki ve veri sınırından sonra girdi doğrulaması, çıktı kodlama, CSRF, hız sınırı, günlüklerde sırların korunması ve bağımlılık güncellemeleri gelir. Hepsini ilk hafta kusursuz tasarlayamazsınız; ama hangi sorumluluğu hazır çerçevenin sağladığını, hangisinin sizin iş kodunuzda kaldığını öğrenmelisiniz.

## SQL injection, XSS, CSRF farkı

SQL injection, saldırgan girdisinin veritabanı komutunun yapısına karışmasıdır. Parametreli sorgu kullanılır; metin birleştirerek sorgu oluşturulmaz. XSS, güvenilmeyen içeriğin tarayıcıda kod olarak çalışmasıdır. Kullanıcı metnini çoğu durumda textContent ile gösterirsiniz; bilinçli HTML gerekiyorsa uygun temizleme ve dar izin modeli gerekir.

CSRF, kullanıcının tarayıcıda taşıdığı oturumla başka sayfanın istenmeyen işlem yaptırmaya çalışmasıdır. Cookie tabanlı yazma işlemlerinde framework'ün antiforgery mekanizması ve doğru cookie ayarları kullanılır. CORS ile CSRF aynı şey değildir. CORS tarayıcının origin'ler arası erişim kurallarını etkiler; sunucuyu genel bir yetki duvarına dönüştürmez. curl veya başka bir sunucu CORS sınırını tarayıcı gibi uygulamak zorunda değildir.

## Sır yönetimi

Veritabanı şifresi, e-posta anahtarı, oturum şifreleme anahtarı ve özel sertifika sırdır. Bunları Git'e koymayın. `.gitignore` dosyası, daha önce commit edilmiş sırrı geçmişten silmez. Yanlışlıkla sızmış anahtar için yalnız dosyayı kaldırmak değil, anahtarı iptal/değiştirmek gerekir.

Yerel geliştirmede user-secrets gibi araçlar kullanılabilir. User-secrets bütün tehditlere karşı şifreli kasa garantisi değildir; kaynak kodundan ayrı tutma kolaylığı sağlar. Üretimde ortamın desteklediği secret yönetimini ve erişim kısıtlarını kullanın. Ortam değişkenleri de log veya süreç incelemesi üzerinden sızabilir; “env'de duruyor, görünmez” sanmayın.

Log'a isteğin tamamını basmak caziptir. Ancak parolalar, reset token'ları ve kişisel veriler loglara kalıcı girebilir. Gereken alanları seçin. Sahte test verisiyle örnek üretin. Bir hata raporunu başka kişiye gönderirken sırrı maskeleyin; hata ayıklama, veri sızdırma bahanesi değildir.

## Rate limit ve brute force

Rate limit, bir zaman aralığında istek sayısını sınırlar. Amaç yalnız performans değildir; giriş denemesi, token tahmini ve pahalı sorgulara karşı koruma sağlayabilir. Limitin anahtarı önemlidir: IP, kullanıcı, firma veya bunların birleşimi farklı etkiler doğurur. Aynı ofisten gelen bütün çalışanların tek IP'yi paylaşabileceğini düşünün.

Bir testin 429 alması her zaman ürün hatası değildir; test aynı IP'den çok sayıda giriş denemesi yapmış olabilir. Ancak testi geçsin diye gerçek güvenlik sınırını kalıcı yükseltmek yanlış düzeltmedir. Test izolasyonu, sentetik ortam ayarları ve gerçek kabul sınırları ayrı tutulmalıdır.

# Docker: uygulamayı paketlemek ve ortamı anlamak

## Docker'ı hangi sorun için kullanırız?

“Bende çalışıyor” cümlesi genellikle ortam farkını saklar. Bir bilgisayarda doğru runtime, başka bilgisayarda farklı bağımlılık veya dosya yolu bulunabilir. Container yaklaşımı uygulamanın kullanıcı alanındaki dosyalarını ve çalıştırma tarifini daha taşınabilir bir paket haline getirir. Bu, donanım ve işletim sistemi farklarının tamamını sihirle yok etmez.

Image, uygulama ve gereken dosyaları içeren katmanlı pakettir. Container, bu image'dan başlatılan çalışan örnektir. Aynı image'dan iki container çalıştırabilirsiniz. Image genellikle değişmez kabul edilir; çalışan container'ın yazılabilir katmanı ayrı yaşar. Program dosyaları ile kalıcı müşteri verisi bu nedenle aynı yerde yönetilmemelidir.

Docker Desktop, Windows'ta Docker araçları ve ilgili sanallaştırma altyapısını kullanmayı kolaylaştıran masaüstü ürünüdür. Docker Engine işleri çalıştıran motordur. `docker` komutu ise motora istek gönderen istemcidir. İstemci kurulu ama motor kapalı olabilir. `docker --version` yalnız istemcinin sürümünü gösterebilir; motorun çalıştığını kanıtlamaz.

```powershell
docker --version
docker version
docker info
docker compose version
```

İlk komut çalışıp diğerleri bağlantı hatası veriyorsa hemen reset veya yeniden kurulum yapmayın. Docker Desktop açık mı? Motor hazır mı? Doğru context seçili mi? WSL/sanallaştırma altyapısı hazır mı? Hata metnini okuyun. Kullanılan context'i görmek için `docker context ls` yararlıdır. Context değiştirmek başka motora bağlanmanıza neden olabilir; öncesinde nereye baktığınızı anlayın.

## Container ile sanal makine farklıdır

Sanal makine genellikle kendi konuk işletim sistemi çekirdeğiyle çalışır. Container ise işletim sistemi seviyesinde izolasyon kullanır; Linux container'ları uygun Linux çekirdeğine ihtiyaç duyar. Windows Docker Desktop'ın Linux container çalıştırırken Linux sanallaştırma altyapısı kullanması bu farkla ilgilidir.

Container bir güvenlik sınırı sağlar fakat “içindeki her şey zararsız” anlamına gelmez. Host klasörünü yazılabilir bağlarsanız container o alana yazabilir. Docker socket erişimi çok güçlüdür. Bilmediğiniz image'ı canlı veri volume'uyla başlatmayın. Öğrenme denemelerinde boş/sentetik volume ve dar port yayını kullanın.

## Port eşleme

Bir container içindeki uygulama 8080 dinleyebilir. Bilgisayarınızdan 5311 ile erişmek için port eşlemesi yapılır. `5311:8080` dışarıdaki port ile içerideki portu eşler; iki uygulamanın aynı olduğunu söylemez.

```text
127.0.0.1:5311:8080
```

Bu biçimde yalnız yerel loopback arayüzüne yayın yaparız. Öğrenme uygulamasının ağdaki bütün cihazlara açık olması gerekmez. `0.0.0.0` dinleme bağlamına göre tüm arayüzleri ifade eder; tarayıcıda ziyaret etmek için kullanılan gerçek hedef adresi değildir. Container içindeki `localhost`, host bilgisayar değil o container'ın kendisidir. Bir başka container'a servis adıyla ulaşılır.

## Volume, bind mount ve verinin ömrü

Container silindiğinde onun yazılabilir katmanındaki veriler de kaybolabilir. Volume, veriyi container yaşam döngüsünden ayrı yönetmek için kullanılır. Bind mount ise host'taki belirli klasörü container içine bağlar. İkisi de veritabanını yanlış işlemden veya saldırıdan otomatik korumaz.

Image oluşturmak DB yedeği almak değildir. Image içinde uygulamanın kodu vardır; çalışan volume'daki güncel müşteri kayıtları ayrı yerde durur. Volume varken ayrıca geri yüklenebilir yedek gerekir. Bir dosyanın bulunması onun tutarlı, şifresi açılabilir veya güncel olduğunu kanıtlamaz.

Öğrenirken `docker compose down` ile `docker compose down -v` arasındaki farkı özellikle bilin. `-v`, ilgili volume'ları kaldırabilir ve kalıcı veriyi silebilir. Bu kitap normal durdurma akışında `-v` kullanmaz. Benzer biçimde gelişigüzel prune komutlarıyla yer açmaya çalışmayın. Önce hangi nesnenin hangi projeye ait olduğunu listeleyin.

# Dockerfile ve Compose laboratuvarı

## Çok aşamalı Dockerfile

StudyApi kökünde `Dockerfile` oluşturun. Önceki migration dosyalarının mevcut olması gerekir. Aşağıdaki paketleme öğretim örneğidir; üretim için non-root kullanıcı, yalnız okunur kök dosya sistemi, kaynak limitleri ve diğer sertleştirme kararları ayrıca tamamlanmalıdır.

```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /src
COPY StudyApi.csproj ./
RUN dotnet restore
COPY . ./
RUN dotnet publish -c Release -o /out --no-restore

FROM mcr.microsoft.com/dotnet/aspnet:10.0
WORKDIR /app
COPY --from=build /out ./
ENV ASPNETCORE_URLS=http://0.0.0.0:8080
ENV DatabasePath=/data/study.db
EXPOSE 8080
ENTRYPOINT ["dotnet", "StudyApi.dll"]
```

İlk aşamada SDK ile derleme yapılır. Son aşamaya SDK'nın tamamını taşımak yerine yayın çıktısı kopyalanır. Bu, runtime image'ının daha küçük olmasına yardım eder. EXPOSE bir portu kendiliğinden host'a açmaz; belgelendirme/metadata görevi görür. Gerçek yayın Compose ports veya docker run parametresiyle belirlenir.

`.dockerignore` dosyası da ekleyin:

```text
bin/
obj/
.git/
*.db
*.db-shm
*.db-wal
.env
secrets/
```

COPY noktası build context içeriğini alır. Sır veya gerçek veritabanını yanlışlıkla image katmanına sokmamak için context ve ignore dosyaları önemlidir. Son aşamada dosyayı silmek, önceki image katmanına girmiş sırrı güvenli biçimde yok etmiş olmayabilir. Sırları en baştan build context dışında tutun.

## Compose: birden fazla parçanın tarifi

`compose.yaml` dosyası:

```yaml
services:
  api:
    build: .
    image: study-api:local
    ports:
      - "127.0.0.1:5311:8080"
    volumes:
      - study-data:/data
    environment:
      DatabasePath: /data/study.db
    restart: "no"

volumes:
  study-data:
```

Bu dosyayı okurken önce api servisini bulun. Image yerel bir etiketle adlandırılır. Volume, container içindeki `/data` dizinine bağlanır. Veritabanı yolu da o dizinin içindedir. Eğer DB yolunu `/app/study.db` yaparsanız volume var olsa bile DB volume'a yazılmıyor olabilir. “Compose'da volume yazdım, verim kalıcıdır” varsayımı bu yüzden yetersizdir.

```powershell
docker compose config
docker compose build
docker compose run --rm api --migrate
docker compose up -d
docker compose ps
docker compose logs --tail 50 api
```

Config, birleştirilmiş yapılandırmayı kontrol etmenize yardım eder. Build image'ı hazırlar. Run komutu aynı volume üzerinde tek seferlik migration modunu çalıştırır; kodumuz `--migrate` görünce şemayı uygular ve çıkar. Up servisi başlatır. Ps durumunu, logs uygulama çıktısını gösterir. Bu komutlar yalnız yeni StudyApi Compose projesine aittir; başka dizindeki gerçek uygulamaya uygulamayın.

Yerel dotnet sunucusu hâlâ 5311'de çalışıyorsa Compose portu alamaz. Aynı portta iki dinleyici beklemeyin. Ya kendi öğrenme dotnet sürecinizi Ctrl+C ile durdurun ya da Compose'un host portunu boş bir başka porta değiştirin. Hata ayıklarken başka uygulamayı öldürmek yerine çakışmanın sahibini belirleyin.

```powershell
Invoke-RestMethod http://127.0.0.1:5311/health
docker compose stop
docker compose start
docker compose down
```

Stop durdurur, start mevcut container'ı başlatır, down bu Compose projesinin container/ağ düzenini kaldırır. Burada `-v` yoktur; öğrenme verisinin volume'u tutulur. Yeniden up yaptığınızda veriyi kontrol edin. Gerçek yedekleme yine ayrı görevdir.

## Image etiketi ve digest

`study-api:local` etiketi istediğinizde başka bir image'ı gösterebilir. Tag okunabilir isimdir; aynı isimle yeni image üretilebilir. Digest içerik temelli kimlik sağlar. Üretimde “hangi dosya gerçekten çalışıyor?” sorusuna yalnız latest etiketiyle cevap vermek zorlaşır. Sürüm, commit SHA, image kimliği ve ortamı izlenebilir tutun.

Bir PR'ın birleşmesi image'ın üretildiğini, image'ın üretilmesi sunucuya dağıtıldığını, dağıtım da kullanıcı kabulünü kanıtlamaz. Teslim raporunda bu aşamaları ayrı yazmak mühendislik disiplinidir. “Bitti” kelimesinin hangi aşamayı anlattığını somutlaştırın.

# Caddy: uygulamanın önündeki web sunucusu

## Reverse proxy ne yapar?

Reverse proxy, istemciden gelen isteği uygun arka uç servisine iletir ve yanıtı geri taşır. Kullanıcı doğrudan Kestrel'in yerel portunu bilmek zorunda kalmaz. TLS sonlandırma, alan adına göre yönlendirme ve statik içerik sunma gibi görevler bu katmanda olabilir.

Caddy bir web sunucusu ve reverse proxy'dir. Docker ile aynı şey değildir. Caddy'yi host'ta veya container içinde çalıştırabilirsiniz. Docker uygulamayı çalıştırma/paketleme katmanında, Caddy HTTP trafiğinin ön yüzünde görev alır. Caddy'nin kurulmuş olması, uygulama motorunun ya da Docker'ın da çalıştığını göstermez.

## Ücretsiz yerel HTTP denemesi

Önce yerel dotnet uygulamasını 5311'de çalıştırın. Caddy kuruluysa aynı öğrenme klasöründe şu `Caddyfile` dosyasını oluşturun:

```caddyfile
http://127.0.0.1:5312 {
    reverse_proxy 127.0.0.1:5311
}
```

```powershell
caddy validate --config Caddyfile --adapter caddyfile
caddy run --config Caddyfile --adapter caddyfile
```

İkinci terminalden `http://127.0.0.1:5312/health` isteği gönderin. İstek önce Caddy'ye, sonra 5311'deki uygulamaya gider. Bu özel yerel örnekte HTTP şemasını açık yazdık; sertifika üretme veya tarayıcı güven deposu değiştirme adımı yoktur. Gerçek internette şifre taşıyan uygulamayı düz HTTP ile yayınlamak için örnek alınmamalıdır.

TLS, tarayıcı ile sunucu arasındaki bağlantıyı şifreler ve sunucu kimliğinin doğrulanmasına yardım eder. Caddy uygun alan adı ve erişim koşullarında otomatik HTTPS yönetebilir. Bunun çalışması DNS, port erişimi, sertifika sağlayıcısı ve ortam koşullarına bağlıdır. “Caddyfile'a ad yazdım, her ağda otomatik olur” diye düşünmeyin.

## Container içindeki adres tuzağı

Caddy ayrı bir container'daysa `reverse_proxy localhost:5311` çoğunlukla yanlış hedef olur. localhost Caddy container'ını gösterir. Aynı Compose ağına bağlı api servisine örneğin `reverse_proxy api:8080` ile gidilebilir. Host'a yayınlanan 5311 portunu container'lar arasında kullanmak zorunlu değildir.

502 Bad Gateway gördüğünüzde hemen uygulama kodunu değiştirmeyin. Proxy hedef adı doğru mu? Uygulama içeride hangi portu dinliyor? İki servis aynı ağa bağlı mı? Uygulama başlamış mı? HTTP hedefe yanlışlıkla HTTPS mi deniyorsunuz? Önce bu bağlantı zincirini test edin.

Reverse proxy'nin ilettiği başlıklar da güvenlik konusudur. Uygulama, X-Forwarded-For gibi başlıklara yalnız güvendiği proxy sınırında güvenmelidir. Her istemcinin yazdığı forwarded bilgisini doğru kabul etmek IP temelli hız sınırını veya bağlantı bilgilerini yanıltabilir. Caddy kullanmak bu uygulama ayarını kendiliğinden tamamlamaz.

# CI/CD ve GitHub Actions

## CI neyi kanıtlar?

Continuous Integration, değişikliklerin belirli otomatik kontrollerden düzenli geçmesidir. Bir PR açıldığında restore, build, test ve paketleme adımlarını çalıştırabilirsiniz. CI yeşilse yalnız tanımlı kontrollerin o koşuda geçtiğini bilirsiniz. Test yazılmamış güvenlik açığı veya yanlış iş kuralı kendiliğinden bulunmuş olmaz.

Continuous Delivery, değişikliği dağıtılabilir durumda tutma pratiğidir. Continuous Deployment ise belirli koşullar sağlandığında dağıtımın otomatik yapılmasını anlatır. Her projede aynı onay ve yayın modeli yoktur. Öğrenme projesinde otomatik production deploy kurmak zorunda değilsiniz; önce test ve artefakt üretimini anlamak daha iyidir.

GitHub Actions workflow dosyası depodaki `.github/workflows` altında YAML biçiminde tutulur. Event ne zaman başlayacağını, jobs yapılacak iş gruplarını, steps adımları belirler. Runner bu adımların çalıştığı makinedir. Kendi bilgisayarınız ile GitHub runner aynı dosyalara veya kurulu araçlara sahip olmayabilir.

## Basit bir build workflow'u

StudyApi için `.github/workflows/build.yml` örneği:

```yaml
name: Build study API
on:
  push:
  pull_request:
permissions:
  contents: read
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
        with:
          dotnet-version: "10.0.x"
      - run: dotnet restore
      - run: dotnet build -c Release --no-restore
```

Bu dosya yalnız derler; test çalıştırdığını iddia etmiyoruz. Test projesi eklediğinizde ayrıca dotnet test adımı gerekir. Action major etiketleri yerine güvenlik politikası gerektiriyorsa doğrulanmış tam commit SHA ile sabitleme yapılabilir. Kitaptaki örnek ana fikri öğretir; kuruluşunuzun tedarik zinciri politikasını yerine koymaz.

Bir workflow'u okurken yalnız yeşil simgeye bakmayın. Doğru branch ve SHA mı? Test komutu filtreyle beklenen testleri bulmuş mu? Sıfır test çalışmasına rağmen süreç 0 ile çıkmış mı? Adım continue-on-error ile başarısızlığı gizliyor mu? Koşul nedeniyle kritik iş atlanmış mı? Bu sorular, kanıtı değerlendirmek için gereklidir.

## Artefakt ile önbellek farkı

Artefakt, incelemek veya dağıtmak istediğiniz çıktı olabilir: test raporu, ekran görüntüsü, publish paketi. Cache ise tekrar indirilecek bağımlılıkları yeniden kullanarak süreyi azaltır. Cache'i tek gerçek kayıt arşivi gibi kullanmayın. Bir önceki head'in test dosyasını yeni head'de koşulmuş gibi sunmak da doğru değildir.

Bir test çıktısını yeniden kullanıyorsanız hangi SHA'da üretildiğini ve ilgili kodun değişip değişmediğini açıkça söyleyin. Yalnız belge değişmişse bütün uzun testleri tekrar çalıştırmamak mantıklı olabilir. Ancak “yeniden çalıştırılmadı, önceki aynı kod çıktısı kullanıldı” bilgisi raporda bulunmalıdır. Dürüst kapsam, yeşil sayıdan daha değerlidir.

# Günlük, gözlem, yedek ve geri yükleme

## Log, exception ve stack trace okuma

Log, uygulamanın belirli olaylarda bıraktığı kayıttır. Exception hata nesnesi; stack trace ise çağrı zincirinin izidir. Bir hata ekranında ilk satır çoğunlukla hata türünü, izleyen satırlar hangi dosya/metotlardan geçildiğini gösterir. Bütün izi ezberlemeyin; uygulamanıza ait ilk anlamlı satırı bulun.

`SqliteException: no such table: Jobs` gördüğünüzde şüphe migration, yanlış DB yolu veya yanlış çalışma ortamıdır. “Kod syntax hatası var” diye başlamazsınız. `Connection refused` ağdaki hedefte dinleyen servis olmadığını gösterebilir. `401` kimlik doğrulamaya, `403` yetki/erişim politikasına, `409` sürüm çakışmasına işaret edebilir. Hatanın katmanını sınıflandırmak araştırmayı daraltır.

Structured logging, metni gelişi güzel birleştirmek yerine alanlarla kayıt tutar. Örneğin olay adı, correlationId, endpoint, durum kodu ve süre ayrı alanlar olabilir. CorrelationId aynı isteğin proxy, API ve işleyici kayıtlarını ilişkilendirmeye yardım eder. Bu kimliği bilmek kullanıcının yaşadığı tek olayı log denizinden ayırabilir.

## Health check neyi kontrol ediyor?

`/health` örneğimiz yalnız sürecin yanıt verdiğini söyler. Veritabanının yazılabilir olduğunu veya bütün müşteri işlemlerinin çalıştığını doğrulamaz. Liveness, sürecin hayatta olmasıyla; readiness, trafiği almaya hazır olmasıyla ilişkilidir. Gerçek sistemde bu ayrım yeniden başlatma ve trafik yönlendirme kararlarını etkiler.

Health endpoint'ine bütün yapılandırmayı veya sırları döndürmeyin. Kamuya açık bir yanıt, sistemin hassas iç bilgisini açmamalıdır. İç operasyon paneli daha fazla bilgi gösterebilir ama orada da rol ve minimum alan ilkesi geçerlidir. “Sadece yönetici bakıyor” gereksiz bilgi toplamayı haklı çıkarmaz.

## Yedek almak ile geri dönebilmek farklıdır

Yedekleme, gereken veriyi belirli bir zamandaki haliyle korunabilir biçimde saklamaktır. Geri yükleme, bu kopyadan kullanılabilir bir ortam oluşturabilmektir. Bir dosyanın adının backup olması, onun açılabildiğini veya doğru anahtarla çözülebildiğini kanıtlamaz.

SQLite kullanırken çalışan veritabanını gelişigüzel dosya kopyasıyla yedeklemek doğru olmayabilir; WAL gibi yan dosyalar ve tutarlılık koşulları vardır. Veritabanının desteklediği tutarlı yedekleme yaklaşımını veya kontrollü durdurma akışını öğrenin. Bu kitap gerçek üretim DB’sine dosya kopyalama komutu vermez. Her uygulamanın anahtar, dosya eki ve şema gereksinimi ayrıca incelenmelidir.

Şifrelenmiş yedek için anahtar gerekir. Anahtar yalnız kaybolan sunucuda duruyorsa felaket anında yedeği çözemeyebilirsiniz. Buna karşılık anahtarı yedekle aynı herkese açık klasöre koymak gizliliği zayıflatır. Erişim, saklama ve kurtarma planı birlikte tasarlanır.

## Geri yükleme provası

Sentetik bir ortam kurun, ayırt edilebilir birkaç kayıt ekleyin, uygulamanın kendi desteklediği yedekleme işlemini kullanın. Sonra boş ve ayrı bir dizine geri yükleyin. Orijinal öğrenme DB'sinin üzerine yazmayın. Geri yüklenen ortamı farklı portta başlatın. Kayıt sayısını değil, kayıt içeriğini ve gerekli şifreli verinin açılmasını da kontrol edin.

RPO, kabul edilebilir veri kaybı penceresidir. Günde bir yedek alıyorsanız son yedekten sonraki işlemler risk altında olabilir. RTO, hizmeti geri getirmek için kabul edilebilir süredir. Bir haftada çözülebilen yedek küçük ofis için bile iş ihtiyacını karşılamayabilir. Bu terimler yalnız büyük şirketlerin kelimeleri değildir; hangi kaybı göze aldığınızı açıklaştırır.

# Hata avı atölyesi: semptomdan kök nedene

## Olay 1: kayıt ekleniyor, yeniden başlayınca kayboluyor

İlk varsayımınız “EF bozuk” olmasın. Uygulama bellek içi sağlayıcı mı kullanıyor? DB yolu her başlatmada rastgele geçici klasöre mi gidiyor? Container DB'yi volume dışında mı tutuyor? İlk adım, kullanılan gerçek tam DB yolunu sır içermeyecek biçimde incelemektir. Sonra önceki ve sonraki çalışmanın aynı dosyayı açtığını doğrulayın.

Deney: StudyApi'yi farklı çalışma klasörlerinden göreli study.db yolu ile başlatmanın ne değiştirdiğini araştırın. Göreli yolun neye göre çözüldüğünü açıklayın. Çözüm, canlı dosyaları arayıp rastgele taşımak değildir; yapılandırmada açık ve doğru kalıcı konum kullanmaktır.

## Olay 2: listede veri yok ama DB'de var

Filtre yanlış olabilir: Completed koşulu ters, TenantId yanlış, tarih sınırı başka timezone'da hesaplanmış olabilir. Yanlış veritabanına bakıyor da olabilirsiniz. “DB'de var” kanıtını aynı ortam ve bağlantı için doğrulayın. Sonra sorguyu küçük parçalara ayırın: önce kimlik, sonra tenant, sonra durum, sonra tarih filtresi.

Filtreyi tamamen kaldırıp üretime bırakmak çözüm değildir. Bu yalnız teşhis sırasında sentetik ortamda hangi koşulun sonucu daralttığını anlamaya yarayan deney olabilir. Kalıcı düzeltme iş kuralını doğru ifade etmelidir. Özellikle firma filtresini kaldırmak veri sızıntısı yaratabilir.

## Olay 3: aynı işlem iki kez stok düşürüyor

İstek sayısını Network panelinden inceleyin. Çift event listener var mı? Kullanıcı çift tıklamış mı? İstemci retry yapıyor mu? Sonra sunucunun aynı requestId'yi nasıl ele aldığını okuyun. Yalnız butonu disable etmek kullanıcı arayüzündeki bir kaynağı azaltır; ağ kaynaklı tekrar için sunucu idempotency gerekir.

Sentetik testte aynı gövde ve aynı requestId'yi iki kez gönderin. Ardından iki eşzamanlı istek gönderin. Beklenti yalnız yanıt kodu değildir; nihai stok, hareket sayısı ve audit kaydı da tek iş niyetine uymalıdır. İyi test sonuç durumunu kontrol eder.

## Olay 4: 502 var, uygulama sağlık yanıtı veriyor

Sağlık yanıtını hangi adresten aldığınızı netleştirin. Host'tan 5311'e ulaşmak, Caddy container'ının api:8080'e ulaşabildiğini kanıtlamaz. Proxy hedefi, ağ ve protokolü kontrol edin. API dinleme adresinin yalnız 127.0.0.1 olması, başka container'ın bağlanmasını engelleyebilir.

Bir seferde tek değişiklik yapın. Önce hedef portunu düzeltip tekrar ölçün; aynı anda DNS, image, Caddyfile ve güvenlik duvarını değiştirmeyin. Çok sayıda kontrolsüz değişiklik sorunun neden düzeldiğini öğrenmenizi engeller ve yeni hata yaratır.

## Olay 5: yerelde geçiyor, CI'da başarısız

Dosya adı büyük/küçük harfi Windows'ta fark edilmeyip Linux'ta sorun olabilir. Satır sonları CRLF/LF olabilir. SDK sürümü, çalışma dizini, saat dilimi, culture ve mevcut paketler farklı olabilir. Test kendi bilgisayarınızdaki gerçek Edge veya dış dosyaya bağımlı olabilir. Hata çıktısını kısaltarak belirleyici satırı bulun, sonra ortam farkını tek tek sınayın.

CI'da testi atlamak son çözüm değildir. Önce testin doğru varsayımı mı, ortam bağımlı yanlış varsayımı mı sınadığını anlayın. Örneğin İstanbul gece yarısına denk gelen bir “bugün” testi istek öncesi ve sonrası gün farkını düşünmelidir. Bütün tarihlere tolerans eklemek ise gerçek hatayı gizleyebilir; mümkünse denetlenebilir saat kullanılır.

## Olay 6: bütün testler geçti, kullanıcı yine hata buldu

Testler uygulamanın bütün olası durumlarının kanıtı değildir. Sadece yazılmış senaryolarda gözlenen davranışın kanıtıdır. Kullanıcının verisi, rolü, ekran boyutu, boş durum veya işlem sırası testlerde yoksa hata kaçabilir. Önce olayı küçük tekrarlanabilir senaryoya indirip sonra düzeltmeyi koruyacak test ekleyin.

Bir testin beklediği sonuç yanlış olabilir. Şifre yardım listesi Unicode büyük harfi kabul ederken sunucu ASCII kuralıyla reddediyorsa, yalnız “liste yeşil oldu” testi yeşil geçebilir. Doğru regresyon, kullanıcıya anlatılan kuralı gerçek sunucu davranışıyla karşılaştırmalıdır. Test yazmak kadar doğru iddiayı test etmek önemlidir.

# Uygulamalı görevler ve çözümler

## Görev A: kodu konuşarak açıkla

StudyApi POST endpoint'ini açın. Her satırı sesli açıklayın. Kullanıcı gövdesi nereden geliyor? Trim ne yapıyor? Boş başlık nerede reddediliyor? Id ne zaman oluşuyor? SaveChanges kaldırılırsa ne olur? Created yanıtındaki adres neyi gösteriyor? İnternete bakmadan cevaplayın, sonra koda dönerek kontrol edin.

Çözüm: JSON CreateJobInput'a bağlanır. Trim baştaki/sondaki boşlukları temizler; ortadaki kelimeleri birleştirmez. Boş veya 200'den uzun başlık 400 alır. Entity context'e eklenir ve SaveChanges kalıcı yazmayı yapar. SQLite tarafından üretilen kimlik yazma sonrasında nesneye gelir. Created, oluşan kaynağın adresini belirtir. SaveChanges yoksa başarılı cevap gibi görünen fakat kalıcı olmayan bir işlem oluşturabilirsiniz; bu nedenle sonuç DB'den yeniden okunarak test edilir.

## Görev B: kapalı işleri filtrele

GET /api/jobs için isteğe bağlı `completed` sorgu parametresi ekleyin. Parametre yokken bütün işler, true iken tamamlanmış, false iken açık işler gelsin. Sıralama ve en çok 100 sınırını koruyun. Önce kendi çözümünüzü yazın.

Çözümün temel fikri nullable bool kullanmaktır. Başlangıçta `IQueryable<StudyJob> query = db.Jobs.AsNoTracking();` oluşturun. `completed.HasValue` ise `query = query.Where(x => x.Completed == completed.Value);` ekleyin. Sonra OrderBy/Take/Select/ToListAsync uygulayın. Bütün tabloyu ToList ile çekip bellekte filtrelemeyin. Testte üç durumun da satır kimliklerini doğrulayın.

## Görev C: sürüm yarışını anlat

İki kullanıcı aynı işi Version=4 ile açtı. Birinci kullanıcı kaydedip Version=5 yaptı. İkinci kullanıcı eski içerikle kaydetti. Neden ikinci işlem sessizce birincinin değişikliğini ezmemeli? Yalnız “kullanıcıya hata gösterilir” demek yerine sunucudaki koşulu açıklayın.

Çözüm: İkinci isteğin dayandığı kayıt durumu artık güncel değildir. API istemcinin version değerini güncel kayıtla karşılaştırır ve 409 döndürür. Çok kısa okuma/yazma yarışında EF'in concurrency token koşulu UPDATE'in eski sürümle eşleşmesini engeller; DbUpdateConcurrencyException uygun yanıta çevrilir. Kullanıcıya güncel veriyi okuyup karar verme fırsatı verilir. Otomatik “son yazan kazanır” bazı alanlarda kabul edilebilir ama finans/stok gibi ilişkili verilerde bilinçsizce seçilmemelidir.

## Görev D: migration incele

StudyJob'a Priority adlı tam sayı alanı ekleyin. 1 ile 5 arasında olduğunu API'de doğrulayın. Migration oluşturup SQL'i okuyun. Eski iki sentetik işin yükseltme sonrasında hangi önceliği alacağını yazın. Default kararını iş anlamıyla açıklayın.

Çözüm: Model değişikliği ile API doğrulaması ayrı yazılır. Eski satırların sıfır alması yeni iş kuralında geçersizse bir veri geçişi gerekir; örneğin 3 varsayılanı seçilebilir. Ancak 3'ün ne anlama geldiği belgelenmelidir. Migration'da eski satırlar korunur; yükseltme testinde sayıları ve başlıkları aynı kalır, Priority geçerli değere döner. Kayıtların tümünü silip yeniden oluşturmak veri koruyan yükseltme değildir.

## Görev E: tenant saldırısını tasarla

Bir iş oluşturma endpoint'i gövdeden TenantId alıyor. Yönetici arayüzünde firma seçici görünmüyor. Bunun neden hâlâ riskli olduğunu ve hangi iki testi yazacağınızı belirtin.

Çözüm: Görünmeyen alan HTTP istemcisiyle yine gönderilebilir. Firma kimliği doğrulanmış oturumdan alınmalı veya platforma özel firma seçimi açıkça ayrı yetkilendirilmelidir. Testlerin biri A kullanıcısının A işini oluşturabildiğini, diğeri A kullanıcısının B TenantId gönderdiğinde B adına kayıt oluşturamadığını kanıtlar. Yalnız yanıtı değil B'nin iş sayısının değişmediğini ve A/B audit sınırını da kontrol edin.

## Görev F: Docker veri kaybını teşhis et

Compose'da study-data volume'u `/data` dizinine bağlı, fakat DatabasePath `/app/study.db`. Container yeniden oluşturulunca işler kayboluyor. Veriyi rastgele taşımadan kök nedeni açıklayın.

Çözüm: Kalıcı volume doğru bağlanmış olsa bile veritabanı başka yola yazılıyor. Yapılandırma ve gerçek tam DB yolu eşleştirilmelidir. Sentetik ortamda doğru yolu `/data/study.db` yapıp yeniden kayıt oluşturun; stop/start ve down/up sonrasında kaydı doğrulayın. Gerçek veri söz konusuysa önce mevcut dosyanın tutarlı yedeği ve kontrollü aktarım planı gerekir. Volume tanımını görmek tek başına yeterli kanıt değildir.

## Görev G: yavaş sorguyu düzelt

Bir endpoint bütün işleri ToListAsync ile alıyor, sonra foreach içinde her müşteriyi ayrı sorguluyor. İlk 50 sonuç gösteriliyor. Hangi iki maliyet var? Neyi ölçersiniz?

Çözüm: Önce bütün iş tablosu gereksiz taşınıyor. Sonra her iş/müşteri için ayrı sorgu üretilerek N+1 gidiş gelişi oluşuyor. Filtre, sıralama ve sayfalama DB'ye taşınır; gerekli müşteri alanları projeksiyon veya uygun ilişki yüklemesiyle toplu alınır. Sorgu sayısı, taşınan satır/sütun, yanıt süresi ve sorgu planı ölçülür. “Include ekledim, artık hızlı” demeden veri hacmiyle deneyin.

## Görev H: güvenilir teslim raporu yaz

Kod derlendi, iki hedefli test geçti, Docker motoru kapalı olduğu için container testi başlamadı. CI eski commit'te yeşil. Nasıl rapor yazarsınız?

Çözüm: Hangi SHA incelendiğini ve gerçek komutların sonuçlarını yazarsınız. Build başarılı; iki hedefli test başarılı, atlanan yok. Container testi çalıştırılmadı; motor bağlantısı engeli belirtilir. Eski SHA'nın CI sonucu güncel kod için başarı diye sunulmaz. Kod hazır, test kapsamı sınırlı, deployment yapılmadı şeklinde durumlar ayrılır. Bu dürüstlük eksiklik değil, ekip arkadaşının doğru karar vermesi için gerekli bilgidir.

## Kendi kendini değerlendirme

Bu bölümün sonunda orta seviye olduğunuzu bir unvanla ölçmeyin. Şu işleri yardım almadan yapmayı hedefleyin: yeni endpoint ve DTO yazmak; geçersiz istek için test üretmek; üretilen sorgunun nerede yürüdüğünü açıklamak; basit migration'ı incelemek; eski sürüm çakışmasını göstermek; iki firma izolasyon testini tasarlamak; image/container/volume farkını çizmek; 502 hatasında bağlantı zincirini izlemek; test sonucunu SHA ve kapsamla raporlamak.

Bir görevde takıldığınızda çözümü doğrudan yapıştırmak yerine önce tahmininizi yazın. Sonra tek deney kurun ve beklenen/gerçek sonucu karşılaştırın. Doğru cevabı bir kez görmekten daha değerli olan, yanlış tahmini kontrollü deneyle düzeltebilmektir. Gerçek yazılım geliştirme günlerinin büyük kısmı bu döngüyle geçer.

## Bu bölümün resmi kaynakları ve ileri okuma

Aşağıdaki kaynaklar komut ve kavram kontrolü için kullanılmıştır. Öğretim örnekleri bu kitap için hazırlanmıştır; örneklerin uygulanacağı .NET 10 ve EF Core 10 hedefini koruyun. Resmi sayfada farklı sürüm seçeneği açılırsa sürüm seçicisini kontrol edin. Başlangıçta bütün belgeleri ezberlemek yerine ilgili komutun seçeneklerini okuyup küçük öğrenme projenizde deneyin.

- Microsoft Learn, Minimal API eğitimi: https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api?view=aspnetcore-10.0
- Microsoft Learn, EF Core ve SQLite başlangıcı: https://learn.microsoft.com/en-us/ef/core/get-started/overview/first-app?tabs=netcore-cli
- Microsoft Learn, EF6 ve EF Core karşılaştırması: https://learn.microsoft.com/en-us/ef/efcore-and-ef6/
- Microsoft Learn, EF Core CLI: https://learn.microsoft.com/en-us/ef/core/cli/dotnet
- Microsoft Learn, migration yönetimi: https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/managing
- Microsoft Learn, global query filter: https://learn.microsoft.com/en-us/ef/core/querying/filters
- Microsoft Learn, concurrency çatışmaları: https://learn.microsoft.com/en-us/ef/core/saving/concurrency
- Docker, container kavramı: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/
- Docker, Compose başlangıcı: https://docs.docker.com/compose/gettingstarted/
- Caddy, reverse_proxy yönergesi: https://caddyserver.com/docs/caddyfile/directives/reverse_proxy
- Caddy, komut satırı: https://caddyserver.com/docs/command-line
- Caddy, çalıştırma ve container ağ notları: https://caddyserver.com/docs/running
- GitHub Docs, Actions başlangıcı: https://docs.github.com/en/actions/get-started/quickstart
