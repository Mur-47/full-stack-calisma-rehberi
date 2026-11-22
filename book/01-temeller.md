# Bilgisayarın içinde ne oluyor?

## Bu kısmın sonunda yapabileceklerin

Bir uygulamayı kullanmak ile uygulamanın nasıl çalıştığını anlamak farklı becerilerdir. Arabayı sürebilirsin; bu, motoru söküp arızayı bulabildiğin anlamına gelmez. Yazılımda da düğmenin çalışması son görüntüdür. Dosya, süreç, ağ, tarayıcı ve sunucu birbirine bağlıdır. Bu bölümde o bağlantıları kuracağız. Kodun neden çalışmadığını düşünürken elinde yalnız tahmin değil, kontrol edilebilir bir model olacak.

Bu metni okurken iki ayrı defter tut. İlkine yeni kelimeleri kendi cümlelerinle yaz. İkincisine deney kaydı yaz: ne yaptım, ne bekledim, ne gördüm, fark neden oluştu? Bir komutun çıktısını görmeden sonraki komuta geçme. Buradaki amaç yazılımcı gibi görünmek değil; bir iddiayı küçük bir deneyle doğrulayabilmektir.

Uygulama örneğimiz hayali bir bakım takip sistemidir. Bir firma, bakım bekleyen cihazleri görür ve iş emri açar. Gerçek müşteri, şifre, sunucu veya veritabanı kullanmayacağız. Alıştırmaları ayrı bir çalışma klasöründe yapacağız. Alıştırma için ayrı bir klasör açacaksın. Aynı cümleyi her bölümde tekrar etmeyeceğiz; bu sınır bütün kitap için geçerlidir.

## Donanım, işletim sistemi ve program

Donanım elle tutulan parçadır: işlemci, bellek, disk, ağ kartı. İşletim sistemi bu parçaların kullanımını düzenler. Windows bir işletim sistemidir. Program ise işletim sisteminin çalıştırdığı talimatlar ve kullandığı veriler bütünüdür. Tarayıcı, metin düzenleyici ve veritabanı sunucusu birer programdır.

İşlemci komut yürütür. Bellek, çalışırken hızla erişilmesi gereken veriyi tutar. Disk kalıcı dosyaları tutar. Bu ayrım hata çözmede önemlidir. Bilgisayar kapanınca açık değişkenlerin kaybolması normaldir; diske yazılmış dosyanın kendiliğinden kaybolması başka bir sorundur. Bir sayfayı yenileyince listen siliniyorsa önce verinin yalnız tarayıcı belleğinde mi kaldığını düşün. Docker, veritabanı veya Git suçlamadan önce verinin nerede tutulduğunu bul.

Dosya diskte saklanır; program başlatılınca bir süreç oluşur. Docker simgesi uygulamayı açar; motorun durumunu Docker Desktop içinde görebilirsin. Benzer şekilde `app.js` dosyasının yüklenmesini Network panelinde kontrol edebilirsin. Dosya bulunabilir, fakat HTML yanlış adrese bakıyor olabilir. Yazılımda sürekli şu ayrımı yap: mevcut mu, çalışıyor mu, doğru sürümü mü çalışıyor, beklenen ortamda mı çalışıyor?

## Süreç, iş parçacığı ve kimlik

Bir program çalıştırıldığında işletim sistemi bir süreç oluşturur. Süreç, çalışan programın belleği, açık dosyaları ve diğer kaynaklarıyla birlikte yürüyen örneğidir. Her süreç bir PID ile tanınır. Aynı programdan iki tane açarsan genellikle iki süreç veya birden fazla yardımcı süreç oluşur. Tarayıcılar sekmeler ve güvenlik ayrımları nedeniyle birçok süreç kullanabilir.

İş parçacığı, sürecin içindeki yürütme akışıdır. İlk aşamada ayrıntısını ezberleme. Şunu bilmen yeterli: dosya, süreç ve pencere ayrı kavramlardır. Pencere kapansa bile bazı programlar arka planda yaşamaya devam edebilir. Bir terminalde çalışan sunucuyu başka terminalden başlatınca port çakışmasının nedeni budur.

PowerShell'de yalnız okuma yapan bu komutları dene:

```powershell
Get-Process | Select-Object -First 8 Id, ProcessName
Get-Process -Name notepad -ErrorAction SilentlyContinue
```

İlk komut süreç listesinin sekiz satırını gösterir. İkinci komut Not Defteri açıksa ilgili süreci gösterir; açık değilse boş sonuç normaldir. Çıktıdaki sayılar bu kitapla aynı olmayacaktır. PID her çalıştırmada değişebilir. Bir öğretici ekranda 8460 yazıyor diye kendi bilgisayarında 8460 numaralı süreci kapatma.

## Terminal, kabuk ve komut

Terminal yazı yazarak programlarla konuştuğun penceredir. Kabuk bu yazıyı yorumlayan programdır. Windows Terminal birden fazla kabuğu açabilen uygulamadır. PowerShell, Command Prompt ve Bash farklı kabuklardır. Görünüşleri benzer olsa da sözdizimleri farklıdır.

Komut satırı çoğu zaman üç parçadır: program, işlem ve seçenekler. `git status --short` yazdığında `git` programı çağrılır, `status` işlemi seçilir, `--short` çıktının kısa olmasını ister. `Get-ChildItem -File` ise PowerShell komutudur; `-File` yalnız dosyaları seçer. Her tireli kelime aynı kurala uymaz; seçenekleri ilgili aracın yardımından öğrenirsin.

Bir hata gördüğünde kabuğu da rapora yaz. Bash için hazırlanmış `export NAME=value` satırını PowerShell'e yapıştırmak çalışmaz. PowerShell'de geçici ortam değişkeni şöyle tanımlanır:

```powershell
$env:LEARNING_MODE = 'practice'
Write-Output $env:LEARNING_MODE
```

Bu değişken, o oturumdan başlatılan süreçlere aktarılabilir. Bilgisayardaki bütün oturumlara kalıcı olarak yazılmaz. Ortam değişkeni gizli kasa değildir. Şifreleri komut geçmişine veya ekran görüntüsüne koyma. Buradaki `practice` yalnız çalışma ortamını adlandıran bir ayardır.

## Çalışma dizini ve dosya yolu

Terminalin o anda baktığı klasöre çalışma dizini denir. `Get-Location` bunun adresini verir. Mutlak yol kökten başlayan tam adrestir. Göreli yol mevcut çalışma dizinine göre yorumlanır. `./index.html`, bulunduğun yerdeki dosyadır. `../index.html`, üst klasördeki dosyadır. Aynı komut farklı klasörde farklı dosyaya erişebilir.

Şu alıştırmada yeni bir laboratuvar klasörü oluştur. Önceden aynı adla önemli dosya varsa başka ad seç. Komutlar örnek bir kullanıcının gerçek proje klasörünü hedeflemez.

```powershell
$lab = Join-Path $env:USERPROFILE 'Documents\FullStackLab'
New-Item -ItemType Directory -Path $lab
Set-Location -LiteralPath $lab
Get-Location
New-Item -ItemType Directory -Name 'web'
Get-ChildItem
```

Beklenen sonuç, `FullStackLab` içinde `web` adlı bir klasör görmendir. Klasör zaten varsa `New-Item` bunu söyleyebilir. Hata mesajını okumadan silmeye geçme. Hedefi değiştirmen çoğu zaman daha güvenlidir. `Set-Location` dosyayı taşımaz; terminalin baktığı yeri değiştirir.

Boşluk bulunan yollarda tırnak veya `-LiteralPath` kullan:

```powershell
Set-Location -LiteralPath (Join-Path $env:USERPROFILE 'Documents\Kod Dersleri')
```

Bu satır yalnız söz dizimi örneğidir. Kendi bilgisayarında böyle klasör yoksa çalışmaması beklenir. Hata mesajında `Cannot find path` görüyorsan ilk şüphe internet veya derleyici değil, yolun doğruluğudur.

## Uzantı, içerik ve kodlama

`index.html` dosyasının `.html` uzantısı, dosyanın HTML olarak ele alınacağını anlatır. Dosya adını değiştirmek içeriğini dönüştürmez. Bir resme `.txt` yazarsan resim metne dönüşmez. Windows uzantıları gizliyorsa `index.html.txt` oluşturabilirsin. Dosya Gezgini'nde dosya adı uzantılarını görünür yap.

Kod dosyasını düz metin düzenleyicisinde UTF-8 olarak kaydet. Türkçe karakterler için UTF-8 kullan. `ş` yerine garip simgeler çıkması çoğu zaman yanlış kodlama veya yanlış HTTP `charset` bilgisidir. Karakterler seçilen kodlamayla baytlara çevrilir. Özellikle şifre uzunluğu, dosya boyutu ve HTTP veri uzunluğu konuşurken bu ayrım önem kazanır.

Dosyanın adı, konumu, uzantısı ve içeriğini ayrı ayrı doğrula. Örneğin `style.css` doğru klasörde olsa bile HTML içindeki `href="styles.css"` farklı dosya ister. Bir harf farkı yeterlidir. Windows'ta çalışan büyük/küçük harf hatası Linux'ta bozulabilir; dosya adlarını tutarlı yazmak bu nedenle de önemlidir.

## Bir hatayı ilk kez sınıflandırmak

Hataları katmanlarına göre ayırabilirsin. Şu beş kutuyla başla:

- Dosya/yol hatası: gerekli dosya bulunmuyor.
- Sözdizimi hatası: dilin kurallarına aykırı kod var.
- Çalışma zamanı hatası: program başladıktan sonra beklenmeyen durum oluşuyor.
- Mantık hatası: program hata vermiyor ama yanlış sonuç üretiyor.
- Ortam hatası: doğru kod, eksik araç veya yanlış ayar nedeniyle çalışmıyor.

