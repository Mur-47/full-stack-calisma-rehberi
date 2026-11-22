# Bilgiyi beceriye dönüştüren çalışma planı

## Bir haftalık çalışma nasıl görünmeli?

Öğrenme süresini yalnız video veya kitap saatine göre ölçme. Bir hafta boyunca hiç hata görmediysen büyük ihtimalle yeterince bağımsız deneme yapmadın. Önerilen düzen haftada beş çalışma günü, her gün 60-120 dakikadır. İlk 15 dakikada önceki konuyu notsuz hatırla. Sonraki 30-50 dakikada bir küçük özellik yaz. 20 dakikada onu bozan bir girdi üret. Son sürede sonucu deftere ve Git geçmişine kaydet. Hafta sonu 30 dakika ayırıp hangi konuda hâlâ yardım gerektiğini yaz.

Konu zor gelirse takvimi uzat; sıradaki başlığa sırf tarih geldi diye geçme. Hızlı öğreniyorsan da ara sınavı atlama. Önceden programlama bilmeyen biri için 24 hafta bir çalışma iskeletidir, iş garantisi veya seviye sertifikası değildir. Asıl ölçüt kendi yazdığın programın davranışını açıklayabilmen ve yeni bir gereksinime göre değiştirebilmendir.

## İlk sekiz hafta: ekrana gelen şeyi anlayabilmek

**1. hafta - Dosya ve süreç.** Eğitim klasörü kur. Bir metin dosyasını editörden ve terminalden aç. Geçerli klasörü, göreli yolu ve tam yolu açıklayan kısa not yaz. Bir Node sürecini kendi başlattığın terminalde açıp kapat. Başka uygulamanın sürecine dokunma. Teslimin, kullandığın beş komutun amacı ve yanlış klasörde çalıştırıldığında ne olacağıdır.

**2. hafta - Git.** Üç anlamlı commit oluştur. Bir dalda sayfanın başlığını, diğer dalda aynı satırı değiştirip yalnız eğitim deposunda conflict üret. İki değişikliğin niyetini koruyarak çöz. Teslimin ekran görüntüsü değil, okunabilir diff ve neden seçtiğini anlatan commit mesajıdır. `git status` çıktısını kendi sözlerinle açıklayamıyorsan devam etme.

**3. hafta - HTTP.** Bir istek için URL, method, status, headers ve body alanlarını Network panelinden bul. Yanlış adrese istek gönderip 404 ile ağ bağlantısı kurulamaması arasındaki farkı gözle. Teslimin, bir HTTP isteğinin tarayıcıdan sunucuya gidişini anlatan bir sayfalık haritadır.

**4. hafta - HTML.** Başlık, açıklama, bağlantı, liste ve etiketli form alanları içeren bakım talebi sayfası yaz. Yalnız klavyeyle bütün alanlara ulaş. Bir alanın label bağlantısını bilerek boz; sonra düzelt. Teslimin, semantik eleman seçimlerini açıklayan çalışan sayfadır.

**5. hafta - CSS.** Aynı sayfayı 390 ve 1280 pikselde okunur yap. Önce normal akışı, sonra Flexbox veya Grid'i kullan. Sabit genişlik vererek taşma üretip hangi elemanın taşırdığını DevTools ile bul. Teslimin iki genişlikte görüntü ve yaptığın düzeltmenin açıklamasıdır.

**6. hafta - JavaScript temel.** Değişken, koşul, döngü ve fonksiyonlarla işlerin tamamlanma oranını hesapla. Boş liste, tek kayıt ve farklı türden değerler için çıktıyı önce tahmin et. Teslimin en az sekiz giriş/çıkış örneğidir. `"5" + 2` ile `5 + 2` farkını açıklayabilmelisin.

**7. hafta - Nesne ve dizi.** İşleri ada, tarihe ve duruma göre filtrele. Bir nesnenin kopyasını değiştirirken asıl veriyi yanlışlıkla değiştiren bir örnek üret. Yüzeysel kopyanın nerede yetersiz olduğunu anlat. Teslimin çalışan filtre fonksiyonları ve beklenen sonuçları gösteren testlerdir.

**8. hafta - DOM.** Veriden güvenli liste oluştur. Kullanıcı girdisini `textContent` ile göster. Boş durum, yükleniyor durumu ve hata durumunu ayrı çiz. Düğmeye iki kez basınca iki kayıt oluşup oluşmadığını gözle. Teslimin JavaScript'i kapatınca neyin çalışmadığını da açıkladığın küçük arayüzdür.

## İkinci sekiz hafta: veri ve sunucu

