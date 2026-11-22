# Bu kitap nasıl kullanılacak?

## Açık baskı ve hazırlayan

Hazırlayan ve yayımlayan: **Murat AKTAŞ (Mur-47)**. İlk taslak ve düzenleme OpenAI Codex ve alt ajanlarının desteğiyle oluşturuldu. Bu çalışma insan incelemesine ve topluluk düzeltmesine açıktır; bütün kod bloklarının bütün ortamlarda doğrulandığı iddia edilmez. Çalıştırılan kontroller ve sınırlar deponun VALIDATION.md dosyasında açıklanır.

Metin ve PDF CC BY 4.0, özgün kod örnekleri ve betikler MIT lisansındadır. Atıf vererek paylaşabilir ve uyarlayabilirsin. Üçüncü taraf belgeleri ve fontları kendi koşullarına tabidir. Yayın: https://github.com/Mur-47/full-stack-calisma-rehberi . Metin lisansı: https://creativecommons.org/licenses/by/4.0/ .

Bu açık çalışma kitabı, web geliştirmeye temelden başlamak isteyenler için hazırlandı. Hedefi, kullanılan araçların adını ezberlemek değil; bir web uygulamasının isteği nasıl aldığını, veriyi nasıl sakladığını ve sonucu nasıl gösterdiğini anlayarak küçük bir özelliği kendi eliyle geliştirebilmektir. Örneklerin çoğu bakım ve iş takibi çevresindedir. Bütün alıştırmalar uydurma hesaplar ve ayrı öğrenme veritabanları kullanır.

Bir kitabın bitmesi otomatik olarak bir meslek seviyesi kazandırmaz. Orta seviye geliştiricilik, bir problemi parçalara ayırmak, uygun çözümü seçmek, başkasının kodunu okuyabilmek, hata bulmak, test yazmak ve yaptığı değişikliğin sonucunu açıklamakla kazanılır. Bu kitap o beceriler için çalışma zemini verir. Sayfa çevirmek yerine kod yazarsan, her bölümdeki bozuk örnekleri gerçekten teşhis edersen ve bitirme projesini yardımsız kurarsan ölçülebilir bir gelişim elde edersin. Süre kişiye göre değişir; son bölümde 24 haftalık bir çalışma önerisi bulunur.

## Sıfırdan başlamak utanılacak bir şey değil

Yeni bir komutla karşılaşmak öğrenmenin doğal parçasıdır. Ne yaptığını bilmediğin komutu gerçek müşterinin verisinde çalıştırmak sorundur. Bir hata mesajını anlamamak da normaldir. Onu okumadan rastgele ayar değiştirip hangi değişikliğin sonucu etkilediğini kaybetmek ilerlemeyi zorlaştırır. Çalışma sırasında her seferinde üç cümle yaz: Ne bekliyordum? Ne oldu? Bunu hangi küçük deneyle ayırabilirim? Bu alışkanlık, yüz tane araç adına hakim olmaktan daha değerlidir.

Kitap basit dil kullanır; teknik terimleri saklamaz. Önce günlük hayattan bir örnek, sonra gerçek tanım, sonra kod veya komut gelir. Benzetme yalnız ilk kapıdır. Örneğin sunucuyu garsona benzetmek isteğin taşınmasını açıklar ama yetkilendirmeyi, ağ gecikmesini veya aynı anda iki isteğin yarışmasını tek başına açıklamaz. Benzetmeyi anladıktan sonra terimin teknik anlamını öğrenmelisin.

## Önce bir uygulamanın haritası

Bir yönetici tarayıcıda "İşi tamamla" düğmesine bastığında tek bir dosya çalışmaz. Tarayıcı olayını JavaScript yakalar. İstek bir HTTP adresine gider. Sunucu oturumun geçerli olup olmadığını, kullanıcının bu işi değiştirme yetkisini ve gönderilen verinin geçerli olup olmadığını denetler. Veritabanında değişiklik yapılır. Sunucu bir yanıt üretir. JavaScript yanıtı alıp ekranda sonucu gösterir. Ağ koparsa, kullanıcı iki kez basarsa veya iş başka bir kişi tarafından değiştirilmişse ayrıca karar gerekir.

Bu akışın ilk kısmına frontend, sunucu tarafına backend denir. Veriyi uzun süre saklayan katman veritabanıdır. Uygulamayı paketleme, çalıştırma, yedekleme ve izleme işleri operasyon tarafına girer. Full stack geliştirici bunların her birinde çalışabilir; her alanda aynı derinlikte uzman olması gerekmez. Önemli olan aradaki sınırları bilmesidir.