Örneğin `git is not recogned` yazıyorsa henüz branch çatışmasına bakma; Git komutu bulunamıyor. `Address already in use` yazıyorsa sunucu adresine başka süreç bağlanmış olabilir. Toplam 100 yerine 100100 oluyorsa sayı yerine metin birleştiriyor olabilirsin. Hatanın cümlesini bir cümleyle Türkçeye çevir. Sonra o cümleyi doğrulayacak en küçük kontrolü seç.

## Alıştırma: dosyayı arayan dedektif

`web` klasörüne `not.txt` koy. İçine `İlk deneyim` yaz. Terminalde `FullStackLab` kökündeyken `Get-Content not.txt` dene. Sonra `Get-Content ./web/not.txt` dene. Hangi komut neden başarılı oldu? Hangi yol mutlak, hangisi göreli? Son olarak dosyanın adını `NOT.txt` yapmanın başka bir işletim sisteminde neden önemli olabileceğini yaz.

Bu alıştırmayı tamamlamadan topluca kurulum komutları çalıştırma. Çalışma dizinini bilmiyorsan doğru aracı yanlış yerde kullanabilirsin. Daha gelişmiş bir yazılımcıyı ayıran davranışlardan biri, değişiklik yapmadan önce hedefi kontrol etmesidir.

Kaynak: [Microsoft Learn: Get-Location](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-location). Bu bölümdeki laboratuvar, açıklama ve hata senaryoları bu rehber için hazırlanmıştır.

# İnternet, istemci, sunucu ve HTTP

## Bir sayfa açılınca gerçekleşen yolculuk

Tarayıcıya bir adres yazdığında tek bir sihirli işlem gerçekleşmez. Tarayıcı adresi yorumlar, gerekirse alan adının adresini bulur, sunucuyla bağlantı kurar, güvenli bağlantı gerekiyorsa TLS görüşmesini yapar ve HTTP isteği gönderir. Sunucu yanıt verir. HTML içindeki stil, resim ve betik adresleri için yeni istekler yapılabilir. Tarayıcı bu parçaları kullanarak sayfayı oluşturur.

Bu zincirin herhangi bir halkası bozulabilir. İnternet çalışıyor olsa bile yanlış DNS kaydı sayfayı ulaşılamaz yapabilir. Sunucu açık olsa bile uygulama yanlış portta dinliyor olabilir. HTML gelse bile JavaScript 404 alıyorsa düğmeler çalışmayabilir. Hata ayıklarken "site bozuk" yerine "HTML geldi, app.js 404 aldı" demen çözümü daraltır.

## İstemci ve sunucu birer roldür

İstemci isteği başlatan taraftır. Tarayıcı çoğu web uygulamasında istemcidir. Sunucu ise isteği dinleyip yanıtlayan taraftır. Sunucu sözcüğü bazen fiziksel bilgisayarı, bazen o bilgisayardaki programı anlatır. Bu iki anlamı ayır. Tek bilgisayarda tarayıcı ve geliştirme sunucusu beraber çalışabilir. Fiziksel olarak aynı makinede olmaları, mantıksal rollerini birleştirmez.

Ön yüz, kullanıcının etkileştiği arayüzdür. Arka uç, istekleri işler, yetkiyi kontrol eder ve iş kurallarını uygular. Veritabanı kalıcı veriyi yönetir. Full stack geliştirici bu parçalar arasında nasıl veri aktığını anlayabilir. İlk hedefin bu parçalar arasındaki veri yolunu izleyebilmek olsun.

Bakım sistemi örneğinde kullanıcı "İşi tamamla" düğmesine basar. Ön yüz istek gönderir. Arka uç bu kullanıcının bu işi tamamlamaya yetkili olup olmadığını kontrol eder. Veritabanı değişikliği kaydeder. Yanıt gelir ve ön yüz durumu yeniler. Düğmeyi gizlemek, sunucudaki yetki denetiminin yerine geçmez.

## IP, alan adı ve DNS

IP adresi ağdaki hedefi adreslemek için kullanılır. Alan adı insanların daha kolay hatırladığı addır. DNS, bir alan adına ait kayıtları bulma sistemidir. Telefon rehberi benzetmesi yararlıdır, fakat eksiktir: DNS yalnız tek bir isimden tek bir adrese dönüşüm değildir; farklı kayıt türleri, önbellek ve yetkili sunucular vardır.

`localhost` kendi bilgisayarını gösteren özel addır. `127.0.0.1` IPv4 loopback adresidir. Bir arkadaşına `http://localhost:5500` adresini gönderirsen onun tarayıcısı senin bilgisayarını değil, kendi bilgisayarını arar. Bu hata, ilk kez proje paylaşan geliştiricilerde çok yaygındır.

Bir alan adına `ping` yanıtı gelmemesi tek başına sitenin kapalı olduğunu kanıtlamaz; bazı sistemler ICMP yanıtını engeller. Benzer biçimde DNS çözülmesi uygulamanın sağlıklı olduğunu göstermez. Her kontrol yalnız ölçtüğü şeyi kanıtlar. Ağ teşhisinde büyük iddia yerine küçük kanıt biriktir.

## Port ve protokol

IP adresi apartmanın adresiyse port daire numarası gibi düşünülebilir. Aynı makinede birden fazla program farklı portlarda dinleyebilir. HTTP için 80, HTTPS için 443 yaygın varsayılanlardır. Geliştirmede 5500, 3000 veya 8080 gibi başka portlar kullanılır. Sayıların kendisi aracı belirlemez: 3000 portunda uygun herhangi bir program dinleyebilir.

URL'de protokol, hedef, port ve yol bulunabilir:

```text
http://localhost:5500/maintenance?status=open

Protokol: http
Hedef: localhost
Port: 5500
Yol: /maintenance
Sorgu: status=open
```

`#bolum-3` gibi hash parçası normal HTTP isteğinin sunucuya gönderilen yoluna dahil edilmez. Tarayıcı tarafında bölüm seçmek veya istemci yönlendirmesi için kullanılabilir. Buna karşılık query string sunucuya gider. Hassas token'ları URL'ye koymanın loglar ve geçmiş açısından sonuçlarını ileride güvenlik bölümünde inceleyeceksin.

Bir geliştirme portu doluysa rastgele süreç kapatma. Önce yalnız o portu kimin dinlediğini oku:

```powershell
Get-NetTCPConnection -LocalPort 5500 -State Listen `
  -ErrorAction SilentlyContinue |
  Select-Object LocalAddress, LocalPort, OwningProcess
```

Boş sonuç, o anda bu sorgunun gördüğü bir dinleyici olmadığını söyler. Süreç adı gerekiyorsa çıktıdaki PID için `Get-Process -Id 1234` kullan; 1234 yerine kendi çıktındaki değeri yaz. Kendi başlattığın terminal sunucusunu durdurmak için önce o terminalde `Ctrl+C` kullan. Bu, uygulamaya kontrollü kapanma fırsatı verir.

## HTTP isteği ve yanıtı okumak

HTTP uygulama katmanı protokolüdür. İsteğin metodu, hedefi, başlıkları ve bazen gövdesi vardır. Yanıtta durum kodu, başlıklar ve bazen gövde bulunur. HTTP/2 ve HTTP/3'ün tel üzerindeki gösterimi bu basit metin örneğinden farklı olabilir; örnek, mantıksal parçaları öğretir.

```http
GET /api/work-orders?status=open HTTP/1.1
Host: example.test
Accept: application/json
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