**9. hafta - Asenkron düşünme.** Bir yavaş istek ve bir hızlı istek oluştur. Eski yanıtın yeni ekranı bozduğu yarışı tekrar et. AbortController veya istek sürümüyle çöz. Teslimin sorunu önce gösteren, sonra düzeltmeyi doğrulayan iki senaryodur.

**10. hafta - Node.js.** Kitaptaki yerel mini API'yi sıfırdan yeniden kur. `.mjs`, package.json ve npm script farkını anlat. API'ye yanlış JSON, bilinmeyen adres ve yanlış method gönder. Teslimin hangi durumda hangi HTTP yanıtının döndüğünü gösteren tablodur.

**11. hafta - Test.** Bir iş kuralını DOM'dan ayır. Saf fonksiyona en az altı test yaz. Sonra fonksiyonu bilerek bozup doğru testin düştüğünü doğrula. Teslimin test sayısı değil; her testin hangi riski yakaladığını anlatan kısa açıklamadır.

**12. hafta - SQL.** Firma, cihaz ve iş tablolarını eğitim veritabanında kur. Primary key, foreign key ve JOIN kullan. Bir firmanın iş sayısını bul; hiç işi olmayan firmayı kaybetmeden listele. Teslimin sorgular ve hangi satırın neden sonuçta bulunduğudur.

**13. hafta - C#.** Bir JavaScript iş kuralını C# ile yeniden yaz. Tür sisteminin hangi hatayı derlemede yakaladığını, hangi hatayı yakalamadığını göster. Null değer, tarih ve para alanlarını düşün. Teslimin eşdeğer girişlerde iki uygulamanın aynı sonucu verdiği küçük testtir.

**14. hafta - ASP.NET Core.** DTO doğrulaması olan GET ve POST endpoint kur. 201, 400 ve 404 senaryolarını kendin üret. DI ile bir servisi endpoint'ten ayır. Teslimin tek dosyada çalışsa bile sorumluluklarını anlatabildiğin küçük API'dir.

**15. hafta - EF Core.** Aynı küçük API'yi SQLite ile kalıcı yap. Migration üretip SQL'ini oku. Uygulamayı yeniden başlatınca verinin kaldığını doğrula. DbContext'in neden istek kapsamlı olduğunu ve `AsNoTracking` kullanımının amacını açıkla. Teslimin migration, model ve gerçek sorgu davranışıdır.

**16. hafta - Yetki.** Kimlik doğrulama ile yetkilendirme farkını işle. İki hayali firma için izin tablosu yaz. Firma A kullanıcısının firma B kaydına erişimini yalnız düğme gizleyerek değil, sunucuda reddet. Eğitim örneğindeki sahte kimlik seçiminin üretim kimlik sistemi olmadığını açıkça belgelemelisin.

## Son sekiz hafta: bağımsız değişiklik yapabilmek

**17. hafta - Eşzamanlılık.** Aynı kaydın iki kopyasını aç. Birini değiştir, eski kopyayı kaydetmeye çalış. Kayıp güncellemeyi göster ve version kontrolüyle engelle. Teslimin 409 yanıtını tetikleyen yeniden üretilebilir senaryodur.

**18. hafta - Docker.** Kendi öğrenme uygulamandan image oluştur. Container ve image farkını göster. Veriyi volume ile kalıcı tut; yalnız kendi test container'ını yeniden oluşturarak verinin kaldığını doğrula. Volume silmeyi gerektiren bir deney yapacaksan önce hangi veriyi kaybedeceğini yaz ve ayrı boş eğitim volume'u kullan.

**19. hafta - Compose ve proxy.** Öğrenme uygulamasının port haritasını çiz. Host port ile container portunu karıştırınca oluşan hatayı teşhis et. Caddy'yi yerel reverse proxy olarak düşün; internet üzerinde gerçek alan adı veya sertifika kurmaya mecbur değilsin. Teslimin bir isteğin hangi porta gittiğini açıklayan haritadır.

**20. hafta - CI.** Sentetik öğrenme deposunda GitHub Actions ile test çalıştır. Başarılı commit'in tam SHA'sını kaydet. Ardından hatalı bir test ekleyip kontrolün gerçekten kırmızı olduğunu gör. Teslimin bir badge değil, hangi komutun hangi kodu test ettiğinin kanıtıdır.

**21. hafta - Gözlemlenebilirlik ve yedek.** Bir başarısız isteği correlation id veya zaman bilgisiyle logda bul. Sırları loglamadan yeterli bağlam bırak. Sentetik veritabanının yedeğini ayrı klasöre geri yükle ve bir kaydın varlığını doğrula. Teslimin "yedek dosyası var" değil, geri yükleme kanıtıdır.