Git dosyaların değişim geçmişini tutar. GitHub bu geçmişi paylaşabileceğin ve değişiklik önerilerini tartışabileceğin bir hizmettir. Docker uygulamayı çalıştırmak için paketler ve yalıtılmış süreçler sağlar. JavaScript bir programlama dilidir. Node.js o dili tarayıcı dışında çalıştıran bir çalışma ortamıdır. C# başka bir dildir; .NET onu ve ilgili kütüphaneleri çalıştıran geliştirme platformudur. ASP.NET Core web uygulaması çatısıdır. EF Core ise C# kodu ile ilişkisel veritabanı arasında çalışan bir ORM aracıdır. Bu cümleleri henüz ezberlemene gerek yok; kitabın sonunda her biriyle küçük bir iş yapmış olman gerekiyor.

## Okuma sırası

İlk kısım bilgisayar, terminal, ağ, Git, GitHub, HTML ve CSS ile zemini kurar. İkinci kısım programlama düşüncesini JavaScript üzerinden öğretir ve Node.js ile küçük bir sunucuya ulaşır. Üçüncü kısım aynı düşüncenin C#, SQL, ASP.NET Core ve EF Core karşılığını gösterir; Docker, Caddy, CI ve yedeklemeyle uygulamayı çalıştırma tarafına bağlar. Son kısım hepsini tekrar kullanacağın bir plan, hata avları ve bitirme projesidir.

İlk kez okuyorsan Docker bölümünden başlayıp JavaScript'e dönme. Çalıştırılan programı ve HTTP isteğini anlamadan container hataları anlamsız görünür. Buna karşılık günlük işte bir terimi arıyorsan içindekilerden veya son terim rehberinden doğrudan bulabilirsin. PDF'de aranabilir metin ve yer imleri bulunur.

## Her ders için beş tur

1. **Oku:** Kavramın hangi sorunu çözdüğünü ve nerede kullanıldığını anla.
2. **Tahmin et:** Kodu çalıştırmadan önce çıktısını kağıda yaz.
3. **Yaz:** Örneği yeni bir dosyaya elle yaz. İlk aşamada kopyalamayı kapat.
4. **Boz:** Bir koşulu değiştir, yanlış bir değer gönder veya bir satırı kaldır. Hatanın ne olacağını önce tahmin et.
5. **Anlat:** Ertesi gün kodu görmeden aynı fikri yeniden kur ve nedenini kendi sözlerinle açıkla.

Kodun harflerini elle yazmak tek başına öğretmez; amaç satırı yazarken kararını düşünmektir. Ne yaptığını anlamadan on sayfa kodu kopyalamak yerine on satırın üç farklı girdide ne üreteceğini açıklamak daha yararlıdır. Bunun için her laboratuvarı küçük tutacağız. İlerledikçe parçalar büyüyecek.

## Çalışma defteri şablonu

Her laboratuvar için aşağıdaki kaydı tut. Bir yazılım hatası birkaç gün sonra tekrar çıktığında en çok bu notlar işe yarar.

```text
Tarih:
Amaç:
Çalıştığım klasör:
Dosyalar / sürüm:
Beklenen sonuç:
Gerçek sonuç:
Hata mesajının en anlamlı satırı:
Hipotezim:
Yaptığım tek değişiklik:
Sonuç:
Sonraki küçük deney:
```

"Çalışmıyor" yerine "POST /jobs isteği 400 dönüyor; gövdede title boş" yazmayı öğren. İkinci cümle sorunu daraltır. Aynı disiplin Git commit mesajını, PR açıklamasını ve ekip içi yardım isteğini de iyileştirir.

## Güvenli çalışma alanı

Alıştırmalar için `Belgeler` altında ayrı bir eğitim klasörü kullan. Kitaptaki farklı laboratuvarlar için alt klasörler aç. Bir Node örneğini .NET klasörünün içine gelişigüzel koyma; iki farklı package.json veya proje dosyası hangi komutun nerede çalıştığını karıştırabilir. Bölümler kendi başlangıç klasörünü söyler. Bütün projeyi tek uygulama sanma; bazı örnekler bir kavramı tek başına göstermek içindir.

```powershell
$studyRoot = Join-Path $env:USERPROFILE 'Documents\YazilimCalisma'
New-Item -ItemType Directory -Force $studyRoot
Set-Location $studyRoot
Get-Location
```