[{"id":7,"title":"Aylık bakım","status":"Open"}]
```

`GET` genellikle veri okumak içindir. `POST` bir işlem veya yeni kaynak oluşturmak için kullanılabilir. `PUT` belirli kaynağın durumunu değiştirmek için kullanılır. `PATCH` kısmi değişiklik anlatabilir. `DELETE` silme isteğidir. İsimler tek başına güvenlik sağlamaz; sunucu her durumda girdiyi ve yetkiyi doğrulamalıdır. GET'in veri değiştirmesi, önbellek ve otomatik tekrar davranışları nedeniyle tehlikeli tasarım olabilir.

Başlıklar ek bilgidir. `Content-Type`, gönderilen verinin türünü; `Accept`, istemcinin almak istediği türü bildirir. JSON metin biçimidir. JavaScript nesnesinden serileştirilerek üretilir; ağda gönderilirken belirli sözdizimine sahip karakterlerden oluşur. JSON'da anahtarlar çift tırnakla yazılır. JavaScript'te geçerli olan her ifade JSON değildir.

## Durum kodunu doğru yorumlamak

200 genellikle başarılı yanıt, 201 yeni kaynak oluşturuldu, 204 gövdesiz başarıdır. 400 isteğin kabul edilemeyen biçim veya veri taşıdığını anlatabilir. 401 kimliğin doğrulanması gerektiğini, 403 mevcut erişime izin verilmediğini, 404 hedefin bulunmadığını, 409 mevcut durumla çatışmayı, 429 hız sınırını, 500 sunucu tarafında beklenmeyen hatayı ifade etmek için kullanılır.

Bu kodlar tanı değil, ipucudur. 404 görünce yalnız dosya var mı diye bakmazsın; URL yolu, route eşleşmesi ve bazen kaynağın kullanıcıya görünürlüğü de etkili olabilir. 200 görmek de iş kuralının doğru olduğunu kanıtlamaz. Yanlış firmaya ait veriyi döndüren endpoint 200 verebilir; bu yine ciddi hatadır.

Bir istek için şu kayıt yeterli başlangıçtır: metod, URL'nin sır içermeyen kısmı, durum kodu, yanıt gövdesinin ilgili bölümü, beklenen davranış. Cookie ve Authorization başlıklarını herkese açık ekran görüntüsünde paylaşma. Kendi hata kaydın, başka birinin oturum anahtarını taşımamalıdır.

## HTTPS, TLS ve sertifika

HTTPS, HTTP iletişiminin TLS ile korunmasıdır. TLS aktarım sırasında dinlemeye ve değiştirilmeye karşı koruma sağlar, sertifikalar hedef kimliğini doğrulamaya yardımcı olur. Kilit işareti sitenin dürüst veya hatasız olduğunu söylemez. Sahte ürün satan site de geçerli HTTPS kullanabilir.

Yerelde HTTP ile çalışmak, bütün interneti HTTP ile yayınlamayı uygun yapmaz. Üretimde cookie, yönlendirme ve ters vekil ayarları ayrıca düşünülür. Sertifika hatasını gidermek için tarayıcı güvenliğini kalıcı kapatmak öğrenme yöntemi değildir. Yanlış alan adı, süresi geçmiş sertifika ve güvenilmeyen yerel sertifika farklı sorunlardır; önce hata türünü oku.

## Önbellek ve eski sürüm yanılsaması

Tarayıcı her dosyayı her seferinde sıfırdan indirmeyebilir. Cache, yeniden kullanılabilecek yanıtları saklar. Önbellek performansı artırır; yanlış yapılandırılırsa yeni kodun görünmesini geciktirir. Sunucuda dosyayı değiştirdikten sonra eski CSS görünüyorsa hemen dağıtımı tekrar etme. Network panelinde gelen dosyanın URL'sini, içeriğini ve cache başlıklarını kontrol et.

Geliştirme sırasında DevTools içindeki Disable cache seçeneği tanıya yardım edebilir. Bu ayar yalnız araç açıkken etkili olabilir ve üretim kullanıcılarının sorununu çözmez. Kalıcı çözüm çoğu zaman içerik parmak izli dosya adı veya kontrollü sürüm adresidir. Aynı URL'yi uzun süre immutable yayınlayıp içerik değiştirmek hatalı sözleşmedir.

## Hata laboratuvarı: görüntü var, düğme yok

Varsayımımız: HTML açılıyor, fakat Kaydet düğmesi hiçbir şey yapmıyor. Önce F12 ile Console'u aç. Kırmızı bir JavaScript hatası var mı? Ardından Network'te `app.js` isteğini bul. 404 mü, 200 mü? 200 ise Response içinde beklediğin kod var mı? Dosya yerine HTML hata sayfası gelmiş olabilir. Sonra düğmeye bas ve yeni ağ isteği oluşup oluşmadığına bak.

Bu sıra bir karar ağacıdır. Betik hiç yüklenmediyse event listener ayrıntısını incelemek erken olur. Betik yüklenmiş ama sözdizimi hatasıyla durduysa API yetkisine bakmak erken olur. İstek oluşmuş ve 403 dönmüşse düğmenin CSS rengine bakmak erken olur. Sorunu ilk başarısız sınırda yakalamaya çalış.

## Alıştırmalar

1. `https://example.test:8443/api/jobs?page=2#details` adresini parçalara ayır. Hangisi normal HTTP isteğinde sunucuya gitmez?
2. Tarayıcı Network panelinde HTML 200, CSS 200, JS 404 görüyorsun. Sorunun ilk araştırılacak yeri nedir?
3. Bir düğme 403 alıyor. Kullanıcının isteğini başka bir firmanın kimliğiyle tekrar göndermek neden doğru çözüm değildir?
4. İki terminalden aynı sunucuyu aynı portta başlattın. İkinci terminalin hatasını nasıl doğrular, kendi sunucunu nasıl kapatırsın?

Kaynak: [MDN: HTTP genel görünümü](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview). URL ve hata laboratuvarları rehber için hazırlanmış sentetik örneklerdir.

# Git: kodun geçmişini yönetmek

## Git ile GitHub neden farklıdır?

Git, sürüm kontrol aracıdır. Dosyaların değişiklik geçmişini yerel bilgisayarda kaydeder. GitHub ise Git depolarını barındıran ve işbirliği özellikleri sunan hizmettir. Git internet olmadan kullanılabilir. GitHub olmadan Git vardır; Git olmadan GitHub'ın bazı dosya düzenleme özellikleri kullanılabilse de yazılım geliştirme akışının temeli yine Git geçmişidir.

Bir klasörün ZIP kopyasını almak yedek olabilir; sürüm kontrolü değildir. Git sana hangi değişikliğin hangi amaçla yapıldığını, hangi satırın ne zaman değiştiğini ve iki çalışma kolunun nasıl birleştiğini anlatır. İyi commit geçmişi, gelecekteki hata çözme süresini kısaltır. Fakat Git'e kaydetmediğin çalışmayı Git'in geri getireceğini varsayma.

Repository veya kısaca repo, sürüm kontrolü yapılan depodur. Çalışma ağacı düzenlediğin dosyalardır. Staging area, bir sonraki commit'e seçtiğin değişiklik kümesidir. Commit, kayıtlı bir anlık görüntüye ve açıklamaya sahiptir. Branch, bir commit'i gösteren ve yeni commit'lerle ilerleyen isimli başvurudur. Bu kelimeleri ayrı öğren; aksi halde `save`, `commit`, `push` ve `deploy` birbirine karışır.

## Kaydetmek, commit, push ve deploy

Editörde Kaydet, dosyayı diske yazar. Commit, seçtiğin değişikliği Git geçmişine ekler. Push, yerel commit'leri uzak depoya gönderir. Deploy, çalışan uygulamayı bir ortama kurar veya yeni sürümü o ortamda başlatır. Bunların hiçbiri diğerini otomatik garanti etmez.

GitHub'da kod görünmesi, canlı sunucunun o kodu çalıştırdığı anlamına gelmez. Commit atmak testleri çalıştırmaz; ayrıca test veya CI tanımlanmış olması gerekir. CI'ın yeşil olması testlerin kapsamı dışında hata olmadığı anlamına gelmez. Her teslimde hangi adımın gerçekten gerçekleştiğini ayrı yazmayı alışkanlık haline getir.

## İlk güvenli repo

Bu bölümün bütün komutlarını yalnız öğrenme için oluşturduğun yeni klasörde çalıştır. `Get-Location` ile hedefi kontrol et. Aşağıdaki yerel e-posta örnektir; gerçek GitHub kimliğinin yerine zorunlu değildir. `--global` kullanmadığımız için ayar yalnız bu depoda tutulur.

```powershell
# Yeni bir terminal açtıysan $lab boş olur; yeniden tanımla:
$lab = Join-Path $env:USERPROFILE 'Documents\FullStackLab'
Set-Location -LiteralPath $lab
New-Item -ItemType Directory -Name 'git-practice'
Set-Location './git-practice'
git init -b main
git config user.name 'Ogrenci'
git config user.email 'learner@example.test'
'Bakim takip laboratuvari' | Set-Content README.md
git status
```

`git status` README dosyasını untracked gösterecektir. Untracked, Git'in bu dosyanın geçmişini henüz takip etmediğini söyler. Dosyanın diskte olmadığı anlamına gelmez. Şimdi yalnız bu dosyayı seç:

```powershell
git add README.md
git diff --cached
git commit -m 'docs: laboratuvar amacini ekle'
git status
git log --oneline
```

Beklenen sonuç bir commit ve temiz çalışma ağacıdır. Commit kimliği kitapta sabit yazılmaz; içerik ve metadata'ya bağlıdır. `git diff --cached`, seçtiğin değişikliğin commit öncesi son kontrolüdür. Her şeyi otomatik eklemek yerine önce dosya adını açıkça vermen yanlış dosyayı commit etme riskini azaltır.

## Diff okumak

Diff, iki durumun farkıdır. `git diff` çalışma ağacı ile index arasındaki farkı gösterir. `git diff --cached`, index ile mevcut commit arasını gösterir. `git diff HEAD` mevcut commit ile çalışma durumunu birlikte karşılaştırmak için kullanılabilir. Dosyayı kaydettin ama diff boşsa yanlış klasörde, yanlış dosyada veya dosya zaten aynı durumda olabilir.

Diff'te `+` eklenen, `-` kaldırılan satırı anlatır. Kırmızı satır her zaman kötü, yeşil satır her zaman iyi değildir. Bir yetki kontrolünün kaldırılması tek satırdır ama etkisi büyüktür. İnceleme yaparken satır sayısından önce davranışa bak: bu değişiklikten önce hangi girdi ne sonuç veriyordu, şimdi ne verecek?

```diff
- const limit = 14;
+ const limit = 90;
```

Bu örneği gördüğünde "sayı değişmiş" demek yetmez. Limit gün mü, kayıt sayısı mı, para mı? İzin verilen maksimum mu, varsayılan mı? Sunucuda da aynı sınır var mı? Formdaki maksimumu artırıp sunucuyu değiştirmezsen kullanıcı yeni değeri seçebilir ama kaydedemez.

## Branch ile tek işe odaklanmak

Yeni özelliği doğrudan main üzerinde geliştirmek yerine dal aç. Böylece değişikliği bağımsız inceleyebilirsin. Branch, Git geçmişindeki bir işaretçidir. Dal değiştirince Git çalışma ağacındaki dosyaları o dalın durumuna getirir. Kaydedilmemiş editör sekmesinin bu davranışla nasıl etkileştiğini ayrıca kontrol et.