**22. hafta - Başkasının kodunu okuma.** Daha önce yazmadığın küçük bir endpoint seç. İstek modelinden veritabanı değişikliğine kadar akışı izle. Hiç kod değiştirmeden üç varsayım ve iki test fikri yaz. Teslimin mimari ezber değil; dosya ve fonksiyon bağlantılarıyla hazırlanmış kısa okuma notudur.

**23. hafta - Hata düzeltme PR'ı.** Bitirme projesinden bir hatayı seç. Önce hatayı doğrulayan test veya senaryo kur, sonra en küçük düzeltmeyi yap. İlgisiz dosyaları düzenleme. Teslimin problemi, çözümü ve sınırı açık bir PR açıklamasıdır.

**24. hafta - Kapalı kitap teslimi.** Boş klasörden küçük bir özelliği kur, test et, hata üret, düzelt ve anlat. Yapay zeka ilk taslağı yazmasın. Resmi belgeleri açabilirsin; önemli olan aradığın şeyi bilmen. Teslimini aşağıdaki rubrikle değerlendir. Eksik kalan haftaları tekrar planla.

# Bitirme projesi: iki firmalı bakım masası

## Proje neden küçük tutuluyor?

Bir ürünün bütün ekranlarını kopyalamak öğrenme için iyi bir ilk hedef değildir. Onlarca sayfa, asıl düşünceyi saklayabilir. Bu projede az sayıda ekran olacak ama iş kuralları ve hata durumları gerçekçi olacaktır. Amaç bir ürünü kopyalamak değil, gerçek kod okurken karşılaşacağın kavramları bağımsız bir uygulamada kurmaktır.

Önce tek firmanın işlerini bellekte tutan arayüzü yap. Sonra aynı arayüzü API'ye bağla. Sonra kalıcı veritabanı ekle. En sonda firma sınırı, eşzamanlılık ve testleri ekle. Her aşamada çalışan küçük bir teslim olsun. Böylece hata çıktığında hangi katmanın son değiştiğini bilirsin.

## Veri modeli

Firma için Id ve Name; cihaz için Id, TenantId, Code; iş için Id, TenantId, ElevatorId, Title, Status, DueDate ve Version düşün. İlişkileri kağıtta çiz. Bir işin cihazü başka firmadaysa ne olacağını önce karar ver. Sadece istemcinin doğru seçim yaptığını varsayma. Tarih alanının takvim günü mü, bir an mı olduğuna karar ver; iki anlamı aynı string ile gelişigüzel taşıma.

Kimlik sistemi bu projenin ayrı bir aşamasıdır. İlk yerel deneyde kimliği taklit edebilirsin; bunu dosyada ve README'de açıkça "yalnız yerel öğrenme" diye işaretle. Üretime benzer sürümde kimlik güvenilir oturumdan gelir. İstek gövdesindeki TenantId kullanıcının hangi firmaya ait olduğunu kanıtlamaz. Böyle bir gövdeyi değiştirince erişim sınırı değişiyorsa uygulama güvenli değildir.

## Kabul kriterleri

1. İş listesi açıldığında yükleniyor, boş liste, dolu liste ve hata durumları ayrı görünür.
2. Başlık boş veya belirlediğin sınırdan uzunsa sunucu 400 döner; yalnız HTML required niteliğine güvenilmez.
3. İş eklenince doğru firma ve cihaz ilişkisi kaydedilir; başka firmanın cihaz kimliği reddedilir.
4. Tamamlanmış işin ekranındaki durum, sayfa yenilenince de korunur.
5. Aynı düğmeye iki kez basma senaryosu tanımlıdır: istemci düğmeyi kilitler ve önemli yazma işinde sunucu da tekrarı yönetir.
6. İki eski kopyadan ikinci kayıt, version uyuşmazlığıyla kontrollü reddedilir; ilk değişiklik ezilmez.
7. Firma A hesabı firma B'nin kaydını kimlik değiştirerek okuyamaz, düzenleyemez veya silemez.
8. Kullanıcı girdisi HTML olarak yürütülmez; sıradan metin olarak görüntülenir.
9. 390 pikselde yatay taşma yoktur; etiketler ve hata metni okunur; yalnız klavyeyle temel işlem yapılır.
10. Bir test gerçekten hatalı davranışta başarısız olur; sıfır test çalışması başarı kabul edilmez.
11. Başarısız API isteğinin status ve gövdesi geliştirici tarafından ayırt edilebilir; kullanıcıya teknik sır verilmez.
12. Sentetik yedek başka klasöre geri yüklenerek doğrulanır; sürüm yükseltme ve geri dönme riski belgelenir.

Her kriter için bir kanıt dosyası veya kısa deney notu yaz. Her şeyi ekran görüntüsüyle kanıtlamaya çalışma. Yetki ihlalini bir API testi, taşmayı görüntü, migration geçişini eski şemadan yükseltme testi daha iyi gösterir. Kanıtın türü soruya uygun olsun.