Son komutta gerçekten eğitim klasöründe olduğunu gör. Üretim klasörlerine ve canlı portlara erişmeden bu ayrı alanda çalış. Kitapta geçen ad, e-posta, müşteri ve işler hayalidir. Bir öğrenme projesi oluşturmak için üretim veritabanının kopyasını alma. On tane uydurma satır çoğu kavramı öğrenmeye yeter.

Bir komutun başında `PS>` veya `$` görürsen bu terminal istemi olabilir; dosyanın parçası değildir. Bu kitap kod bloklarında mümkün olduğunca istemi yazmaz. `#` PowerShell'de yorum başlatabilir; URL'de ise fragment anlamına gelebilir. Aynı işaretin bağlama göre farklı görevi olduğunu aklında tut. Terminal hatası ile JavaScript sözdizimi hatasını aynı yerde arama.

## Sürüm, kurulum ve kütüphane gerçeği

Yazılım araçları değişir. Bu kitap 22 Kasım 2026 bağlamında hazırlanmıştır; örneklerin çoğu sürümden bağımsız temellere dayanır. Node.js bölümündeki örnekler modern Node, backend bölümü .NET 10 ve uyumlu EF Core sürümü çevresindedir. Kullanacağın sürümü önce `node --version`, `npm --version`, `dotnet --info`, `git --version` ve `docker version` ile öğren. Kitaptaki bir komut farklı sonuç verirse önce sürümü ve çalışma klasörünü kontrol et; rastgele paket güncelleme.

Kurulum ekranındaki lisans ve yetki gereksinimlerini incele. Docker Desktop masaüstü uygulaması, Engine motor, registry ise imaj deposudur; bulut sunucusu bunları çalıştırabileceğin ayrı bir bilgisayardır. Bu kitabı çalışmak için ücretli sunucu veya yeni bir API anahtarı oluşturman gerekmiyor. Yerel örnekler yeterlidir. Kurumsal kullanım koşulları ve güncel sistem gereksinimleri için araçların kendi belgeleri esas alınır.

## Nasıl yardım isteyeceksin?

Bir kişiye veya yapay zekaya soru sorarken şu beş bilgiyi ver: amaç, en küçük kod parçası, hata metni, beklenen sonuç ve denediğin şey. Şifre, token, gerçek müşteri kaydı veya bağlantı anahtarı ekleme. Logun tamamını yapıştırmak yerine ilgili isteğin zamanını ve hatanın geçtiği kısa bölümü paylaş. Bilgi eksiltirken hatayı gizleme; kişisel veriyi ve sırları çıkar.

İlk isteğin "kodu yaz" olmasın. "Bu üç satırın çıktısını tahmin ettim; neden üçüncü satır farklı?" diye sor. Sonraki aşamada "Bu çözümde hangi varsayım kırılır?" diye sor. Daha sonra kendi PR'ını incelet. Ama önerilen düzeltmeyi anlamadan kabul etme. Bir aracın kendinden emin konuşması, kodunun doğru olduğunun kanıtı değildir.

## Bitirme ölçütü

Bir konuyu öğrendim demeden önce üç kanıt üret: çalışan küçük örnek, örneği bozan bir girdi ve o girdiyi yakalayan kontrol veya test. Git öğrendiğinde conflict çözümü; HTTP öğrendiğinde başarısız istek teşhisi; ORM öğrendiğinde üretilen sorguyu anlama; Docker öğrendiğinde container silinince verinin nerede kaldığını açıklama bu kanıtlara örnektir. Son bölümde bunları birleştiren bir kontrol listesi bulunur.

Bu kitap uygulama ve geri bildirimle ilerleyen bir çalışma rotasıdır. Güçlü bir başlangıç, uygulama ve geri bildirim döngüsüdür. Zorlandığın bölüm, tekrar okuman gereken bir etiket değil; daha küçük bir deney kurman gerektiğini söyleyen işarettir.

## Öğrenme yaklaşımı için kaynaklar

- MDN Curriculum: https://developer.mozilla.org/en-US/curriculum/
- MDN web geliştirmeyi öğrenme: https://developer.mozilla.org/en-US/docs/Learn_web_development
- OWASP geliştirici rehberi: https://devguide.owasp.org/

Bu bağlantılar ileri okuma içindir. Kitabın özgün alıştırmaları, tamamını okuduğunu veya mesleki yeterlilik kazandığını iddia eden bir belge yerine geçmez.