```powershell
git switch -c feat/deneme-note
'Deneme suresi: 30 gun' | Add-Content README.md
git diff
git add README.md
git commit -m 'docs: deneme suresini acikla'
git switch main
Get-Content README.md
```

Main'e dönünce deneme satırı görünmez; çünkü commit diğer daldadır. Commit dalın geçmişinde durmaya devam eder. `git switch feat/deneme-note` dediğinde satır geri gelir. Henüz commit etmediğin değişiklikler varsa dal geçişi her zaman istediğin gibi gerçekleşmeyebilir; Git bazı geçişleri durdurur. Bu durumda hata mesajını okuyup değişikliği commit etmek veya geçici saklamak arasında bilinçli karar ver.

## Merge ile birleştirmek

Öğrenme deposunda main dalındayken aşağıdaki komutları çalıştır:

```powershell
git status
git merge feat/deneme-note
git log --oneline --graph --all
```

Main başka yöne ilerlememişse fast-forward olabilir: işaretçi mevcut commit'e ilerler. İki dal da farklı commit'ler aldıysa merge commit'i gerekebilir. Komutun başarıyla bitmesi ürün testinin geçtiğini söylemez; yalnız Git'in metinsel geçmişi birleştirebildiğini söyler.

Bir kod incelemesinde birleşebilir durumda olmak, doğru olmak değildir. İki dal farklı dosyaları değiştirse bile sözleşmeyi bozabilir. Biri API alanını `denemeDays` yerine `trialDays` yapar, diğeri eski adı kullanan formu ekler; Git çatışma göstermeden işlevsel hata oluşur.

## Çatışmayı kendin üret ve çöz

Conflict, Git'in aynı bölgedeki farklı değişiklikleri nasıl birleştireceğine karar verememesidir. İki sürümden birini rastgele seçmek çözüm değildir; hedef davranışı belirlemek gerekir. Şu deney yalnız öğrenme deposundaki `title.txt` dosyasında yapılır:

```powershell
git switch -c feat/short-title
'Kisa baslik' | Set-Content title.txt
git add title.txt
git commit -m 'docs: baslik dosyasini ekle'
git switch main
git merge feat/short-title
git switch -c feat/long-title
'Ayrintili baslik' | Set-Content title.txt
git add title.txt
git commit -m 'docs: basligi genislet'
git switch main
'Bakim basligi' | Set-Content title.txt
git add title.txt
git commit -m 'docs: basligi bakima uyarla'
git merge feat/long-title
```

Son komut çatışma üretmelidir. `git status` dosyayı unresolved olarak gösterebilir. `title.txt` dosyasını aç. `<<<<<<<`, `=======`, `>>>>>>>` işaretlerini görürsün. Bunlar ürün kodu değildir; çözüm işaretleridir. İki tarafın niyetini oku, örneğin `Bakim takip sisteminin ayrintili basligi` yaz ve bütün işaretleri kaldır.

```powershell
git add title.txt
git commit -m 'docs: baslik degisikliklerini birlestir'
git status
```

Çözümden emin değilsen ve henüz birleştirmeyi tamamlamadıysan `git merge --abort` devam eden merge'i iptal etmek için kullanılabilir. Birleştirmeye başlamadan önce temiz çalışma ağacıyla hareket etmek, iptalin anlaşılmasını kolaylaştırır. İptal ve silme aynı kavram değildir; hangi işlemin devam ettiğini status ile gör.

## Rebase neyi değiştirir?

Merge iki geçmişi bir araya getirir. Rebase, dalındaki commit değişikliklerini başka bir tabanın üzerine yeniden uygular. Bu işlem commit kimliklerini değiştirebilir. Çizgi daha düz görünür, fakat geçmiş yeniden yazılır. Kendi henüz paylaşmadığın dalında yararlı olabilir; başka insanların dayandığı ortak geçmişte beklenmeyen sor yaratabilir.

Yeni başlayan için güvenli kural: takımın akışını bilmeden paylaşılan branch'i rebase etme ve force push yapma. Rebase sırasında conflict çözülür, dosya seçilir ve `git rebase --continue` denir. Vazgeçmek için devam eden işlemde `git rebase --abort` kullanılır. Rebase'in ne yaptığını öğrenmek, her yerde kullanmak zorunda olduğun anlamına gelmez.

Somut zihinsel model kur: main üzerinde A ve B commit'leri varken sen A'dan C oluşturmuş olabilirsin. Rebase, C'nin değişikliğini B'nin üzerine yeni C' olarak uygular. Yeni commit, eskiyle aynı metni içerse bile farklı ebeveyne sahip olduğundan farklı kimlik alabilir. "Neden SHA değişti?" sorusunun yanıtı yalnız dosya içeriği değildir.

## Geri alma yöntemleri birbirinin yerine geçmez

`git restore dosya` çalışma ağacındaki commit edilmemiş değişikliği seçilen kaynaktaki duruma döndürebilir. Bu, yazdığın kodu kaybettirebilir. `git restore --staged dosya` dosyayı staging alanından çıkarır; normal kullanımda çalışma dosyasını bırakır. `git revert <commit>` ters değişiklik yapan yeni commit oluşturur. Paylaşılmış hatalı değişiklikte çoğu zaman geçmişi yeniden yazmadan ilerlemeyi sağlar.

`git reset --hard` ve `git clean -fd` gibi komutları sor çözme düğmesi sayma. İlki takip edilen yerel değişiklikleri kaybettirebilir; ikincisi takip edilmeyen dosyaları silebilir. Bu kitap bunları uygulama alıştırması olarak kullandırmıyor. Gerçek projede önce status, diff, hedef yol, yedek ve takımın talimatı gerekir. Ne sileceğini bilmiyorsan çalıştırma.

Bir commit'i yanlış dalda oluşturduysan hemen silme. Önce commit SHA'sını kaydet. `git branch rescue/my-work` gibi bir kurtarma dalı mevcut commit'i referans altında tutabilir. Ancak daha karmaşık geçmiş düzeltmelerini kendi çalışma akışını anlamadan kopyalama; zararı düzeltmek için yapılan ikinci acele komut ilkinden daha pahalı olabilir.

## GitHub ile uzak depoya bağlanmak

Remote, uzak depo adresine verilen isimdir. `origin` yaygın bir isimdir; başka bir isim de seçebilirsin. Clone, depoyu yerel bilgisayara alır. Fetch, uzak referansların son durumunu getirir; mevcut çalışma dalını kendiliğinden birleştirmez. Pull ise fetch ile ardından seçili entegrasyon davranışını bir araya getirir. Bu yüzden inceleme yaparken fetch sonrasında farkı okumak daha kontrollü olabilir.

```powershell
git remote -v
git fetch origin
git status
git log --oneline --decorate -5
```

Bu komutlar remote tanımlı bir depoda anlamlıdır. Laboratuvarında remote yoksa `origin` bulunamadı hatası beklenir. Her örneğin önkoşulunu oku. İnternette gördüğün gerçek repo adresini yanlışlıkla kendi projenin remote'u yapma. Public ve private ayrımı, secret yönetiminin yerini tutmaz; private depoya da şifre commit edilmez.

Bir branch'i ilk kez kendi uzak depona gönderirken `git push -u origin feat/deneme-note` kullanılabilir. Bu, paylaşım adımıdır. Burada gerçek hesap veya depo oluşturmak zorunda değilsin; GitHub alıştırmasını kendi eğitim depon hazır olduğunda yap. Kimlik doğrulama yöntemleri ve kurum kuralları değişebilir; şifreni komuta yazmak yerine resmi akışı izlersin.

## Git alıştırma seti

1. Bir metin dosyasında iki değişiklik yap. Yalnız bir dosyayı stage et ve cached diff'i oku. Commit'e girmeyecek başka dosya kaldığını status ile göster.
2. Branch değiştirince dosyanın farklı görünmesini kayıp dosya sanmadan açıkla.
3. Çatışmayı üret, hedef davranışı tek cümleyle yaz, işaretleri kaldır ve çözümü commit et.
4. Kaydet, commit, push, deploy adımlarının her birine ayrı kanıt örneği yaz.
5. Takım arkadaşının kullandığı dalı force push etmeden önce neden durman gerektiğini anlat.