## Teslim dosyaları

README'de amaç, kullanılan sürümler, kurulum, çalıştırma, test, veri konumu ve bilinen sınırlar bulunsun. Kaynak kodu ayrı, derleme çıktısı ayrı olsun. Gizli bilgiler örnek dosyada gerçek değer taşımadan anlatılsın. Git geçmişinde her commit tek niyeti taşısın. Büyük tek commit çalışmayı yasaklamaz ama öğrenirken hangi kararın hangi etkiyi yaptığını kaybettirir.

```text
calisma-projesi/
  README.md
  docs/
    kararlar.md
    hata-gunlugu.md
    kabul-kanitlari.md
  frontend/
  backend/
  tests/
```

Bu klasör şeması bir zorunlu framework düzeni değildir. Kullandığın dile göre proje dosyaları değişir. Node mini API ile ASP.NET Core API'yi aynı endpoint'i aynı portta açacak şekilde birlikte başlatma; biriyle öğrendiğin fikri diğerine taşı. İki backend kullanmak full stack olmanın şartı değildir.

## Değerlendirme rubriği

Altı alana ayrı ayrı 0-4 puan ver: veri akışını açıklama, kod yazma, hata teşhisi, veri/yetki doğruluğu, test tasarımı ve teslim disiplini. Sıfır hiç yapamadığını; bir yalnız kopyalayabildiğini; iki yardımla çalıştırabildiğini; üç bağımsız yapabildiğini; dört ise sınır durumlarını açıklayıp başka birine öğretebildiğini gösterir. Toplam 24 puan mümkündür.

Bir alanın sıfır olduğu toplam puanı başarı sanma. Güvenlik sınırını açıklayamıyorsan güzel arayüz bunu telafi etmez. Testleri anlamıyorsan yeşil sonuç tek başına yeterli değildir. Hedef, en az üç hafta arayla iki kez bütün alanlarda üç veya üzeri performans göstermektir. Bu bile iş hayatındaki bütün orta seviye görevlerini garanti etmez; gerçek ekipte kod incelemesi ve farklı sorunlarla deneyim gerekir.

# Hata avı atölyesi

## Vaka 1: ekran başarılı diyor ama veri kaydolmuyor

İpucu: fetch çağrısından sonra kod doğrudan "Kaydedildi" mesajı veriyor. Network panelinde sunucu 400 dönüyor. Kullanıcı hata mesajını göremiyor.

Çözümü okumadan önce şu soruları yanıtla: İstek gönderildi mi? HTTP yanıtı geldi mi? 400 bir ağ hatası mı? fetch hangi durumda Promise reddeder? UI hangi koşulda başarı gösterebilir? En küçük deney olarak response.ok değerini kaydet ve gövdeyi oku. Sonra mesajı koşullu yap; sunucu doğrulamasını kaldırarak sorunu gizleme.

```javascript
const response = await fetch('/api/jobs', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ title: '' })
});

if (!response.ok) {
  throw new Error(`İstek başarısız: ${response.status}`);
}

console.log('Sunucu isteği kabul etti.');
```

Çözüm ilkesi: HTTP 4xx/5xx yanıtı ile bağlantı kurulamamasını ayrı ele al. Gerçek uygulamada sunucunun güvenli hata açıklamasını kullanıcıya göster; gövdenin her zaman JSON olduğunu varsayma. Testte bir 201 ve bir 400 yanıtı üretip ikisinin aynı başarı akışına girmediğini doğrula.

## Vaka 2: doğru kişi yanlış firmanın kaydını görüyor

İpucu: endpoint, URL'deki kaydı yalnız Id ile arıyor. İstemci listeyi firma filtresiyle gösteriyor, bu yüzden normal kullanımda sor görünmüyor. Fakat başka firmanın Id değeri URL'ye yazıldığında kayıt dönüyor.

Çözüm ilkesi: istemcinin filtresi bir güvenlik sınırı değildir. Sunucu kaydı güvenilir oturumdan gelen firma ve izinli operasyon kapsamıyla birlikte aramalıdır. ORM filtreleri yardımcıdır; açık istisnalar ayrıca değerlendirilir. Testte iki firma oluştur ve A kullanıcısıyla B kaydını doğrudan iste. Güvenlik testi düğmenin gizli olduğuna değil, sunucunun erişimi reddettiğine bakar.

## Vaka 3: tarih bir gün kayıyor

İpucu: kullanıcı 5 Mayıs bakım gününü seçiyor; kod onu UTC anına çevirip sonra başka saat diliminde takvim günü olarak gösteriyor. API alanı tarih mi zaman damgası mı açıkça tanımlanmamış.

Çözüm ilkesi: yalnız takvim günü için DateOnly veya açık `YYYY-MM-DD` sözleşmesi kullan. Bir olayın gerçekleştiği an için UTC zaman damgası ve görüntüleme saat dilimi kullan. Aynı problemi her ekranda saat ekleyip çıkararak çözme. Test girdileri gece yarısı sınırlarını, ay sonunu ve gerekiyorsa saat dilimi dönüşümünü kapsamalıdır. SQLite metin olarak saklıyor diye zamanın anlamı ortadan kalkmaz.

## Vaka 4: geliştirme bilgisayarında çalışıyor, container'da çalışmıyor

İpucu: bağlantı adresi container içinde `localhost` olarak yazılmış. Geliştirici bunun bilgisayarındaki başka servisi gösterdiğini sanıyor.

Çözüm ilkesi: container'ın localhost'u container'ın kendi ağ alanıdır. Compose içindeki başka servis için servis adı ve iç port kullanılır. Host'tan erişimde yayınlanan host portuna gidilir. Önce ağ haritasını çiz, sonra uygulamanın gerçekten dinlediği adresi ve container logunu kontrol et. Her hatayı güvenlik duvarını kapatarak çözmeye çalışma.

## Vaka 5: eski yanıt yeni sayfayı bozuyor

İpucu: A firmasının ekranı yüklenirken B'ye geçiliyor. B hızlı yanıt veriyor; sonra A'nın gecikmiş cevabı aynı DOM alanını dolduruyor.

Çözüm ilkesi: yanıtın hâlâ geçerli ekrana ait olduğunu doğrula. AbortController eski isteği iptal edebilir, ancak zaten tamamlanmış işlerin sırasını da düşünmek gerekir. İstek sürümü veya mevcut seçimle eşleştirme kullan. Hızlı ağda çalışması çözümün doğru olduğunu göstermez; gecikmeleri ters sırada üreterek test et.

## Vaka 6: migration var ama testte kullanılmıyor

İpucu: yeni özellik testinde veritabanı en son modelden doğrudan yaratılıyor. Bu yüzden önceki şemadan yükseltmedeki yanlış SQL veya veri kaybı fark edilmiyor.

Çözüm ilkesi: modelin yeni haliyle çalışması ile eski verinin yeni hale geçebilmesi iki ayrı iddiadır. Sentetik eski şemayı kur, eski kaydı ekle, migration'ı uygula ve hem yeni alanı hem eski kaydın korunmasını doğrula. Canlı veriyi bu deney için kullanma. Geri alma veri kaybettiriyorsa bunu komut açıklamasında açıkça belirt; yedek ve ileri düzeltme stratejisi tasarla.

## Vaka 7: testlerin hepsi yeşil, hata yine var

İpucu: test, davranışı dışarıdan sınamak yerine uygulamadaki aynı yanlış formülü tekrar yazıyor. İki taraf aynı yanlışı yaptığı için test geçiyor.

Çözüm ilkesi: beklentiyi bağımsız bir iş kuralından veya gerçek karşı taraftan üret. Şifre kurallarını tarayıcıda gösteriyorsan, sadece tarayıcı metnini değil sunucudaki gerçek doğrulayıcının aynı örneğe ne dediğini karşılaştır. Para hesabında sınır örneklerini kağıtta hesapla. Tarih aralığında başlangıç dahil mi, bitiş hariç mi kararını açık yaz. Bir testin değeri yalnız yeşil olmasından değil, hangi yanlış uygulamada kırmızı olacağından anlaşılır.

## Vaka 8: yedek var ama geri dönülemiyor

İpucu: dosya her gün kopyalanıyor; kimse ayrı ortamda açmamış. Şifreli yedeğin anahtarı farklı yerde unutulmuş veya uygulamanın beklediği şema sürümü bilinmiyor.

Çözüm ilkesi: yedek bir dosya değil, kurtarma sürecidir. Sentetik ayrı ortamda açılabilen ve anlamlı bir kaydı doğrulanan kopya üret. Sırları yedeğin yanında herkese açık tutma. RPO kaybedebileceğin veri aralığını, RTO toparlanma süresi hedefini anlatır. Bu terimler öğrenme projesine bile şu soruyu sordurur: bugün bilgisayar giderse hangi dosyalarla yeniden çalışabilirim?

# Kod okurken izleyeceğin yol

## Dosyayı baştan sona okumak zorunda değilsin

Bir özellikte önce kullanıcı davranışını tek cümleyle yaz: "Yönetici yeni firma açınca deneme tarihi oluşuyor." Sonra giriş noktasını bul: düğme, form submit olayı veya API endpoint. Verinin şeklini izle: alan adı nedir, boş değer nasıl taşınır, sunucu hangi DTO'ya bağlar? İş kuralını bul: varsayılan nerede seçilir, yetki nerede kontrol edilir? Kalıcı değişikliği ve yanıtı bul. Sonra bu akışın testini ara.