Kaynaklar: [Git switch referansı](https://git-scm.com/docs/git-switch), [Git merge referansı](https://git-scm.com/docs/git-merge), [Pro Git: Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing). Bu bölümdeki bakım sistemi senaryoları ve komut laboratuvarları özgün eğitim örnekleridir.

# GitHub ve kod inceleme disiplini

## Issue, pull request ve review

Issue yapılacak işin veya sorunun kaydıdır. Pull request, bir daldaki değişikliğin başka bir dala alınması önerisidir. Review bu değişikliğin incelenmesidir. Issue sorunu, PR değişikliği, review ise değerlendirmeyi kaydeder. Issue'da "mobil form taşıyor" yazması, çözümün doğru olduğunu söylemez. Pull request'in açılması teslimin incelemeye hazır olduğunu gösterebilir; onay veya canlı yayın değildir.

İyi bir issue, beklenti ve mevcut davranışı ayırır. "Sistem berbat" yerine şunu yaz: "390 px genişlikte yeni firma formundaki Kaydet düğmesi yatay taşmayla ekran dışında kalıyor. Beklenti: yatay kaydırma olmadan görünmesi. Tekrarlama: Firmalar > Yeni firma > formu aç." Görüntü yararlıdır; fakat metinle tekrarlanabilir adım da gerekir. Görüntüdeki gerçek kişisel veriyi kapat.

İyi pull request, neden değiştiğini ve değişikliğin ne yaptığını açıklar. "Düzenleme" başlığı yerine "Mobil firma formunun yatay taşmasını düzelt" yaz. Testleri ayır: "çalıştırıldı ve geçti", "çalıştırıldı ve kaldı", "çalıştırılmadı". Çalıştırmadığın şeyi tahminle yeşil gösterme. Atladığın testin gerekçesini de yaz.

## Küçük bir PR açıklaması yazmak

Örneğin iki sütunlu formu telefonda tek sütuna çevirdin. Açıklama şöyle olabilir:

```text
Sorun:
390 px'te iki sütunlu form yatay taşıyordu.

Değişiklik:
Dar ekranda form tek sütun. Düğmeler tam genişlik.

Doğrulama:
390 ve 1280 px'te form açıldı. Yatay taşma yok.
Klavye ile tüm alanlara ve Kaydet'e ulaşıldı.

Sınır:
Fiziksel iPhone üzerinde çalıştırılmadı.
```

Bu metin kısa ama değerlendirilebilir. "Her şey test edildi" cümlesinden daha çok bilgi verir. Sonradan bir hata çıkarsa hangi iddianın hangi koşulda kurulduğu anlaşılır. Mid-level düzeye yaklaşmak, yalnız kod yazmak değil; tesliminin kapsamını açık anlatabilmektir.

## Base, head ve SHA

PR'ın base dalı değişikliğin alınacağı hedef, head dalı değişikliğin geldiği daldır. SHA, belirli commit'in kimliğidir. Branch adı hareket eder; yeni commit geldikçe aynı branch başka commit'i gösterebilir. Bu nedenle dün incelediğin `feat/deneme-note` ile bugünkü aynı isim aynı içerik olmayabilir.

Bir incelemede `head 51cc6e9 üzerinde` demek kanıtı bir duruma bağlar. Kısa SHA örnek için yeterli olabilir; otomasyon ve kayıt sisteminde tam kimlik daha nettir. Test raporunu başka commit'e aitmiş gibi gösterme. Yeni commit yalnız doküman değiştiriyorsa eski test kanıtının neden yeniden kullanılabildiğini açıklayabilirsin; yeni kod çalıştırılmış gibi konuşamazsın.

Git'te `A..B` ve `A...B` yazımlarının anlamları komuta göre bağlam gerektirir. Özellikle `git diff A...B`, ortak atadan B'ye değişiklikleri görmek için kullanılır. PR'ın gerçek base ve head'ini bilmeden komut seçme. Güncel main ile incelemeye başladığın main farklıysa karşılaştırdığın kapsamı kaydet.

## İncelemeyi nasıl düşünmelisin?

Önce amaç ve kapsamı oku. Sonra değişen dosyaları gözden geçir. Ardından kullanıcıdan sunucuya giden veri yolunu izle. Şu sorular başlangıç için yeterlidir: Girdi nereden geliyor? Kim bu işlemi yapabilir? Hangi veri değişiyor? Başarısız olursa kullanıcı ne görür? Aynı işlem iki kez gelirse ne olur? Başka firmanın kimliği yazılırsa ne olur?

İncelemeyi değişen davranış ve gerekli bağlamıyla sınırla. Değişikliği anlamaya yetecek mevcut bağlamı oku. Örneğin bir form alanı eklendiyse alanın veri dönüştürmesini ve sunucu doğrulamasını incelemek gerekir. İlgili veri akışını takip etmen yeterlidir. Odak dar olmalı; varsayım kör olmamalı.

Görünen davranış ile sunucudaki davranışı karşılaştır. "En az 10 karakter" diyen ön yüzün başka karakter sayımı kullanması, tüm işaretler yeşilken sunucunun reddetmesine neden olabilir. UI testi yalnız işaretlerin yeşil olduğunu kontrol ediyorsa hatayı başarı sayabilir. Testin neyi ölçtüğünü düşünmek, test sayısını artırmaktan daha değerlidir.

## Bulgu nasıl yazılır?

Bulgu en az dört parça taşımalıdır: sor, yer, tekrarlama ve etki. Örneğin "P2: Aynı istek iki kez gönderilince iki ödeme kaydı oluşuyor. Yer: PaymentEndpoints.cs ilgili endpoint. Tekrarlama: aynı requestId ile iki POST gönder. Beklenen: tek kayıt. Gerçekleşen: bakiye iki kez artıyor." Düzeltme önerisi ekleyebilirsin; kanıt yerine öneri yazamazsın.

Öncelik isimleri takım bazında değişebilir. Yaygın bir çalışma modeli olarak P1 ağır üretim/güvenlik/veri kaybı, P2 önemli işlev veya doğruluk sorunu, P3 sınırlı kullanım/görünüm sorunu olabilir. Bu sınıflandırmayı bağlama göre açıkla. Küçük görünen tek satır yetki hatası P1 olabilir; büyük CSS değişikliği yalnız P3 olabilir. Dosya sayısına bakarak risk ölçülmez.

Review yorumunda kişiyi değil değişikliği tartış. "Bunu yazan bilmiyor" çözüm üretmez. "Bu endpoint firma kimliğini request body'den kabul ettiği için oturumdaki firmayı aşabiliyor" teknik olarak tartışılabilir. Kesin değilsen soru sor ama önce kendi okuyabildiğin kodu oku. İyi ekip iletişimi, belirsizliği gizlemek değil küçültmektir.

## Alıştırma: kötü açıklamayı düzelt

Şu açıklamayı incelemeye uygun hale getir: "Bir sürü hata düzeldi. Testler tamam. Artık iyi." Hayali değişiklik: deneme süresi alanı eklendi, varsayılan 30, 0 denemesuz, 180 üst sınır. İki UI testi çalıştırıldı, backend çalıştırılmadı. Açıklaman üç cümle de olabilir; ancak çalıştırılmayan backend'i saklamamalıdır.

Kaynak: [GitHub Docs: Önerilen değişiklikleri incelemek](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request). Buradaki PR ve bulgu metinleri bu kitap için yazılmış örneklerdir.

# HTML: sayfanın iskeletini elle kurmak

## HTML programlama dili midir?

HTML içeriğin anlamını ve yapısını tanımlar. Başlık, paragraf, liste, bağlantı, düğme ve form alanı için uygun elementi seçersin. HTML tek başına "bu işi tamamla ve kaydet" mantığını yürütmez. Fakat yanlış HTML, doğru JavaScript'in kullanımını zorlaştırabilir.

Bir ev benzetmesi kurarsak HTML odalar ve kapılar, CSS görünüm ve yerleşim, JavaScript davranış olur. Benzetmeyi fazla ileri götürme: bu teknolojiler bağımsız dosyalarda dursa da tarayıcıda birbirini etkiler. HTML'deki `name` form verisini, `id` seçim ve etiket bağını, `type` tarayıcı davranışını değiştirebilir.

Etiket, `<button>` gibi yazımdır. Element, bu etiketin temsil ettiği yapısal öğedir. Attribute, elemente eklenen bilgidir: `type="submit"`. Açılış ve kapanış etiketleri çoğu elementte içeriği sarar. `input` gibi void elementler kapanış etiketi almaz. Yanlış iç içe yapı tarayıcı tarafından düzeltilirken senin düşündüğünden farklı DOM oluşabilir.

## İlk tam sayfa

Laboratuvarındaki `web` klasöründe `index.html` oluştur. Kodu bir kez elle yaz. Sonra her satırı kendi cümlenle anlat. Bu örnek henüz sunucuya veri kaydetmez; güvenilir bir arayüz iskeleti kurar.

```html
<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Bakım Takip Laboratuvarı</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header class="site-header">
    <h1>Bakım takip</h1>
    <p>Bugün yapılacak işler</p>
  </header>

  <main>
    <section aria-labelledby="new-job-title">
      <h2 id="new-job-title">Yeni iş</h2>
      <form id="job-form">
        <label for="job-title">İşin başlığı</label>
        <input id="job-title" name="title" required maxlength="80">

        <label for="job-priority">Öncelik</label>
        <select id="job-priority" name="priority">
          <option value="normal">Normal</option>
          <option value="urgent">Acil</option>
        </select>

        <button type="submit">İşi ekle</button>
        <p id="form-message" role="status"></p>
      </form>
    </section>

    <section aria-labelledby="jobs-title">
      <h2 id="jobs-title">Açık işler</h2>
      <ul id="job-list">
        <li>A Blok aylık bakım</li>
        <li>B Blok kapı kontrolü</li>
      </ul>
    </section>
  </main>
</body>
</html>
```

Dosyayı tarayıcıda aç. CSS dosyası henüz yoksa sayfa varsayılan biçimde görünür; bu beklenir. Başlıklar, iki iş satırı ve form bulunmalıdır. Boş başlıkla gönderince tarayıcı doğrulaması uyarabilir. Bu, sunucu doğrulamasının yerini almaz. Kullanıcı tarayıcının kontrollerini atlayarak HTTP isteği gönderebilir.

`lang="tr"` belgenin dilini belirtir. UTF-8 Türkçe karakterlerin yorumlanmasına yardım eder. Viewport mobil sayfanın cihaz genişliğine göre düzenlenmesi için önemlidir. `title` sekmenin başlığı, h1 ise sayfadaki ana başlıktır. Link stylesheet'in göreli yolunu verir. Dosyaların aynı klasörde olduğu varsayımı değişirse yol da değişir.

## Semantik neden işine yarar?

Semantik, öğeyi anlamına uygun seçmektir. İşlem yapan kontrol için button, bir adrese götüren bağlantı için a kullanılır. Tıklanabilen bir div yapmak mümkündür; fakat klavye, odak, rol ve etkinleştirme davranışlarını kendin yeniden kurman gerekir. Yerleşik element doğru başlangıçtır.

`main` sayfanın ana içeriğini, `nav` gezinmeyi, `section` ilişkili bölümü anlatır. Her yere section yazmak otomatik kalite sağlamaz; bölümün anlamlı başlığı olmalıdır. Başlık sıralamasını görsel boyuta göre seçme. Büyük görünmesi için h1 kullanmak yerine doğru yapısal başlığı CSS ile biçimlendir.

Bir tablo gerçek satır-sütun ilişkili veriler için uygundur. Düğmeleri yan yana koymak için table kullanmak düzen ile anlamı karıştırır. Aynı biçimde liste olan veriyi yalnız paragraf yığını yapmak ekran okuyucu ve kullanıcı açısından yapıyı zayıflatır. Doğru element, sonraki CSS ve test kodunu da sadeleştirir.

## id, class, name ve value

`id` belge içinde tekil olmalıdır. Bir etiketi belirli alana bağlamak veya bir öğeyi seçmek için kullanılır. `class` birden fazla öğenin paylaşabildiği sınıftır. CSS'te `.card` gibi seçilir. `name` form verisindeki alan adını belirler. `value` gönderilecek veya kontrolün tuttuğu değerdir. Bu dört kelime birbirinin yerine geçmez.

Örnekte kullanıcı Öncelik listesinde ekranda Acil görür; veri değeri `urgent` olur. Sunucu Türkçe görünen etiketi değil bu değeri bekleyebilir. API sözleşmesi `Urgent` isterken `urgent` gönderirsen davranış kullandığın sunucu dönüştürmesine bağlıdır; büyük/küçük harfi rastlantıya bırakma.

Bir input'un id'si doğru ama name'i yoksa FormData içinde alanı bulamayabilirsin. Label'ın `for` değeri ile input id'si farklıysa etikete tıklamak alanı odaklamaz. İki element aynı id'yi kullanıyorsa seçici beklediğin öğeyi getirmeyebilir. Küçük görünen bu hatalar formdaki veri yolunu doğrudan bozar.

## Kalıcı etiket ve placeholder

Placeholder, alan boşken görünen örnek veya ipucudur. Kullanıcı yazmaya başlayınca kaybolur. Kalıcı label'ın yerini tutmaz. E-posta alanına yalnız `placeholder="E-posta"` eklemek, özellikle ekran okuyucu ve hafıza yükü açısından zayıf tasarımdır. Görsel etiket ve programatik bağ birlikte olmalıdır.

Hata mesajını yalnız kırmızı kenarlıkla anlatma. "İş başlığı gerekli" gibi metin ekle. Gerekirse `aria-describedby` ile yardımcı metni alana bağla. Önce yerleşik HTML davranışlarını kullan; yerleşik HTML doğru kullanıldığında çoğu temel davranış hazır gelir. İlk soru "hangi ARIA?" değil, "doğru element hangisi?" olsun.

## Form düğmelerindeki görünmez varsayım

Form içindeki button için type yazmazsan varsayılan submit davranışı oluşabilir. Şifreyi Göster düğmesine basınca formun gönderilmesi bu nedenle olabilir. İşlem formu göndermemeliyse açıkça `type="button"` yaz. Formun asıl Kaydet düğmesinde `type="submit"` kullan.

Bir formun `submit` olayını ele almak, yalnız Kaydet düğmesinin click olayını ele almaktan daha kapsayıcıdır. Kullanıcı Enter ile de gönderebilir. Davranışı öğrenirken tarayıcı varsayılanını fark et: sayfa yenilendiğinde formun doğal gönderim davranışı gerçekleşmiş olabilir.

## HTML hata laboratuvarı

Örnekte `for="job-title"` değerini `for="job-name"` yap. Etikete tıkla. Odak input'a gelmiyorsa gözlemi yaz. Sonra eşleşmeyi düzelt. İkinci deneyde priority select'in name'ini kaldır. DevTools Console'da aşağıdaki ifadeyi çalıştır:

```javascript
const form = document.querySelector('#job-form');
console.table([...new FormData(form).entries()]);
```

Başlık ve öncelik alanlarının listede olup olmadığını gör. DevTools'a yalnız anladığın kendi kodunu yaz; tanımadığın bir sitenin söylediği uzun script'i yapıştırma. Bu komut yalnız bu eğitim formunun değerlerini okur. İkinci deneyde name'in gönderimle ilişkisini görmüş olursun.

## HTML alıştırmaları

1. Başlığın altına "Tamamlanan işler" bölümü ekle. Yeni başlığın seviyesi ne olmalı?
2. Her işin yanına Tamamla düğmesi koy. Bu düğme formun içinde olacaksa type ne olmalı?
3. Bir adres alanı ekle; label, id ve name bağını kur.
4. Yalnız Tab, Shift+Tab ve Enter kullanarak formu dolaş. Fare olmadan ulaşılamayan kontrol var mı?
5. 80 karakter sınırını ön yüzden kaldırabilen bir istemciyi düşün. Sunucu bu sınırı ayrıca neden denetlemeli?

Kaynak: [MDN: HTML ile içeriği yapılandırmak](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content), [MDN: İlk form](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Your_first_form). Laboratuvar uygulaması rehbere ait özgün örnektir.

# CSS: düzeni ve okunabilirliği kurmak

## CSS seçicisi ne seçer?

CSS bir öğenin nasıl görüneceğini tanımlar. Seçici hedefi bulur; bildirimler özellik ve değerleri belirler. `button { color: white; }` bütün button öğelerini etkiler. `.primary` sınıfı belirli bir grubu, `#job-form` tekil id'yi hedefler. Seçici ile DOM arasındaki bağlantıyı anlamadan CSS eklemek genellikle üst üste yamaya dönüşür.

CSS adındaki cascade, kuralların birlikte nasıl sonuçlandığını anlatır. Kalıtım, kaynak sırası, özgüllük ve importance sonucu etkileyebilir. Her uyuşmazlığı `!important` ile bastırmak kısa vadede işe yarasa da sonraki değişikliği zorlaştırır. DevTools Computed bölümünden hangi kuralın kazandığını bulmak daha öğreticidir.

## Kutu modeli

Her öğeyi bir kutu olarak düşün. İçerik alanı, padding, border ve margin vardır. Padding iç boşluk, margin dış boşluktur. Varsayılan content-box hesabında width içerik genişliği olabilir; padding ve border buna eklenir. `box-sizing: border-box` genişlik hesabını çoğu arayüzde daha öngörülebilir yapar.

Bir karta width yüzde 100 verip iki yanda padding eklediğinde, kutu modeli nedeniyle taşma oluşabilir. Bu yüzden "genişlik 100%, nasıl taşıyor?" sorusunun ilk yanıtlarından biri border-box kontrolüdür. Taşmayı bütün body'ye `overflow-x:hidden` koyarak gizlemek, yanlış hesabı ve erişilemeyen içeriği çözmez.

Örnek HTML'nin yanına `style.css` dosyasını yaz:

```css
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: system-ui, sans-serif;
  line-height: 1.5;
  color: #163b35;
  background: #edf3ef;
}

.site-header {
  padding: 1.5rem;
  color: white;
  background: #163b35;
}

h1, h2, p {
  margin-top: 0;
}

main {
  max-width: 64rem;
  margin: 0 auto;
  padding: 1rem;
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}

section {
  padding: 1.25rem;
  border: 1px solid #ccdad3;
  border-radius: 0.75rem;
  background: white;
  min-width: 0;
}

form {
  display: grid;
  gap: 0.6rem;
}

input, select, button {
  width: 100%;
  min-height: 2.75rem;
  padding: 0.6rem;
  font: inherit;
}

button {
  border: 0;
  border-radius: 0.4rem;
  color: white;
  background: #176348;
  cursor: pointer;
}

button:focus-visible, input:focus-visible,
select:focus-visible {
  outline: 3px solid #c97700;
  outline-offset: 2px;
}

@media (max-width: 44rem) {
  main {
    grid-template-columns: 1fr;
  }
}
```

Geniş ekranda iki kart, dar ekranda tek sütun beklenir. Bu örnek için sınır 44rem seçildi; içerik için seçilmiş bir eşiktir. İçerik nerede bozuluyorsa orada düzeni değiştirmelisin. Ekranın marka modelinden önce gerçek içeriğin sığmasını düşün.

## px, rem, yüzde ve viewport

`px` CSS pikselidir; fiziksel ekrandaki tek noktaya zorunlu olarak eşit değildir. `rem` kök öğenin yazı boyutuna bağlı birimdir. Yüzde, özelliğe bağlı olarak kapsayıcıyla ilişkilidir. `vw` görünüm alanının genişliğiyle ilişkilidir. Hangi birimin neye göre hesaplandığını bilmek, rastgele sayı denemekten daha hızlı sonuç verir.

Yazıyı küçültmek her sığmama sorununu çözmez. Telefon ekranında 6 piksele düşen tarih, teknik olarak taşmıyor olsa da okunmaz. Düğmeyi daraltmak yerine düzeni tek sütuna geçirmek daha doğru olabilir. Form hataları, uzun firma adları, Türkçe metinler ve boş durumlar gerçek yerleşim testinin parçasıdır.

## Flexbox ve Grid arasındaki pratik fark

Flexbox bir satır veya sütun boyunca öğeleri dağıtmak için uygundur. Grid satır ve sütun ilişkisini birlikte kurar. Üst menüdeki düğmeler için flex, iki sütunlu panel düzeni için grid iyi başlangıç olabilir. Fakat ikisini yalnız ezberle seçme; hangi öğelerin birlikte hareket edeceğine bak.

Bir şifre alanının altında kural listesi varsa input ve liste aynı mantıksal gruba ait olmalıdır. Grid içine bağımsız kardeşler halinde eklenirlerse otomatik yerleşim listeyi yan sütuna koyabilir. "Kodda after yazıyor, demek altında" düşüncesi yanlıştır. Görsel yerleşimi DOM sırasıyla birlikte CSS de belirler. CSS layout'unu da okuyabilmelisin.

Örneğin her alanı bir kapsayıcıda toplayabilirsin:

```html
<div class="field">
  <label for="new-password">Yeni şifre</label>
  <input id="new-password" name="newPassword" type="password">
  <p class="hint">En az 10 karakter kullanın.</p>
</div>
```

Bu, input ve açıklamanın aynı grid hücresinde tutulmasını kolaylaştırır. Erişilebilirlik için açıklamaya id ekleyip input'un aria-describedby değerine bağlamak da mümkündür. Kapsayıcı eklerken label ve kontrolün anlam bağı korunmalıdır.

## Responsive tasarım ve taşma deneyi

Responsive tasarım, içeriğin farklı kullanılabilir alanlara uyum sağlamasıdır. Düzeni ara genişliklerde de kontrol ederek geliştirirsin. Tarayıcıyı yavaşça daralt; düzenin hangi aralıkta bozulduğunu gözle. Çok uzun kelime veya e-posta adresi ekle. Boş liste ve yüz satırlı listeyle dene. Düğmenin yüklenirken metni değişince sığıp sığmadığını kontrol et.

Dar ekranda yatay tablo bazen bilinçli olarak kaydırılabilir. Bu durumda bütün sayfayı değil, belirli tablo kabını kaydırmak daha anlaşılırdır. Finans gibi satır-sütun ilişkisi güçlü verilerde kart dönüşümü her zaman en iyi çözüm değildir. Karar, kullanıcı hangi bilgiyi karşılaştıracak sorusuyla verilmelidir.

## CSS hata laboratuvarı

Kartlardan birine kasıtlı olarak `width: 700px` ekle. 390 px görünümde taşmayı gözle. DevTools Elements'te kartı seç, Styles panelinde bu satırı kapat. Taşma kayboldu mu? Sonra sorunu kalıcı dosyada düzelt. DevTools'ta yaptığın geçici değişiklik dosyana otomatik kaydedilmez; sayfayı yenileyince kaybolabilir.

İkinci deneyde `outline: none` ekle ve Tab ile formu dolaş. Nerede olduğunu seçebiliyor musun? Satırı kaldır ve focus-visible kuralını gözle. Görünüm hataları kullanımı da etkiler; bir kontrolün klavyeyle takip edilememesi işi yapmayı engelleyebilir. Erişilebilirlik ayrı son kontrol değil, temel işlev kalitesidir.

## CSS alıştırmaları

1. 390 px'te iki kartı tek sütuna geçir, 1280 px'te iki sütun bırak.
2. Çok uzun bir firma adı ekle. Kartı genişletmeden metnin sarılmasını sağla.
3. Formdaki açıklamaları 12 pikselden daha küçük yapmadan sığdır.
4. Düğme yüklenirken `Kaydediliyor...` yazsaydı düzen değişir miydi?
5. Sadece kırmızı renkle anlatılan hatayı metinle de anlaşılır hale getir.

Kaynak: [MDN: Responsive web design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design). Kutu ve form örnekleri bu rehber için hazırlanmıştır.

# DevTools ile hata ayıklamak

## Hata ayıklama: bir tahmini tek deneyle sınamak

Hata ayıklama bir hipotezi sınama işidir. "Sunucu bozuk" bir hipotez olabilir ama çok geniştir. "Kaydet sırasında oluşan istek 400 dönüyor çünkü priority boş gönderiliyor" daha sınanabilirdir. Önce hatayı tekrar üret. Sonra beklenen ve gerçekleşeni yaz. Ardından tek bir sınırı kontrol et. Aynı anda beş dosyayı değiştirirsen hangi değişikliğin etki yaptığını bilemezsin.

Bir hata notunu şu biçimde tut: ortam, girdi, adımlar, beklenen, gerçek, kanıt, tahmin, deney, sonuç. Ortam derken tarayıcı sürümü gibi her ayrıntıyı ezbere doldurmak gerekmez; davranışı etkileyebilecek bilgiyi yaz. Örneğin yalnız 390 px'te oluşan hata için görünüm genişliği gereklidir; işlemci markası çoğu zaman değildir.

## Elements, Console ve Network

Elements paneli tarayıcının o anki DOM'unu ve stilini gösterir. Kaynak HTML’den farklılaşabilir; JavaScript DOM'u değiştirmiş olabilir. Console hataları, logları ve kendi küçük ifadelerini gösterir. Network ağ isteklerini ve yanıtlarını gösterir. Her panel farklı soruyu yanıtlar.

Örneğin düğme görünmüyorsa Elements'te DOM'da var mı diye bak. Varsa display none, visibility, üstüne binen katman, konum veya boyut sorunu olabilir. DOM'da yoksa render koşulu veya önceki JavaScript hatası olabilir. API isteği başarısızsa Network'teki request ve response önemlidir. Hangi panelin hangi kanıtı verdiğini bilmek zaman kazandırır.

## Breakpoint ve satır satır yürütme

Breakpoint, belirli yerde çalışmayı durdurur. Böylece o andaki değişkenleri inceleyebilirsin. Step over sonraki satıra ilerlerken çağrılan işlevin içine girmez. Step into işlevin içine girer. Step out bulunduğun işlevden çıkar. İsimler aracın diline göre farklı görünebilir; davranışları aynı fikirdir.

Bu küçük dosyayı `debug.js` olarak yaz. HTML'nin body kapanışından önce script etiketiyle bağla. Bu, JavaScript bölümündeki ayrıntılı dil çalışmasına hazırlıktır; burada yalnız akışı izleyeceğiz.

```javascript
function total(items) {
  let result = 0;
  for (const item of items) {
    result += item.price;
  }
  return result;
}

const basket = [
  { title: 'Bakım', price: '100' },
  { title: 'Kontrol', price: '50' }
];

console.log(total(basket));
```

Beklediğin 150 iken metin birleşimi görürsün. Sources panelinde `result += item.price` satırına breakpoint koy. Sayfayı yenile. İlk adım öncesinde result sayı, item.price ise metindir. İlk toplama metin birleştirmeye döner. Sorunu görmeden Number eklemek yerine tür değişimini gözle. Daha sonra veri sınırında doğrulanmış sayısal dönüşüm yapmayı öğreneceksin.

## Console doğru kullanımı

`console.log` kötü araç değildir; her şeyi çözen araç da değildir. Anlamlı etiketi olan küçük loglar kullan. Bir döngüde bin satır log üretmek önemli farkı gizleyebilir. Şifre, token, gerçek müşteri veya ödeme verisi loglama. Geçici tanı loglarını teslimden önce değerlendir.

`console.table` nesne dizisini okumayı kolaylaştırabilir. `typeof` değişkenin temel türünü incelemek için kullanılabilir. Ancak `typeof null` sonucunun `object` olması gibi dil ayrıntıları vardır. Bunları ileride öğreneceksin. Şimdilik araç çıktısını kendi açıklamanla eşleştirmeyi öğren: gördüğün tek kelime, bütün veri modelini anlatmaz.

## Network üzerinden formu takip etmek

Kaydet'e basmadan önce Network listesini temizle. İşlemi bir kez yap. İlgili isteği seç ve şu sırayla bak: URL, metod, durum kodu, gönderilen veri, yanıt. İstek hiç oluşmadıysa olay işleyicisi veya istemci doğrulaması olabilir. İstek oluştuysa artık ağ sınırındasın; sunucu cevabını oku.

400 dönen bir istekte payload'ı beklenen sözleşmeyle karşılaştır. Örneğin sunucu `denemeDays` için sayı isterken `"30"` metni gönderilmiş olabilir. Bazı framework'ler dönüştürür, bazı ayarlarda reddeder. Dönüşüme güvenmek yerine istemcinin ne gönderdiğini bil. Yanıt gövdesindeki hatayı okurken gerçek sırları paylaşmadan küçük örnek oluştur.

Network'te `Preserve log` yönlendirme boyunca kayıtları tutmaya yardım edebilir. `Disable cache` eski dosya şüphesini sınamak için yararlı olabilir. Fakat test ettiğin koşulu kaydet: cache kapalıyken başarılı olması gerçek kullanıcının koşulunda da başarılı olacağı anlamına gelmez. Bir tanı ayarını ürün çözümü diye raporlama.

## Tarayıcı eklentisi ve uygulama hatasını ayırmak

Console'daki her kırmızı satır senin kodundan gelmez. Eklenti, tarayıcı özelliği veya dış kaynak hata yazabilir. Stack trace içinde dosya adını ve çağrı zincirini oku. Gerekirse yeni temiz profil veya eklentisiz ortamda tekrar dene. Ancak bu yöntemi gerçek uygulama hatasını yok saymak için kullanma; karşılaştırmalı deney yap.

Bir hata yalnız belirli hesapta oluşuyorsa hemen o hesabın verisini dışa aktarma. Sentetik veriyle benzer koşulu kurmaya çalış. Gerçek projede kişisel veriye erişim ve log paylaşımı ayrı kurallara tabidir. Öğrenme laboratuvarında bu sorunu sahte başlıklar, sahte e-posta ve yeni veritabanıyla üretmek mümkündür.

## Hata ayıklama oturumu: görünür olmayan liste

Senaryo: İş ekledikten sonra sayfa yenilenene kadar yeni satır görünmüyor. Hipotez A: sunucu kaydetmedi. Hipotez B: sunucu kaydetti ama ön yüz listeyi yenilemedi. Önce POST yanıtını kontrol et. Ardından GET ile listeyi oku. Yeni kayıt GET'te varsa A zayıflar. DOM'da yoksa render/state yolunu incele.

Bu dene sonucu "front-end bozuk" gibi geniş bir cümlede kalmamalı. Daha doğru sonuç şu olabilir: "POST 201 döndü ve sonraki GET kaydı içeriyor. Ancak submit handler state.items dizisini güncellemediği için render eski listeyi kullanıyor." Böyle bir cümle, düzeltilecek yere doğrudan işaret eder.

## Alıştırma: kanıt zinciri

Aynı hayali hata için üç farklı kanıt üret: ekran görüntüsü, ağ kaydı ve kod satırı. Hangisi tek başına neden yeterli değil? Ekran görüntüsü durumu gösterir ama veri kaydedildi mi söylemez. Ağ kaydı yanıtı gösterir ama bütün DOM düzenini anlatmaz. Kod satırı olası mekanmayı gösterir ama o dalın gerçekten çalıştığını her zaman kanıtlamaz. Üçü birlikte daha güçlüdür.

Kaynak: [Chrome DevTools: JavaScript hata ayıklama](https://developer.chrome.com/docs/devtools/javascript). Bu bölümdeki basket ve iş listesi hataları özgün öğretim örnekleridir.

# Çözüm anahtarı ve beceri sınavı

## Dosya ve terminal alıştırmasının çözümü

FullStackLab kökündeyken `Get-Content not.txt`, dosyayı kökte arar. Dosya web içinde olduğu için bulunamaz. `Get-Content ./web/not.txt` doğru göreli yoldur. Mutlak yol, sürücü ve kök dahil tam adresi taşır. Dosya adının büyük/küçük harf farkı, dosya sisteminin duyarlılığına bağlıdır; taşınabilir kodda tutarlı isim kullanmak gerekir.

Doğru çözüm yalnız komutun çalışması değildir. Neden ilk komutun başarısız olduğunu açıklayabiliyorsan hedefi anladın. "Çalışmadı, tekrar denedim" açıklaması eksiktir. Hata ayıklamada rastlantısal başarı ile anlaşılmış başarı arasındaki farkı arıyoruz.

## Ağ alıştırmalarının çözümü

URL örneğinde protokol HTTPS, hedef example.test, port 8443, yol /api/jobs, sorgu page=2, hash details'tır. Hash normal HTTP isteğinde sunucuya gönderilmez. JavaScript 404 ise ilk kontrol HTML'deki script adresi, dosya konumu ve sunucunun statik dosya sunumudur. CSS 200 olması JavaScript'in yüklendiğini kanıtlamaz.

403 sorununu başka firmanın kimliğini yazarak çözmeye çalışmak yetki sınırını aşma girişimidir ve doğru iş akışını öğretmez. Yapılması gereken hesabın rolünü, kaynağın sahipliğini ve endpoint politikasını anlamaktır. Kendi başlattığın iki sunucu port çakıştırıyorsa port dinleyicisini oku, sahip terminali bul ve kendi sürecini Ctrl+C ile durdur. Rastgele PID kapatılmaz.

## Git alıştırmalarının çözümü

Stage etmek, dosyayı diske kaydetmekten farklıdır. `git diff --cached` bir sonraki commit'e girecek farkı gösterir. Başka değişmiş veya untracked dosya status'ta kalabilir. Branch değişiminde commit edilmiş dosyanın farklı görünmesi dalın farklı geçmişi göstermesidir; kayıp değildir.

Conflict çözümü, işaretleri mekanik olarak silmek değildir. İki niyeti okuyup hedef metni oluşturmalı, sonra stage edip commit etmelisin. Paylaşılan branch'te force push, başkalarının dayandığı commit geçmişini değiştirebilir. Takımın onayı ve kurtarma planı olmadan yapılmaz. Merge ve rebase arasındaki farkı çizerek anlatabiliyorsan ezberden bir adım ileri gittin.

Kaydet kanıtı dosyanın yeni içeriği, commit kanıtı yerel git log, push kanıtı uzak branch'teki commit, deploy kanıtı çalışan ortamın sürüm ve davranış doğrulamasıdır. Bunları tek ekran görüntüsüyle topluca olmuş sayamazsın. Bir CI pipeline deploy ediyorsa dahi hangi commit'i hangi ortama kurduğunun kaydı gerekir.

## PR açıklaması alıştırmasının çözümü

Örnek açıklama: "Firma açma formuna deneme süresi eklendi: boş 30 gün, 0 denemesuz, üst sınır 180. İki ilgili UI testi çalıştırıldı ve geçti. Backend testi çalıştırılmadı; sunucu sınırları için henüz koşum kanıtı yok." Bu açıklama ürünün kesin hatasız olduğunu iddia etmez; inceleyen kişiye değerlendireceği açık kapsam verir.

## HTML alıştırmalarının çözümü

Tamamlanan işler ana sayfadaki benzer bir bölümse h2 uygundur; onun içindeki alt konu için h3 düşünülebilir. Tamamla düğmesi mevcut formu göndermeyecekse type=button olmalıdır. Adres alanında label for ile input id eşleşmeli ve formda gönderim için name bulunmalıdır. Örneğin id=address, name=address kullanılabilir; aynı olmak zorunda değiller ama anlaşılır isim iyi başlangıçtır.

Tab sırası normalde DOM sırasını izler. Pozitif tabindex değerleriyle karmaşayı yamamak yerine DOM yapısını düzeltmek çoğu zaman daha doğrudur. Tarayıcının maxlength kontrolü geliştirici araçları veya doğrudan HTTP isteğiyle aşılabilir. Sunucu, kayıt bütünlüğü ve kaynak sınırları için uzunluğu kendi doğrulamalıdır.

## CSS alıştırmalarının çözümü

Media query ile ana grid tek sütuna indirilebilir. Uzun adlar için kapsayıcının min-width davranışını, metin sarmasını ve gerekirse overflow-wrap özelliğini değerlendir. Metni rastgele kesmeden önce kullanıcının bütün adı görmesi gerekip gerekmediğini düşün. Açıklamaları küçültmek yerine düzeni sadeleştirmek, uzun örnek listesini yardımcı metne taşımak veya alanı tam satıra almak daha iyi olabilir.

Kaydediliyor metni düğmenin genişliğini artırabilir. Form grid'i veya flex düzeni bu değişimi kaldırabilmelidir. Hata rengine metin ve gerektiğinde alan bağlantısı eklenir. Her görsel hatada tek bir CSS özelliği çözüm olmaz; ölç, hipotez kur, bir değişiklik yap ve tekrar gözle.

## Kapalı kitap sınavı

Aşağıdaki görevleri önce yardım almadan yap. Ardından resmi belgeleri açabilirsin; bir yazılımcının belge kullanması zayıflık değildir. Ölçmek istediğimiz, neyi neden aradığını bilmen ve sonucu doğrulayabilmendir.

1. Yeni bir eğitim klasörü aç, çalışma yolunu göster, Git başlat ve ilk commit'i oluştur.
2. HTML/CSS dosyalarını boş editörde yeniden yaz. İki bölüm, etiketli form ve iki iş satırı olsun.
3. 1280 px'te iki sütun, 390 px'te tek sütun oluştur. Klavye odağı görünür kalsın.
4. CSS dosya adını yanlış yaz ve Network'te 404'ü bularak düzelt.
5. Bir branch aç, küçük değişiklik yap, diff'i okuyarak commit et ve main'e birleştir.
6. Öğrenme dosyasında conflict oluştur ve niyeti koruyarak çöz.
7. GET ile POST, 401 ile 403, Git ile GitHub farklarını kendi cümlelerinle anlat.
8. Ekran doğru görünürken API'nin neden yine hatalı olabileceğine bir örnek yaz.
9. Küçük bir PR açıklaması ve tekrarlanabilir bir hata bulgusu yaz.
10. Bir işlemin gerçekten test edildiğini söylemek için hangi dosya veya çıktıyı saklayacağını göster.

Her görev için 0, 1 veya 2 puan ver: yapamadım; yardımla yaptım ama açıklayamıyorum; kendim yaptım ve nedenini açıklayabiliyorum. Bu puan meslek unvanı değildir. İlk denemede eksikleri görmek beklenir. 20 üzerinden 16 ve üzeri alıp en az bir hafta sonra aynı görevleri tekrar yapabiliyorsan bu temeller üzerinde sonraki bölümlere güvenle geçebilirsin.

## Kendini kandırmama kontrolü

Kodu kopyaladıktan sonra çalıştırmak ilk adımdır. Ertesi gün boş dosyadan benzerini kurabiliyor musun? Hatalı satırı gösterince neden hatalı olduğunu açıklayabiliyor musun? Değişen gereksinime göre uyarlayabiliyor musun? Yanıt hayırsa konu bitmedi; bu normaldir. Aynı sayfayı tekrar okumak yerine örnekte küçük bir şeyi değiştir ve sonucu tahmin et.

Bir yapay zeka aracından yardım aldığında cevabı sana açıklatmadan teslim etme. Önce kendi hipotezini yaz, sonra araçtan eleştiri iste. Önerilen komut dosya silerse neyi sileceğini, kod yetki kontrolü eklerse hangi isteği reddedeceğini bil. Bu kitapta ilerleme ölçütü sayfa sayısı değil; giderek daha az yardımla doğru soru sorup kanıt toplayabilmendir.