Bu haritayı çıkarmadan projedeki bütün sınıfları ezberlemeye çalışma. Bir dosya adı tanıdık gelmediğinde önce hangi katmana ait olduğunu belirle. `wwwroot` genelde tarayıcı varlıklarını, `Features` işlevsel sunucu parçalarını, `Infrastructure` veri veya dış dünya bağlantılarını taşıyabilir. Klasör adı tek başına güvenlik veya doğruluk kanıtı değildir; gerçek çağrıyı izle.

## Her fonksiyona sorulacak yedi soru

Fonksiyon ne alıyor? Ne döndürüyor? Hangi dış durumu değiştiriyor? Hangi durumda hata üretiyor? Çağıran kişi ne varsayıyor? Aynı anda iki çağrı gelirse ne oluyor? Bunu hangi deneyle doğrulayabilirim? Bu sorulara kısa cevap yazabildiğinde kodu gerçekten okumaya başlamışsındır.

Örneğin bir liste çizme fonksiyonu yalnız HTML mi oluşturuyor, API de çağırıyor mu? Bir EF sorgusu henüz SQL'e dönüşmedi mi, ToListAsync ile veriyi çekti mi? Bir kayıt işlemi SaveChanges'e kadar bellekte mi, yoksa doğrudan SQL ile korumaları atlayan bir yola mı giriyor? Aynı sözcüklerin farklı katmanda farklı anlamı olabilir. "Kaydet" düğmesine basılması veritabanı commit'iyle aynı şey değildir.

## Bir inceleme bulgusunu nasıl yazarsın?

İyi bulgu, yazarın becerisine yorum değil; kodun belirli koşulda ürettiği davranışa kanıttır. Dosya ve satır ver. Beklenen ve gerçek sonucu ayır. Etkilenen kullanıcıyı söyle. En kısa tekrar adımlarını yaz. Düzeltme önerisini kesin çözüm gibi dayatmadan temel sorumluluğu anlat. Şüphe ile doğrulanmış hatayı aynı dille yazma.

```text
Önem: P2
Yer: jobs.js, saveJob içindeki response kontrolü
Beklenen: 400 yanıtında başarı mesajı çıkmamalı.
Gerçek: Boş başlıkla POST 400 dönüyor, ekran Kaydedildi diyor.
Tekrar: Formu aç, başlığı boş gönder, Network'ü kontrol et.
Kanıt: Sentetik API yanıtıyla aynı davranış tekrarlandı.
Öneri: Başarı akışından önce response.ok kontrolü yap.
```

P1/P2/P3 gibi etiketler ekipten ekibe değişebilir. Kendi ekibinde hangi riskin ne anlama geldiğini netleştir. Veri sızıntısını küçük görsel sorunla aynı önemde ele alma. Buna karşılık her görsel tercihi hata diye yazıp asıl riskleri görünmez kılma.

# Terim rehberi: adını duyunca ne düşünmelisin?

## Dil, çalışma ortamı ve uygulama yapısı

- **Dil:** Kodun kuralları ve anlamı. JavaScript ve C# örnektir.
- **Runtime:** Programı çalıştıran ortam. Node.js, JavaScript'i tarayıcı dışında çalıştırır; .NET runtime derlenmiş .NET kodunu yürütür.
- **SDK:** Uygulama geliştirmek için derleyici, komutlar ve ilgili araçlar bütünü. Runtime tek başına geliştirme araçlarının hepsi değildir.
- **Framework:** Uygulamaya yapı ve ortak davranış sunan çatı. ASP.NET Core HTTP uygulamaları için kullanılır.
- **Library:** Belirli iş için çağırdığın kütüphane. Framework ile sınırı her üründe keskin değildir.
- **Frontend:** Kullanıcının etkileştiği arayüz tarafı; tarayıcı verisi güvenilir kabul edilmez.
- **Backend:** Sunucudaki iş kuralları ve erişim sınırları; veritabanı çağrıları sıklıkla buradadır.
- **Full stack:** Bir özelliği arayüzden sunucu ve veri katmanına kadar geliştirebilme alanı.
- **TypeScript:** JavaScript üzerine statik tür denetimi ekleyen dil. Türler derlemede silinir; dışarıdan gelen JSON yine runtime doğrulaması ister.
- **React / Vue / Angular:** Arayüz geliştirme araç ve çatıları. Bu kitabın vanilla DOM bilgisi bunların altında ne olduğunu anlamanı kolaylaştırır; öğrenmenin ilk şartı üçüne birden başlamak değildir.
- **SPA:** Sayfa geçişlerinin önemli kısmını istemcide yöneten uygulama. Sunucu yetkisi ve doğru URL davranışı yine gerekir.
- **SSR:** HTML'in sunucuda üretilmesi. JavaScript kullanımını veya güvenlik kontrolünü kendiliğinden ortadan kaldırmaz.
- **Module:** Kodu dosyalar arasında düzenleme birimi. ESM ile CommonJS aynı sözdizimi değildir.
- **Dependency:** Kodunun veya aracının ihtiyaç duyduğu başka paket ya da hizmet.
- **Package manager:** Paketleri ve bağımlılıklarını kuran araç; npm ve NuGet farklı ekosistemlere hizmet eder.
- **Lock file:** Çözümlenmiş bağımlılık sürümlerini kaydeden dosya. Yeniden üretilebilir kurulum için önemlidir; güvenlik güncellemelerini düşünme işini ortadan kaldırmaz.
- **Build:** Kaynağı çalıştırılabilir veya dağıtılabilir çıktıya dönüştürme işlemi.
- **Bundle:** Tarayıcı varlıklarını işleyip birleştirilmiş çıktıya dönüştüren paketleme yaklaşımı.
- **Lint:** Şüpheli kalıpları ve stil sorunlarını statik kontrolle arama. Çalışma zamanı doğruluğunun yerine geçmez.

## Ağ ve veri sözleşmesi

- **HTTP:** İstemci ile sunucunun istek/yanıt alışverişi için protokol.
- **HTTPS / TLS:** Taşınan verinin bağlantı üzerinde korunmasını sağlayan katman; uygulamanın yetkisini kendiliğinden doğrulamaz.
- **DNS:** Alan adını ilgili ağ adresiyle ilişkilendiren sistem.
- **Port:** Bir makinedeki ağ hizmetinin mantıksal kapısı. Host port ile container iç portu farklı olabilir.
- **Origin:** Tarayıcı açısından scheme, host ve port birleşimi. Aynı site ile aynı origin her durumda aynı şey değildir.
- **CORS:** Tarayıcının farklı origin yanıtlarını JavaScript'e açma kuralları. API yetkilendirmesi değildir.
- **Endpoint:** API'nin belirli bir method/adres işini karşılayan giriş noktası.
- **REST:** Kaynaklar ve HTTP semantiği çevresinde API tasarlama yaklaşımı; yalnız JSON dönmek REST'i tam tanımlamaz.
- **JSON:** Veriyi metin biçiminde taşıma formatı; bir programlama dili nesnesiyle aynı şey değildir.
- **DTO:** Sınırdan taşınan verinin şekli. Veritabanı entity'sini doğrudan API sözleşmesi yapmamak için kullanılır.
- **Validation:** Verinin beklenen biçim ve kurallara uyduğunu denetleme. Yetkilendirmeyle karıştırılmaz.
- **Idempotency:** Aynı mantıksal isteğin tekrarlanmasının ek yan etki yaratmaması özelliği.
- **Pagination:** Büyük listenin parçalara ayrılarak alınması. Sıralama kararlı değilse sayfalar arasında kayıt atlanabilir.
- **Rate limit:** Belirli zaman aralığında iş veya istek sayısını sınırlama. Kimlik ve maliyet modeline uygun tasarlanır.
- **Cache:** Sonucun daha hızlı tekrar kullanılması için saklanması. Yanlış anahtar veya geçersizleştirme eski/başka kullanıcı verisini gösterebilir.

## Veritabanı ve ORM

- **SQL:** İlişkisel veritabanına sorgu ve değişiklik bildiren dil.
- **SQLite:** Dosya tabanlı ilişkisel veritabanı motoru; SQL sorguları, kısıtlar ve transaction desteği sunar.
- **PostgreSQL / SQL Server:** Ayrı sunucu olarak kullanılan ilişkisel veritabanı ürünleri. Taşınırken SQL ve sağlayıcı davranışı farkları incelenir.
- **ORM:** Nesneler ile ilişkisel tablo/veri işlemleri arasında eşleme sağlayan yaklaşım.
- **Entity Framework / EF Core:** Microsoft'un ORM ailesi. EF6 ve EF Core farklı paket ve mimari hatlarıdır.
- **DbContext:** EF Core'da veri erişimi, takip ve bir çalışma birimi çevresinde kullanılan nesne.
- **LINQ:** C# içinde veri sorgularını ifade etme yaklaşımı. Veritabanı sağlayıcısının neyi SQL'e çevirdiğini bilmek gerekir.
- **Migration:** Veritabanı şemasını sürümler arasında değiştirme adımı; veri yedeği değildir.
- **Snapshot:** EF Core migration üretiminde model karşılaştırması için saklanan model görünümü; verinin kendisini içermez.
- **Index:** Belirli erişimleri hızlandıran veri yapısı; yazma ve depolama maliyeti vardır.
- **Transaction:** Bir grup değişikliği birlikte başarı/başarısızlık sınırında ele alma.
- **Concurrency:** Aynı veriye birden fazla işlemin yakın zamanda erişmesi. Yarış koşulları için açık karar gerekir.
- **N+1:** Bir listeyi almak için ana sorgudan sonra her öğe için ek sorgu çalışması kalıbı.
- **Multi-tenant:** Bir uygulamanın birden fazla firmaya hizmet vermesi; firma sınırı yalnız arayüz filtresi değildir.

## Güvenlik, teslim ve operasyon

- **Authentication:** İsteği yapanın kimliğini doğrulama.
- **Authorization:** Doğrulanmış kişinin hangi işi yapabileceğini belirleme.
- **Session:** Kullanıcının giriş durumunu bir süre taşıyan ilişki; sona erme ve iptal davranışı önemlidir.
- **Cookie:** Tarayıcının belirli kurallarla gönderdiği küçük veri. Güvenlik nitelikleri kullanımına göre ayarlanır.
- **JWT:** İmzalı token formatı. İmzalı olması içeriğin şifreli olduğu anlamına gelmez.
- **CSRF:** Kullanıcının tarayıcı kimliğiyle istemediği isteğin tetiklenmesi riski.
- **XSS:** Güvenilmeyen içeriğin kullanıcının sayfasında kod gibi çalışması riski.
- **CSP:** Tarayıcıda içerik kaynaklarını sınırlayan savunma katmanı; güvenli DOM kullanımının yerine geçmez.
- **Hash:** Girdiden özet üretme. Şifre saklamada genel hızlı hash tek başına uygun yöntem değildir.
- **Secret:** Parola, anahtar, token veya benzeri korunması gereken değer; Git geçmişine girerse dosyayı silmek tek başına yetmez.
- **Git:** Dağıtık sürüm kontrol aracı.
- **GitHub:** Git depoları, PR, issue ve otomasyon gibi işbirliği hizmetleri sunan platform.
- **PR:** Değişikliği birleştirmeden önce inceleme ve tartışma önerisi.
- **CI:** Değişiklikler üzerinde otomatik doğrulama çalıştırma süreci.
- **CD:** Kuruma göre sürekli teslim veya sürekli dağıtım anlamında kullanılır; otomatik canlı yayın olup olmadığı açık söylenmelidir.
- **Artifact:** Derleme, rapor veya paket gibi bir süreç çıktısı.
- **Environment:** Development, test, staging ve production gibi farklı çalışma bağlamı.
- **Docker image:** Uygulama ve çalışma gereksinimlerinin katmanlı paket görüntüsü.
- **Container:** Image'dan başlatılan, yalıtılmış süreç ve dosya sistemi bağlamı.
- **Volume:** Container ömründen bağımsız veri tutmak için kullanılan Docker depolama mekanması.
- **Docker Compose:** Birbiriyle ilişkili servisleri bildirimsel dosyayla tanımlayıp yönetme aracı.
- **Reverse proxy:** İstemci isteğini arkadaki uygulamaya ileten sunucu; Caddy bu görevi yapabilir.
- **Observability:** Log, metrik ve trace gibi kanıtlardan sistem davranışını anlayabilme.
- **Rollback:** Bir değişiklikten önceki sürüme dönme. Uygulama dosyası ve veritabanı şeması için geri dönüş planlarını ayrı yap.
- **RPO / RTO:** Kabul edilebilir veri kaybı aralığı ve toparlanma süresi hedefleri.

# Bundan sonra ne öğrenmelisin?

Önce bu kitabın tek bir yığınıyla bağımsız küçük uygulama bitir. Sonra TypeScript ve bir arayüz aracını, örneğin React'i, aynı özellik üzerinde dene. Ardından sunucu tarafında daha büyük SQL motoru, performans ölçümü, erişilebilirlik denetimi ve sistem tasarımı öğren. Her yeni araç için aynı soruyu sor: mevcut hangi sorunu çözüyor, hangi maliyeti ekliyor? Bir sor yaşamadan Kubernetes, microservice veya çok sayıda bulut hizmeti eklemek genellikle öğrenme odağını dağıtır.

Orta seviye geliştirici olma yolunda bir sonraki adım daha fazla terim biriktirmek değil; farklı sorunlar üzerinde aynı düşünme disiplinini tekrar kullanmaktır. Gereksinimi netleştir, verinin akışını çiz, küçük değişiklik yap, sonucu ölç, sınırını yaz ve geri bildirim al. Bu döngüyü bağımsız uygulayabildiğinde kitabın amacı gerçekleşmeye başlamıştır.
