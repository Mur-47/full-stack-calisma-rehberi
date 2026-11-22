# JavaScript: bilgisayara açık ve sınanabilir talimat vermek

## Bu kısmı nasıl çalışacaksınız?

Bu kitapta kodu görmek, kodu bilmek sayılmaz. Her kısa örneği önce okuyun. Ekrana ne yazacağını bir deftere tahmin edin. Sonra ayrı bir eğitim klasöründe elle yazın, çalıştırın ve tahmininizle karşılaştırın. Yanlış tahmin öğrenme fırsatıdır. Çalışan örneği hiç anlamadan kopyalamak, başkasının çözdüğü matematik sorusunun fotoğrafını çekmek gibidir: elinizde doğru sonuç bulunur ama işlemi siz yapamazsınız.

Buradaki örnekler için yeni bir `FullStack-Calisma` klasörü açın. Bir uygulamanın çalışan kurulumunda, gerçek müşteri verisinde veya canlı sunucuda deneme yapmayın. Bütün firma, iş ve kişi isimleri sentetiktir. Öğrenme programı yalnız kendi bilgisayarınızda çalışacak. Bir örneği kapatmak için o örneği başlattığınız terminalde Ctrl+C kullanın; başka bir uygulamanın sürecini rastgele sonlandırmayın.

Kod blokları birer talimattır. Başında `powershell` yazan blok terminalde, `javascript` yazan blok JavaScript dosyasında kullanılacaktır. Dosya adı belirtilen örnekleri o adla kaydedin. Kod satırlarının sonundaki açıklamalar bilgisayara değil size konuşur. Örneklerin çoğunda satır sonuna noktalı virgül koyacağız. JavaScript bazı noktalı virgülleri kendisi tamamlayabilir; bu, başlangıçta gelişigüzel yazmanız için iyi bir gerekçe değildir.

İlk hedefiniz “JavaScript biliyorum” demek değildir. Şu üç işi yapabilmektir: kısa bir fonksiyonun girdisini ve çıktısını açıklamak, hatalı bir sonucu küçük bir örnekle tekrar üretmek, düzeltmeyi bir testle korumak. Daha sonra bir ekranın tarayıcıdan sunucuya giden bütün yolunu izleyeceğiz.

## Dil, çalışma ortamı ve kütüphane üç ayrı şeydir

JavaScript bir programlama dilidir. Değerleri, değişkenleri, fonksiyonları, döngüleri ve hata kurallarını tanımlar. Tarayıcı JavaScript'i çalıştıran bir ortamdır. Node.js de JavaScript'i çalıştıran başka bir ortamdır. Aynı Türkçe metni telefonda da kâğıtta da okuyabilirsiniz; Türkçe başka, onu taşıyan araç başkadır. JavaScript ile Node.js arasındaki ilişkiyi böyle düşünün.

Tarayıcı pencereyi, belgeyi ve kullanıcının tıklamalarını yönetir. Bu nedenle `document.querySelector` gibi araçlar sunar. Node.js dosya sistemi, süreç ve ağ sunucusu gibi araçlar sunar. Bu nedenle `node:fs` veya `node:http` kullanabilir. Node.js içinde `document` yazmanız bir HTML belgesi oluşturmaz. Tarayıcıda `node:fs` kullanmanız da ziyaretçinin bütün diskini okumanıza izin vermez. Ortamların izinleri ve sundukları API'ler farklıdır.

Bir kütüphane başkasının yazdığı, sizin çağırdığınız kod paketidir. Bir framework uygulamanın iskeletini ve çalıştırma düzenini daha fazla belirler. React, Vue, Express ve benzeri isimleri duyabilirsiniz. İlk aşamada isim biriktirmeyin. JavaScript'in veriyi nasıl değiştirdiğini, HTTP isteğinin nasıl cevaplandığını ve DOM'un nasıl güncellendiğini anlamadan framework ezberlemek, motoru tanımadan otomobil aksesuarı seçmeye benzer.

Node.js yüklüyse terminalde sürümü okuyabilirsiniz:

```powershell
node --version
npm --version
```

Sürüm numaraları makinenize göre değişebilir. Bu bölüm modern ve desteklenen bir Node sürümünü varsayar; projedeki sürüm kuralı her zaman önceliklidir. Hata `node is not recognized` ise JavaScript sözdiziminiz bozuk değildir. Terminal Node çalıştırılabilir dosyasını bulamıyordur. Kurulum ve PATH katmanına bakmanız gerekir. Hatanın hangi katmanda olduğunu ayırmak, hata çözmenin ilk büyük becerisidir.

## İlk program ve programın izlenmesi

`ilk.mjs` adında bir dosya oluşturun:

```javascript
const firmaAdi = 'Örnek Asansör';
const acikIs = 3;
const tamamlananIs = 2;
const toplamIs = acikIs + tamamlananIs;

console.log(firmaAdi);
console.log('Toplam iş:', toplamIs);
```

Terminalde dosyanın bulunduğu klasöre gidip çalıştırın:

```powershell
node ilk.mjs
```

Beklenen çıktı iki satırdır: önce firma adı, ardından `Toplam iş: 5`. Program yukarıdan aşağı ilerler. Önce üç değeri bağlar, sonra toplama yapar, sonra çıktıları üretir. Bilgisayar firma adının ne anlama geldiğini bilmez. Ona verdiğiniz metni saklar. `acikIs` adının iş sayısını anlatması insanlara yardım eder; makine açısından `x` adı da çalışabilirdi. Ancak çalışan kod ile okunabilir kod aynı şey değildir.

Şimdi `tamamlananIs` değerini 7 yapın. Sonucun 10 olacağını çalıştırmadan söyleyin. Ardından `toplamIs` satırını yanlışlıkla `acikIs - tamamlananIs` yapın. Program yine çalışır ama iş kuralı yanlış olur. Buna mantık hatası denir. Yazılımda her yanlış kırmızı hata mesajı üretmez. Bir muhasebe toplamının yanlış olması, uygulamanın çökmesinden daha pahalı olabilir.

Kısa bir programı okurken bir izleme tablosu tutun: “Bu satırdan önce değer neydi, bu satırdan sonra ne oldu?” Özellikle döngü ve koşullarda bu yöntem zihninizde aynı anda çok fazla bilgi tutma yükünü azaltır. Debugger kullanmaya geçince bu tabloyu araç sizin için görünür hâle getirir.

## Değişken, sabit bağ ve değer

Bir değişkeni isim verilmiş bir kutu gibi düşünebilirsiniz. Benzetmenin sınırı şudur: JavaScript'te isim ve değer ilişkisi, özellikle nesnelerde, her zaman kutunun içine fiziksel bir kopya koymak gibi davranmaz. Başlangıç için `const` ve `let` yeterlidir. Yeniden değer atamayacağınız bağı `const`, yeniden atayacağınız bağı `let` ile tanımlayın.

```javascript
const hizmet = 'Bakım';
let bekleyen = 4;

bekleyen = bekleyen + 1;
console.log(bekleyen); // 5
```

`const bekleyen = 4` yazıp sonra `bekleyen = 5` demek hata üretir. `const`, “bu isim başka bir değere bağlanmayacak” demektir. “İçindeki her şey sonsuza kadar değişmez” demek değildir. Bu ayrımı nesneler bölümünde özellikle sınayacağız. `var` eski JavaScript kodunda karşınıza çıkar. Fonksiyon kapsamı ve yeniden tanımlama davranışları yüzünden başlangıç örneklerinde onu kullanmayacağız; eski kod okurken de gördüğünüz her `var`ı düşünmeden değiştirmeyeceksiniz.

İsimlendirme, yorum yazmanın yerine geçen ilk açıklamadır. `t` yerine `toplamKurus`, `d` yerine `sonBakimTarihi`, `x` yerine `firmaId` yazınca yanlış kullanım daha görünür olur. Türkçe anlatıyoruz ama ortak projelerde kod tanımlayıcıları genellikle İngilizcedir. Aynı örneğin İngilizce karşılığı `openJobs`, `completedJobs`, `totalCents` olabilir. Dil seçimi kadar tutarlılık önemlidir.

Bir değişken tanımlı değilse `ReferenceError`, tanımlı olduğu hâlde beklenmeyen biçimde kullanılıyorsa çoğu zaman `TypeError` görürsünüz. Hata isimleri süs değildir. `customer is not defined` ile `Cannot read properties of undefined` aynı olay değildir. İlkinde isim bulunmamıştır; ikincisinde isim bulunmuş ama değerin beklediğiniz nesne olmadığı ortaya çıkmıştır.

## Değer türlerini tanımak

JavaScript'te metin `string`, sayı `number`, doğru/yanlış `boolean` olarak kullanılır. `null` bilinçli boşluğu, `undefined` çoğunlukla değer verilmemiş veya bulunamamış olmayı ifade eder. `bigint` çok büyük tam sayılar için ayrı bir türdür; normal `number` ile gelişigüzel karıştırılmaz. `symbol` daha özel kimlik anahtarları oluşturur. Nesneler, diziler ve fonksiyonlar daha karmaşık yapılar kurmamıza yardım eder.

```javascript
const ad = 'Ada';
const kat = 8;
const aktif = true;
const teknisyen = null;
let sonKontrol;

console.log(typeof ad);          // string
console.log(typeof kat);         // number
console.log(typeof aktif);       // boolean
console.log(sonKontrol);         // undefined
console.log(typeof null);        // object: tarihsel istisna
```

`typeof null` sonucunun `object` olması `null` üzerinde özellik okuyabileceğiniz anlamına gelmez. `null.name` hata verir. Bir dilde tarihsel tuhaflıkların bulunması, her satırı ezberlemeniz gerektiği anlamına da gelmez. Güvenilir birkaç ilke öğrenin ve şüphelendiğiniz davranışı küçük bir örnekle sınayın.

Metin ile sayı farkı önemlidir. HTML formundan alınan bir `input.value` sayı kutusunda bile çoğunlukla metindir. Kullanıcı kutuya 12 yazınca `value` değeri `'12'` olur. Toplama yapmadan önce doğrulama ve dönüştürme gerekir. `typeof` geçici teşhis için yararlıdır; fakat “türü number çıktı, o hâlde her şey geçerli” diyemezsiniz. `NaN` da number türündedir.

## Tür dönüşümü: JavaScript'in sizin yerinize karar vermesini sınırlamak

Coercion, bir işlemin değerleri başka türe dönüştürmesidir. Bazı durumlarda kullanışlı, bazı durumlarda sessiz hata kaynağıdır. Yeni başlayanların sık yaptığı yanlış, toplama işaretinin her zaman aritmetik toplama yapacağını sanmaktır.

```javascript
console.log(10 + 2);     // 12
console.log('10' + 2);   // '102'
console.log('10' - 2);   // 8
console.log(Number('10') + 2); // 12
console.log(Number('')); // 0
```

Son satır iş kuralı açısından tehlikelidir. Boş ücret alanını 0 kabul etmek istemiyorsanız önce boşluğu kontrol etmelisiniz. `Number` dönüştürme yapar; neyin işletmeniz için geçerli olduğuna karar vermez.

```javascript
function tamSayiOku(metin) {
  if (typeof metin !== 'string' || metin.trim() === '') {
    throw new Error('Sayı gerekli.');
  }
  const sayi = Number(metin);
  if (!Number.isSafeInteger(sayi)) {
    throw new Error('Geçerli bir tam sayı yazın.');
  }
  return sayi;
}
```

`Number.isSafeInteger`, tam sayının güvenilir temsil aralığında olup olmadığını da kontrol eder. Bunun anlamını başlangıçta bütün ayrıntılarıyla hesaplamanız gerekmez; “number sonsuz kesinlikli bir hesap makinesi değildir” bilgisini edinmeniz gerekir. Para değerlerini kuruş gibi tam birimlerle taşımak birçok yuvarlama sorununu azaltır. Yine de çok büyük tutarlarda sınır kontrolü ve sunucu tarafında uygun sayı türü şarttır.

`parseInt('12abc', 10)` sonucu 12 olur. Çünkü metnin başında okuyabildiği kısmı alır. Kullanıcının tüm girdisini geçerli saymak istiyorsanız bu, yanlış doğrulama tercihi olabilir. Her dönüştürme işlevinin “toleranslı okuma” mı “tam doğrulama” mı yaptığına bakın. Bir API fiyatı `12abc` olarak kabul ediyorsa hata yalnız ekranda değildir; sunucu doğrulamasının da güçlendirilmesi gerekir.

## Karşılaştırma, doğruluk ve boş değerler

Karşılaştırmada başlangıç kuralımız `===` ve `!==` kullanmaktır. Bunlar değerin yanı sıra tür farkını da dikkate alır. `==` bazı tür dönüşümleri yapar. Eski bir projede `== null` ifadesi bilinçli olarak hem null hem undefined kontrolü için kullanılmış olabilir; onu anlamadan toplu değişiklik yapmayın. Yeni kodda niyetinizi açık yazın.

```javascript
console.log(3 === '3'); // false
console.log(3 == '3');  // true

const fiyat = 0;
console.log(fiyat || 100); // 100
console.log(fiyat ?? 100); // 0
```

`||`, sol değer falsy ise sağ tarafı kullanır. Falsy değerler arasında 0, boş metin, false, null, undefined ve NaN bulunur. `??` ise yalnız null veya undefined durumunda sağ tarafı kullanır. Ücretsiz bir hizmetin fiyatı 0 olabilir. `fiyat || varsayilanFiyat` yazarsanız geçerli sıfırı yanlışlıkla değiştirirsiniz. Bu, gerçek bir faturalandırma hatasına dönüşebilir.

Boş dizi ve boş nesne truthy'dir. `if (liste)` listenin içinde kayıt olduğunu kanıtlamaz. Kayıt sayısını kontrol etmek için `liste.length > 0` kullanın. Nesnenin beklediğiniz alanlarını içerip içermediğini ayrı doğrulayın. “Değer var mı?”, “doğru tür mü?” ve “iş kuralına uygun mu?” üç ayrı sorudur.

## Koşullar ve iş kurallarını yazmak

Bir koşul, programın hangi yolu izleyeceğini seçer. İnsan dilindeki “ödeme tarihi geçtiyse uyar” cümlesini koda aktarırken iki belirsizliği çözmeniz gerekir: hangi saat dilimine göre geçti ve bitiş günü dâhil mi? Sözdizimini öğrenmek, iş kuralını düşünme zorunluluğunu ortadan kaldırmaz.

```javascript
function isDurumu(acikIsSayisi) {
  if (!Number.isInteger(acikIsSayisi) || acikIsSayisi < 0) {
    throw new Error('İş sayısı negatif olamaz.');
  }
  if (acikIsSayisi === 0) return 'Bekleyen iş yok';
  if (acikIsSayisi <= 5) return 'Normal yoğunluk';
  return 'Yoğun';
}
```

Fonksiyondaki erken `return`lar iç içe koşulları azaltır. Her erken dönüşün neyi garanti ettiğini söyleyebilmelisiniz. İlk koşulu geçtikten sonra elimizde negatif olmayan bir tam sayı olduğunu biliyoruz. Sonraki satırlar artık bu bilgiye güvenebilir. Buna önkoşulu doğrulamak diyebilirsiniz.

Çok sayıda durumu karşılaştırırken `switch` okunabilir olabilir. Fakat durumlar birbirinden farklı iş kuralları içeriyorsa her şeyi tek bir dev switch'e yığmak bakımı zorlaştırır. Önce sade bir çözüm kurun, tekrarlar belirginleşince bölün. Daha ilk günden soyutlama yarışına girmeyin.

## Döngüler: aynı işlemi farklı kayıtlar için yapmak

Bir asansör firmasının 50 açık işi varsa her biri için elle 50 satır yazmazsınız. Döngü, bir işlemi birden fazla kayıt üzerinde yürütür. Önce `for...of` ile başlayın; “dizideki her iş için” diye okuyabilirsiniz.

```javascript
const isler = ['Bakım', 'Arıza', 'Kontrol'];

for (const is of isler) {
  console.log('Sıradaki:', is);
}
```

Bir sayacı izlemek gerektiğinde klasik `for` uygundur:

```javascript
for (let sira = 0; sira < 3; sira += 1) {
  console.log(sira);
}
// 0, 1, 2
```

Dizilerin ilk indeksi 0'dır. Uzunluğu 3 olan bir dizinin son geçerli indeksi 2 olur. Bu nedenle `i <= dizi.length` yazmak genellikle son adımda dizinin dışına çıkar. Bu hataya off-by-one denir. “Bir eksik veya bir fazla” sınır sorunudur. Takvim, sayfalama ve günlük raporlarda da aynı düşünme hatası farklı görünür.

`while` koşul doğru olduğu sürece çalışır. Koşulun değişmesini sağlamazsanız sonsuz döngü oluşturabilirsiniz. Tarayıcıda uzun bir senkron döngü, düğmelerin tepki vermemesine yol açar. Bu durumda ağınız bozuk olmayabilir; ana JavaScript işi bitmediği için ekran yeni olaya cevap veremiyordur.

## Fonksiyon: adı olan küçük bir iş

Fonksiyonu bir makine gibi düşünün: girdi alır, kurala göre işlem yapar ve bazen sonuç döndürür. Aynı işlemi tekrar kullanmanızı sağlar. Daha önemlisi, karmaşık problemi adı olan küçük parçalara ayırır. `hesapla` gibi belirsiz isim yerine `gecikenIsleriSec` gibi niyet anlatan isim tercih edin.

```javascript
function kdvDahilKurus(netKurus, oran) {
  if (!Number.isSafeInteger(netKurus) || netKurus < 0) {
    throw new Error('Net tutar geçersiz.');
  }
  if (!Number.isFinite(oran) || oran < 0 || oran > 1) {
    throw new Error('Oran 0 ile 1 arasında olmalı.');
  }
  return Math.round(netKurus * (1 + oran));
}

console.log(kdvDahilKurus(10000, 0.20)); // 12000
```

Bu örnek bir eğitim hesabıdır; vergi mevzuatı veya tüm ticari yuvarlama kurallarının modeli değildir. Teknik olarak dikkat edeceğiniz şey, fonksiyonun aldığı birim ve döndürdüğü birimdir. Girdi kuruş, çıktı kuruş. Aynı projede bir yerde TL, başka yerde kuruş kullanıp isimlerde bunu saklarsanız yüz katlık hata üretebilirsiniz.

Parametre, fonksiyonun tanımındaki isimdir; argüman, çağırırken verdiğiniz değerdir. `netKurus` parametre, `10000` argümandır. `return` fonksiyondan sonuç çıkarır. `console.log` yalnız bir çıktı yazar. Bu ikisi sık karıştırılır:

```javascript
function yanlisTopla(a, b) {
  console.log(a + b);
}

const sonuc = yanlisTopla(2, 3);
console.log(sonuc); // undefined
```

İlk satırda 5 görmeniz fonksiyonun 5 döndürdüğünü göstermez. Fonksiyonun başka bir yerde hesap için kullanılmasını istiyorsanız `return a + b` yazın. Sonra sonucu ister ekrana basın, ister başka fonksiyona verin. Hesabı ve gösterimi ayırmak test yazmayı kolaylaştırır.

Ok işlevi, yani arrow function, daha kısa bir yazımdır:

```javascript
const ikiKat = sayi => sayi * 2;
const carp = (a, b) => a * b;
```

Tek ifade varsa sonucu örtük döndürür. Süslü parantez açarsanız çoğunlukla açık `return` gerekir. Arrow function'ın kendi `this` bağının olmaması gibi önemli farkları vardır. Başlangıçta “her fonksiyon aynı, yalnız kısa yazılıyor” diye ezberlemeyin. Sade hesaplarda kısa yazımı, nesne yöntemi ve bağlam gerektiren kodda açık niyeti tercih edin.

## Scope ve closure: isimler nerede görünür?

Scope, bir isme kodun hangi bölgesinden erişilebildiğidir. Dışarıdaki bir odadan içerideki kapalı çekmeceyi göremezsiniz. Fonksiyonun içinde tanımlanan bir değişken genellikle o fonksiyonun dışından doğrudan okunamaz. Bu, kodun birbirine istemeden müdahale etmesini azaltır.

```javascript
function sayacOlustur() {
  let sayi = 0;
  return function artir() {
    sayi += 1;
    return sayi;
  };
}

const birinci = sayacOlustur();
const ikinci = sayacOlustur();
console.log(birinci()); // 1
console.log(birinci()); // 2
console.log(ikinci());  // 1
```

Dış fonksiyon tamamlandıktan sonra iç fonksiyonun `sayi` değişkenine erişmesi closure örneğidir. İç fonksiyon, oluşturulduğu çevredeki bağlara erişimini korur. Her `sayacOlustur` çağrısı ayrı bir çevre oluşturur. Bu nedenle ikinci sayaç birincinin kaldığı yerden başlamaz.

Closure bir sihirli önbellek değildir. Olay dinleyicileri, gecikmeli işler ve modüllerde karşınıza çıkar. Bir düğmenin eski firma kimliğini hatırlaması da closure ile ilgili olabilir. Güncel olması gereken bilgiyi fonksiyon oluşturulurken sabitlediyseniz, sonradan kullanıcı başka firmaya geçince eski değeri kullanabilirsiniz. Böyle bir hatada “ekrandaki isim doğru ama istek yanlış firmaya gidiyor” belirtisi oluşur.

Okurken şu soruyu sorun: Bu fonksiyon çağrıldığı anın değerini mi kullanıyor, yoksa oluşturulduğu çevrede tutulmuş bir değeri mi? Ardından verinin değişebilir olup olmadığını kontrol edin. Özellikle asenkron kodda değişkenin zaman içindeki yaşamı, tek bir satırın anlamından daha önemlidir.

## Diziler: kayıt listeleriyle çalışmak

Dizi sıralı bir değer koleksiyonudur. Bir ekranın iş listesi, sunucunun döndürdüğü müşteri kayıtları veya bir filtre grubu dizi olabilir. Dizideki kayıtlar nesne olduğunda gerçek uygulamalara yaklaşırız.

```javascript
const isler = [
  { id: 1, tur: 'Bakım', tamamlandi: false },
  { id: 2, tur: 'Arıza', tamamlandi: true },
  { id: 3, tur: 'Bakım', tamamlandi: false }
];

const aciklar = isler.filter(is => !is.tamamlandi);
const basliklar = aciklar.map(is => `${is.id}: ${is.tur}`);
const bulunan = isler.find(is => is.id === 2);

console.log(aciklar.length); // 2
console.log(basliklar);      // ['1: Bakım', '3: Bakım']
console.log(bulunan.tur);    // Arıza
```

`filter` uygun kayıtları seçer. `map` her kaydı başka bir değere dönüştürür. `find` ilk uygun kaydı bulur; bulamazsa undefined döner. `some` en az bir kaydın, `every` bütün kayıtların koşula uyup uymadığını söyler. `reduce` bir diziyi tek sonuçta biriktirmek için kullanılabilir. Bu isimleri ezberlemek yerine her birini bir defa klasik döngüyle kendiniz yazın. Sonra kısa sürümün ne yaptığını daha iyi anlarsınız.

```javascript
const toplam = isler.reduce((adet, is) => {
  return adet + (is.tamamlandi ? 1 : 0);
}, 0);
console.log(toplam); // 1
```

`reduce` başlangıç değerini yazmak, boş dizi davranışını daha açık yapar. Başlangıç değeri vermeden yazılan bazı biriktirmeler boş listede hata verir. “Liste hep dolu gelir” varsayımı, gerçek uygulamada ilk kullanıcı geldiğinde kırılabilir. Boş liste, tek kayıt, çok kayıt ve beklenmeyen türler testinizin ayrı örnekleri olmalıdır.

`sort` varsayılan olarak metin sıralamasına göre davranır ve diziyi değiştirir. Sayıları sıralarken açık karşılaştırma yazın:

```javascript
const katlar = [2, 10, 1];
const sirali = [...katlar].sort((a, b) => a - b);
console.log(sirali); // [1, 2, 10]
console.log(katlar); // [2, 10, 1]
```

Buradaki yayma işaretiyle yeni dizi oluşturduk. İçindeki değerler basit sayılar olduğu için bu kopya ihtiyacımızı karşılıyor. İç içe nesnelerde durum farklıdır.

## Nesneler, referanslar ve kopya hataları

Nesne, isimli alanları bir arada tutar. `musteri.name` ifadesi o nesnenin name alanını okur. Nesnenin alanlarını değiştirebilirsiniz. İki değişken aynı nesneyi gösteriyorsa birinden yapılan değişiklik diğerinden de görünür.

```javascript
const ilk = { name: 'Örnek Site', address: { city: 'Ankara' } };
const ayni = ilk;
ayni.name = 'Yeni Site';
console.log(ilk.name); // Yeni Site

const yuzeysel = { ...ilk };
yuzeysel.address.city = 'İzmir';
console.log(ilk.address.city); // İzmir
```

`const ilk` ifadesi nesnenin alanlarını dondurmadı. Yalnız `ilk` bağının başka bir nesneye atanmasını engelledi. `{ ...ilk }` yeni bir dış nesne oluşturdu ama içteki address nesnesini derin kopyalamadı. Buna shallow copy, yani yüzeysel kopya denir.

Bir düzenleme formu açarken asıl kaydı doğrudan forma bağlayıp kullanıcı yazdıkça onu değiştirirseniz, Vazgeç düğmesi gerçek bir vazgeçme yapmayabilir. Henüz sunucuya kaydetmediğiniz hâlde listedeki nesneyi değiştirmiş olabilirsiniz. Eğitim için iç içe alanları ayrı kopyalayabilirsiniz:

```javascript
const taslak = {
  ...ilk,
  address: { ...ilk.address }
};
```

`structuredClone` pek çok yapı için derin kopya sağlayabilir; fakat her değeri kopyalayamaz ve onu iş modeli tasarımının yerine kullanmamalısınız. JSON'a çevirip geri okumak da genel amaçlı kusursuz kopya değildir: undefined alanlar kaybolabilir, tarih nesneleri metne dönüşebilir ve bazı türler desteklenmez. Önce hangi veriyi, hangi amaçla kopyaladığınızı belirleyin.

Destructuring, nesneden alanları kısa yoldan almaktır:

```javascript
const is = { id: 7, title: 'Aylık bakım', done: false };
const { id, title } = is;
console.log(id, title);
```

Bu, nesneyi parçalayarak yok etmez. Alan değerlerini yeni bağlara alır. `const { address } = ilk` dediğinizde address hâlâ aynı iç nesneyi gösterebilir. Yazımın kısa olması, referans kurallarını değiştirmez.

## JSON: nesnenin ağdan geçebilen metin biçimi

JavaScript nesnesi çalışan programın içindeki değerdir. JSON ise veriyi metin olarak taşıyan bir biçimdir. İsimleri benzer olduğu için “JSON nesnesi” deyimi yaygındır ama ağdan gelen gövde önce bayt ve metindir; onu ayrıştırdıktan sonra program içinde değer elde edersiniz.

```javascript
const kayit = { id: 1, title: 'Bakım', done: false };
const metin = JSON.stringify(kayit);
const tekrar = JSON.parse(metin);
console.log(metin);
console.log(tekrar.title); // Bakım
```

JSON içinde fonksiyon taşımazsınız. Tarih genellikle bir metindir; `JSON.parse` onu otomatik Date yapmaz. `JSON.parse` işleminin başarılı olması da verinin uygulamanız için geçerli olduğunu kanıtlamaz. `{ "title": 72 }` geçerli JSON'dur ama başlık alanını metin bekleyen API için geçersiz girdidir.

Güven sınırını burada kurun. Kullanıcıdan, dosyadan veya ağdan gelen veriyi önce şekil ve sınır açısından doğrulayın. Kayıt adının metin olması, uzunluğunun uygun olması, kimliğin beklenen biçimde olması ayrı kontrollerdir. Güvenlik, yalnız parolaları gizlemekten oluşmaz; yanlış biçimli verinin sistemin içinde ne kadar ilerleyebileceğini sınırlamak da güvenliktir.

## Hatalar: beklenen başarısızlık ile programcı hatası

Bir fonksiyon her zaman başarılı olmayabilir. Kullanıcı alanı boş bırakabilir, ağ kopabilir, sunucu 500 döndürebilir veya sizin kodunuz yanlış değişken okuyabilir. `try/catch` bu durumları ele almak için kullanılır. Ancak bütün hataları yutup “işlem başarılı” yazmak hata yönetimi değildir; hatayı görünmez kılmaktır.

```javascript
try {
  const veri = JSON.parse('{ bozuk json }');
  console.log(veri);
} catch (error) {
  console.error('Veri okunamadı:', error.message);
}
```

Bir catch içinde yalnız `console.log` yapıp devam ederseniz çağıran kod başarısızlığı öğrenemeyebilir. Bazı katmanlarda hatayı dönüştürüp yeniden fırlatmak gerekir. Kullanıcıya anlaşılır mesaj gösterirken geliştiriciye güvenli teşhis bilgisi bırakın. Parola, oturum çerezi, erişim token'ı ve gerçek müşteri içeriğini loga yazmayın.

`finally`, başarı veya hata sonrasında yapılması gereken temizliği taşır. Kaydet düğmesini tekrar etkinleştirmek iyi bir örnektir. Bir hata oluşunca düğmenin sonsuza kadar kilitli kalması, asıl hataya ek bir kullanım sorunu yaratır.

```javascript
saveButton.disabled = true;
try {
  await saveRecord();
} catch (error) {
  showMessage('Kayıt yapılamadı. Tekrar deneyin.');
} finally {
  saveButton.disabled = false;
}
```

Bu blok tek başına bir dosya değildir; bir formun olay işleyicisinin içinden alınmış örnektir. Kitaptaki parça kod ile tam program ayrımını takip edin. Eksik bağlamı olan bir parçayı boş dosyaya yapıştırıp `saveButton is not defined` görmek beklenir. Kodun hangi ortam ve değişkenlerle çalıştığını bilmek, okumanın bir parçasıdır.

# Tarayıcı JavaScript'i: ekrandaki formdan güvenli DOM'a

## DOM, HTML metninin çalışan ağaç hâlidir

Tarayıcı HTML'yi okuyup bellekte bir belge ağacı oluşturur. JavaScript bu ağacın düğümlerini bulup değiştirebilir. HTML dosyasındaki kaynak ile anlık DOM her zaman aynı değildir; kullanıcı işlem yaptıkça veya kod yeni eleman ekledikçe DOM değişebilir. DevTools Elements görünümü anlık yapıyı incelemenizi sağlar.

```html
<h1>İşler</h1>
<p id="summary">Henüz yüklenmedi.</p>
<button id="refresh" type="button">Yenile</button>
<script type="module" src="./app.mjs"></script>
```

```javascript
const summary = document.querySelector('#summary');
const refresh = document.querySelector('#refresh');

refresh.addEventListener('click', () => {
  summary.textContent = 'Liste yenilendi.';
});
```

`querySelector` eleman bulamazsa null döner. Ardından `null.addEventListener` çağırmak hata üretir. Yanlış id, betiğin belge oluşmadan çalışması veya yanlış sayfada çalıştırılması muhtemel nedenlerdir. İlk tepkiniz rastgele `setTimeout` eklemek olmasın. Önce Elements'te id gerçekten var mı, Network'te script yüklenmiş mi, Console'daki ilk hata ne diyor bakın.

Olay dinleyicisi eklemek, olayın o anda gerçekleştiği anlamına gelmez. Fonksiyonu tarayıcıya kaydedersiniz; kullanıcı tıklayınca çağrılır. `addEventListener('click', kaydet())` yazarsanız fonksiyonu hemen çalıştırıp dönüş değerini verirsiniz. Genellikle istediğiniz `addEventListener('click', kaydet)` veya bir ok işleviyle çağrıyı ertelemektir.

## Kullanıcı metnini HTML gibi çalıştırmayın

Bir iş başlığını ekrana yazarken `textContent` kullanmak, başlığın metin olarak gösterilmesini sağlar. `innerHTML` ise verdiğiniz metni HTML olarak yorumlar. Kullanıcının girdiği metni HTML içine yapıştırmak XSS gibi ciddi sorunlara yol açabilir. Birinin başlığa `<img ...>` benzeri içerik yazabileceğini düşünün; “bizim kullanıcı öyle şey yapmaz” güvenlik sınırı değildir.

```javascript
function jobItem(job) {
  const li = document.createElement('li');
  const title = document.createElement('strong');
  title.textContent = job.title;
  li.append(title);
  return li;
}
```

Bu örnekte hem yapıyı biz oluşturduk hem metni ayrı verdik. `innerHTML` her kullanımda yanlış değildir; sabit, geliştiricinin denetimindeki şablonlarda tercih edilebilir. Fakat dışarıdan gelen verinin HTML'ye nerede karıştığını açıkça bilmelisiniz. Güvenilir temizleme ve izinli etiket modeli gerektiren zengin metin ayrı bir problemdir; başlangıçta ona ihtiyaç yoksa düz metin tercih edin.

Bir bağlantının `href` değerini kullanıcı verisinden alıyorsanız yalnız textContent yeterli değildir. URL protokolü de önemlidir. Benzer şekilde resim adresleri, dosya yolları ve CSS değerlerinin her biri kendi bağlamına göre değerlendirilir. “Metni escape ettim, artık bütün bağlamlarda güvenli” düşüncesi yanlıştır.

## Form okumak: doğrulama tarayıcıda başlar, sunucuda biter

Bir formun `submit` olayı hem düğmeyle hem Enter ile tetiklenebilir. Yalnız düğmenin click olayını dinlerseniz klavye kullanımını kaçırabilirsiniz. Form submit olayını dinleyip `event.preventDefault()` ile varsayılan sayfa gönderimini durdurmak yaygın bir yöntemdir.

```javascript
const form = document.querySelector('#job-form');

form.addEventListener('submit', async event => {
  event.preventDefault();
  const fields = new FormData(form);
  const title = String(fields.get('title') ?? '').trim();
  if (title.length < 3) {
    showMessage('Başlık en az 3 karakter olmalı.');
    return;
  }
  await createJob({ title });
});
```

`required`, `minlength`, `maxlength` ve uygun input türleri kullanıcıya erken yardım sağlar. Kullanıcı bunları DevTools'tan silebilir veya arayüzü hiç kullanmadan API'ye istek gönderebilir. Bu nedenle sunucu aynı temel doğrulamaları kendisi yapmalıdır. Arayüzde yönetici düğmesini gizlemek de sunucunun yetki denetiminin yerine geçmez.

Bir şifre kural listesinin bütün maddeleri yeşilken sunucunun parolayı reddetmesi, arayüz ve sunucunun aynı kavrama farklı anlam verdiğini gösterebilir. “Harf”, “rakam”, “karakter sayısı” gibi basit görünen kelimeler Unicode ve kullanılan doğrulayıcıya göre farklı sonuç verebilir. Kuralı iki yerde yazıyorsanız aynı örneklerle iki tarafı karşılaştırın. Kullanıcıya yardım eklerken yanlış bir güven duygusu üretmeyin.

## Event delegation ve dinamik elemanlar

Ekrana sonradan eklenen düğmelere, sayfa ilk açılırken seçtiğiniz eski düğme listesi otomatik olarak dinleyici eklemez. Her render sonrası tekrar bağlamak mümkündür ama dikkatsiz yapılırsa bir tıklama iki kayda dönüşebilir. Alternatif yöntem olayın ortak üst elemanda ele alınmasıdır.

```javascript
const list = document.querySelector('#jobs');

list.addEventListener('click', event => {
  const button = event.target.closest('button[data-id]');
  if (!button || !list.contains(button)) return;
  completeJob(Number(button.dataset.id));
});
```

Olayın içteki bir span'den gelmesi durumunda `closest` ilgili düğmeyi bulur. `contains` seçilen düğmenin gerçekten bu listenin altında olduğunu doğrular. Bu yönteme event delegation denir. Her durumda şart değildir; basit ekranlarda düğme oluşturulurken bir dinleyici eklemek de temizdir. Seçiminizi sorunla ilişkilendirin.

MutationObserver DOM'a yeni düğüm eklenmesini izleyebilir. Ancak “her değişiklikte bütün belgeyi baştan tara” yaklaşımı büyük ekranlarda gereksiz iş oluşturabilir. Gözlemcinin kendi eklediği elemanlar yeni değişiklikler üretir. Bu nedenle tekrar eklemeyi engelleyen bir işaret, uygun seçici ve kapsam gerekir. Observer'ın çalışması asenkron zamanlamaya bağlı olduğundan test yalnız ilk açılışı değil, sonradan açılan formu ve tekrar açılışı da kapsamalıdır.

## Ekranın durumu: veri ile DOM'u ayırmak

Bir liste ekranı en az dört farklı durumda olabilir: yükleniyor, kayıtlar var, kayıt yok ve hata oluştu. Bütün durumları boş bir kutuyla gösterirseniz kullanıcı “veri mi yok, bağlantı mı bozuk?” sorusunun cevabını bulamaz. Kodda da bu ayrımı görünür tutun.

```javascript
const state = {
  status: 'idle',
  jobs: [],
  error: null
};
```

State, ekranın durumu hakkında tuttuğunuz modeldir. DOM bunun gösterimidir. State içinde hata varken ekranda eski başarı mesajını bırakmak çelişki yaratır. Bir render fonksiyonu duruma bakarak ekranı tek bir tutarlı biçimde güncellerse bu çelişkileri azaltabilirsiniz. Bu yaklaşımı anlamak için React kullanmanız gerekmez.

Ancak bütün uygulamayı tek bir küresel nesneye doldurmak da sürdürülebilir değildir. Hangi sayfanın hangi alanı değiştirdiği belirsizleşir. Önce küçük bir ekranın durumunu düzenli yönetin. Sonra ortak oturum bilgisi, sayfaya özel filtre ve geçici form taslağını ayırın. Orta seviyeye ilerlemek, yalnız daha çok sözdizimi bilmek değil, değişikliğin etkisini dar tutabilmektir.

# Asenkron JavaScript: zaman da programın girdisidir

## Promise ve async/await neyi çözer?

Bir sunucu isteğinin cevabı hemen gelmez. Disk veya ağ beklerken JavaScript'in her şeyi durdurmasını istemezsiniz. Promise, sonucu ileride belli olacak bir işlemi temsil eder. Pending, fulfilled ve rejected durumlarını düşünün: bekliyor, başarıyla sonuçlandı, başarısız oldu. Promise'in kendisi sonuç verisi değildir.

```javascript
const gecik = ms => new Promise(resolve => {
  setTimeout(resolve, ms);
});

async function deneme() {
  console.log('Başladı');
  await gecik(100);
  console.log('Bitti');
  return 7;
}

const sonuc = deneme();
console.log(sonuc instanceof Promise); // true
console.log(await sonuc);             // 7
```

Bu dosyayı `.mjs` olarak Node'da çalıştırabilirsiniz. Üst düzey await, ESM bağlamındadır. `async` fonksiyon her zaman Promise döndürür; içeride düz 7 döndürseniz bile çağıran taraf sonucu Promise üzerinden alır. `await`, bulunduğu async fonksiyonun devamını bekletir; bütün işletim sistemini dondurmaz.

Bir işlem asenkron diye kendi başına hızlı değildir. Çok ağır bir hesaplamayı async fonksiyonun içine koymanız onu ayrı işlemciye taşımaz. Büyük senkron hesap tarayıcının ana işini veya Node'un JavaScript yürütmesini meşgul edebilir. Ağ beklemek ile işlemciyi uzun süre kullanmak farklı performans problemleridir.

## Event loop'u bir çıktı tahminiyle öğrenmek

```javascript
console.log('A');
setTimeout(() => console.log('B'), 0);
Promise.resolve().then(() => console.log('C'));
console.log('D');
```

Bu örnekte beklenen sıra `A`, `D`, `C`, `B` olur. Mevcut senkron iş önce biter. Promise devamı microtask olarak işlenir. Zamanlayıcı callback'i daha sonra çalışabilecek işler arasına girer. `0` milisaniye, “bu satırı şimdi araya sok” anlamına gelmez. En erken uygun zamanda çalıştırılabileceğini düşünün.

Gerçek event loop ayrıntıları tarayıcı ve Node ortamlarında daha zengindir. Bu küçük örnekten “bütün asenkron işler her yerde aynı sırada gelir” sonucu çıkarmayın. Öğrenmeniz gereken pratik ilke şudur: kodda alt satırda yazmak, işlemin mutlaka sonra tamamlanacağını garanti etmez. İki ağ isteğinin tamamlanma sırasını internet koşulları da etkiler.

`await` unutulduğunda, veri sandığınız değişken Promise olabilir. `forEach(async ...)` kullandığınızda dış fonksiyon bütün işleri beklemeyebilir. Sıralı çalışma istiyorsanız `for...of` ve await; bağımsız işleri birlikte beklemek istiyorsanız `Promise.all` seçeneğini değerlendirin.

```javascript
for (const id of [1, 2, 3]) {
  await completeJob(id);
}

const results = await Promise.all([
  loadSummary(),
  loadJobs()
]);
```

İkinci örnekte işler bağımsızsa birlikte başlar. Biri reddedilirse Promise.all reddedilir; diğer işlemler kendiliğinden iptal olmaz. Her sonucu ayrı görmek istediğiniz toplu kontrollerde Promise.allSettled uygun olabilir. “Paralel yazdım, artık güvenli” diye düşünmeyin; aynı kaydı değiştiren işlemler arasında iş kuralı yarışları bulunabilir.

## Fetch: HTTP hatası ile ağ hatasını ayırmak

Fetch ile sunucuya istek gönderebilirsiniz. Önemli ayrıntı: 404 veya 500 HTTP yanıtı gelmesi fetch'in mutlaka rejected Promise üretmesi demek değildir. Yanıt alınmıştır; durum kodu başarısızdır. Bu nedenle response.ok kontrolü gerekir. Ağ kopması ve isteğin hiç tamamlanamaması farklıdır.

```javascript
async function jsonGet(url, options = {}) {
  const response = await fetch(url, options);
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }
  return response.json();
}
```

`response.json()` da asenkron bir ayrıştırmadır. Gövde JSON değilse hata verebilir. Sunucunun 204 No Content döndürdüğü bir istekte körlemesine json okumak da sorun yaratır. API sözleşmesini bilin: hangi endpoint hangi status ve hangi gövdeyi döndürüyor?

Bir istek gövdesi JSON ise başlığını da belirtin. Tarayıcının form sayfası ile API aynı origin'deyse birçok ayrıntı daha sade olur. Farklı origin kullanınca CORS kuralları devreye girer. CORS'u aşmak için rastgele `mode: 'no-cors'` eklemek çözüm değildir; çoğu durumda okuyamadığınız opaque response alırsınız. Önce protokolü, host'u ve portu karşılaştırın.

```javascript
const response = await fetch('/api/jobs', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ title: 'Aylık bakım' })
});
```

Üretim uygulamasında oturum çerezi kullanıyorsanız CSRF koruması da gerekir. Eğitim örneğinde kimlik doğrulama olmayacağı için canlıya açmayacağız. Küçük örneğin güvenlik sınırlarını bilmek, kodun eksiklerini gizlemekten daha değerlidir.

## Yanıt yarışı: hızlı tıklamak eski ekranı geri getirebilir

Bir kullanıcı önce Ankara, hemen sonra İzmir filtresini seçsin. Ankara isteği yavaş, İzmir isteği hızlı tamamlansın. Siz her tamamlanan yanıtı ekrana yazarsanız önce doğru İzmir, sonra yanlış Ankara görünür. Kullanıcının son niyeti ile son tamamlanan istek aynı şey değildir.

```javascript
let revision = 0;

async function refreshJobs(city) {
  const current = ++revision;
  const jobs = await jsonGet(`/api/jobs?city=${city}`);
  if (current !== revision) return;
  renderJobs(jobs);
}
```

Her yeni çağrı bir sıra numarası alır. Eski yanıt geldiğinde artık güncel olmadığını görüp göstermezsiniz. Bu yöntem ağ isteğini durdurmaz ama yanlış ekranın yazılmasını önler. Kullanıcı çıkış yaptıktan sonra eski bir özel yanıtın yeni oturum ekranına yazılmasını engellemek için de oturum nesli gibi benzer bir kavram gerekebilir.

AbortController ile gereksiz isteği iptal etmeyi deneyebilirsiniz:

```javascript
let controller;

async function refreshJobs(city) {
  controller?.abort();
  controller = new AbortController();
  try {
    const jobs = await jsonGet('/api/jobs?city=' + city, {
      signal: controller.signal
    });
    renderJobs(jobs);
  } catch (error) {
    if (error.name !== 'AbortError') throw error;
  }
}
```

İptal edilen istemci isteği, sunucunun daha önce tamamladığı bir yazmayı geri almaz. Kullanıcı Kaydet'e bastı, sunucu kaydetti, cevap gelirken bağlantı koptuysa “istek iptal, kayıt yapılmadı” varsayımı yanlış olabilir. Yazma işlemlerinde idempotency anahtarları ve sunucu tarafı işlem tasarımı bu yüzden önemlidir. Okuma yarışlarıyla yazma tekrarları aynı çözümü gerektirmez.

## Kaynaklara dönme alışkanlığı

JavaScript'in sözdizimi ve temel çalışma modeli için MDN JavaScript Guide, Promise davranışı için MDN Promise, HTTP cevap kontrolü için Using Fetch, iptal için AbortController sayfaları başlangıç başvuru noktalarıdır. Belgelerden bir yöntem seçerken önce hangi ortamda ve hangi sürümde kullanılabildiğine bakın. Belgedeki örneği kendi iş kuralınızın doğrulaması yerine koymayın. Bir API'nin var olması, sizin kullanımınızın doğru olduğu anlamına gelmez.

# Node.js: aynı dille sunucu tarafına geçmek

## Runtime ve süreç kavramını bağlamak

Node.js bir veritabanı değildir. JavaScript framework'ü veya paket yöneticisi de değildir. JavaScript'i tarayıcı dışında çalıştıran bir runtime, yani çalışma ortamıdır. `node server.mjs` çalıştırdığınızda işletim sistemi bir süreç başlatır. Bu süreç bir port dinleyebilir, izin verilen dosyaları okuyabilir ve HTTP isteklerine cevap verebilir. Terminali kapatınca uygulamanın durması bu yüzden şaşırtıcı değildir: program bir yerde çalışmalıdır.

Node'un event loop modeli çok sayıda ağ bekleyişini yönetebilir. Bu, “Node her durumda tek çekirdektir, hiçbir zaman paralel iş yapmaz” gibi kaba bir cümleyle açıklanamaz. JavaScript kodunun bir yürütme iş parçacığındaki davranışı ile işletim sistemi, thread pool, worker thread ve başka süreçlerin yaptığı işler farklıdır. Bu aşamada doğru pratik kural yeterlidir: uzun, senkron ve işlemci yoğun bir işi HTTP işleyicisine koyarsanız diğer ziyaretçilerin beklemesine neden olabilirsiniz.

Bir web uygulamasında Node yalnız geliştirme aracı da olabilir. Örneğin asıl API C# ile yazılmıştır ama tarayıcı testleri ve ön yüz paketleme komutları Node üzerinde çalışıyordur. Depoda package.json bulunması, canlı API'nin Node olduğu anlamına gelmez. Çok firmalı bir web projesinde .NET API ile Node tabanlı test araçlarının birlikte bulunması bu ayrımı anlamak için iyi bir örnektir.

## npm, package.json ve kilit dosyası

npm, paket kurmak ve proje komutlarını çalıştırmak için kullanılan araçlardan biridir. package.json projenin adı, komutları ve bağımlılık talepleri gibi bilgileri taşır. package-lock.json ise çözülmüş bağımlılık ağacını sabitlemeye yardım eder. Birini diğerinin yerine düşünmeyin: “hangi paket aralığını istiyoruz?” ile “bu kurulumda tam olarak hangi paketler seçildi?” farklı sorulardır.

```json
{
  "name": "sentetik-isler",
  "private": true,
  "type": "module",
  "scripts": {
    "start": "node server.mjs",
    "test": "node --test domain.test.mjs"
  }
}
```

Bu örneğin dış bağımlılığı yoktur. Bu nedenle kodu çalıştırmak için herhangi bir npm paketini indirmeniz gerekmez. `npm start` yalnız scripts.start alanındaki komutu çalıştırır. `npm test` de test komutunu çalıştırır. Komutun adının “test” olması, onun gerçekten doğru testler içerdiğini kanıtlamaz; her zaman karşısındaki işlemi okuyun.

`npm install paket-adi` projeye bağımlılık ekler ve kilit dosyasını güncelleyebilir. `npm ci`, mevcut package.json ve kilit dosyasının tutarlı olmasını bekleyerek tekrarlanabilir kurulum yapmayı amaçlar; bağımlılık değiştirmek için kullanılan komut değildir. CI ortamında bu ayrım önemlidir. Kilit dosyasını silerek her kurulumu “çözmek”, sorunu anlamadan belirsizlik üretir.

Paketler kod çalıştırabilir ve kurulum betikleri içerebilir. Adını gördüğünüz her paketi denemek için çalışan projenize eklemeyin. Bakımı, lisansı, amacı, sürüm geçmişi ve ihtiyacınız değerlendirilmelidir. Bir satırla yazılabilecek iş için büyük bir bağımlılık eklemenin de bakım maliyeti vardır. Tersi de geçerlidir: güvenlik açısından hassas bir algoritmayı sırf bağımlılık istemiyorum diye evde yeniden yazmak iyi fikir değildir.

## ESM ve CommonJS neden birbirine karışıyor?

Node projelerinde iki modül düzeni görebilirsiniz. ESM, `import` ve `export` kullanır. CommonJS, `require` ve `module.exports` kullanır. `.mjs` uzantısı bu kitabın örneklerinde ESM niyetini açıkça belirtir. `.cjs` CommonJS niyetini açıklar. `.js` dosyasının yorumu ise package.json içindeki type gibi kurallara bağlı olabilir.

```javascript
// math.mjs
export function add(a, b) {
  return a + b;
}
```

```javascript
// run.mjs
import { add } from './math.mjs';
console.log(add(2, 3)); // 5
```

Yerel ESM import'larında dosya uzantısını açık yazacağız. `node:assert/strict` gibi `node:` öneki ise Node'un yerleşik modülünü kullandığımızı anlatır. Bir örneği farklı modül düzenine geçirirken yalnız import kelimesini değiştirmek yetmeyebilir; paket uyumluluğu, dosya yolu çözümü ve çalışma sürümü de önemlidir.

`require is not defined in ES module scope` gördüğünüzde “paket eksik” diye yeniden kurulum yapmak ilk çözüm olmamalıdır. Dosya ESM olarak çalıştırılıyor ama CommonJS sözdizimi kullanılıyordur. Önce dosyanın uzantısını ve yakın package.json dosyasındaki type değerini okuyun. Hatanın açıklamasını bir arama cümlesi olarak değil, problemin kendisi olarak değerlendirin.

## Ortam değişkeni, yapılandırma ve sırlar

Uygulamanın portu, ortam adı veya log düzeyi kodun içine sabitlenmek yerine yapılandırmadan gelebilir. Node'da `process.env` değerleri metin olarak gelir. `'false'` metni truthy'dir; bu nedenle `if (process.env.DEBUG)` yazmak beklediğiniz sonucu vermeyebilir.

```javascript
const debugEnabled = process.env.DEBUG === 'true';
const port = Number(process.env.PORT ?? '5310');
if (!Number.isInteger(port) || port < 1 || port > 65535) {
  throw new Error('PORT geçersiz.');
}
```

PowerShell'de yalnız o terminal oturumu için değer atayabilirsiniz:

```powershell
$env:PORT = '5310'
node server.mjs
```

`.env` dosyası JavaScript'in kendi sihirli özelliği değildir. Kullandığınız araç veya çalışma seçeneği onu okuyorsa etkili olur. Parola veya API anahtarı içeren bir dosyayı Git'e koymayın. Bir değeri ortam değişkenine taşımak da onu kendiliğinden bütün tehditlere karşı güvenli yapmaz; erişim, loglama, süreç ortamı ve dağıtım düzeni birlikte değerlendirilir. Eğitim uygulamamız sır veya gerçek hesap kullanmayacak.

# Uygulamalı proje: sentetik asansör işleri mini uygulaması

## Projenin sınırı ve klasör düzeni

Şimdi önceki parçaları tek bir küçük sistemde birleştireceğiz. Ekranda açık işler listelenecek, yeni iş eklenecek ve tamamlandı olarak işaretlenecek. Veriler yalnız bellekte tutulacak. Sunucuyu kapatınca kayıtlar silinir. Bu bir hata değil, bu dersin bilinçli sınırıdır. Kalıcı veri ve ORM ayrı bölümün konusudur.

Bu örnekte kullanıcı girişi, firma izolasyonu, CSRF altyapısı, kalıcı depolama, yedekleme ve üretim log düzeni yoktur. Bu nedenle internete veya gerçek kullanıcılara açmayın. Yalnız `127.0.0.1:5310` dinlenecek. Canlı uygulamayı bu projeyle değiştirmeyin. Buradaki yalınlık kavramları görmeniz içindir; üretim hazır olma iddiası değildir.

Yeni eğitim klasörünüzde şu dosyaları oluşturun:

```text
sentetik-isler/
  package.json
  domain.mjs
  domain.test.mjs
  server.mjs
  public/
    index.html
    app.mjs
    styles.css
```

PowerShell'de klasör açmak için:

```powershell
New-Item -ItemType Directory -Force sentetik-isler/public
Set-Location sentetik-isler
```

package.json için bir önceki bölümdeki içeriği kullanın. Her dosyayı elle yazmanız önerilir. Sonuç çalışmazsa aşağıdaki dosyaları bir bütün olarak karşılaştırın; aynı isimli alanı bir dosyada title, diğerinde name yazmanız sözleşmeyi bozar. Bir API sözleşmesinin pratik anlamı tam olarak budur: iki taraf aynı alan ve davranış üzerinde anlaşmalıdır.

## İş kuralları: domain.mjs

Domain, işin teknik gösteriminden bağımsız kurallarını ifade eder. Bu örnekte bir işin başlığı geçerli olmalı, kimlik sayacı benzersiz artmalı ve tamamlanan işi tekrar tamamlamak ikinci bir kayıt yaratmamalıdır. Bu dosya HTTP bilmez, HTML bilmez. Böylece kuralları tarayıcı açmadan test edebiliriz.

```javascript
export class InputError extends Error {}

export function validateTitle(value) {
  if (typeof value !== 'string') {
    throw new InputError('Başlık metin olmalı.');
  }
  const title = value.trim();
  if (title.length < 3 || title.length > 80) {
    throw new InputError('Başlık 3-80 karakter olmalı.');
  }
  return title;
}

export function createStore() {
  let nextId = 1;
  const jobs = [];
  const copy = job => ({ ...job });

  return {
    list() {
      return jobs.map(copy);
    },
    add(input) {
      const title = validateTitle(input?.title);
      const job = { id: nextId++, title, done: false };
      jobs.push(job);
      return copy(job);
    },
    complete(id) {
      const job = jobs.find(item => item.id === id);
      if (!job) return null;
      job.done = true;
      return copy(job);
    }
  };
}
```

Neden listede doğrudan jobs dizisini döndürmedik? Çağıran kodun gizli iç veriyi değiştirmesini istemiyoruz. `map(copy)` yeni dizi ve düz kayıt kopyaları döndürüyor. Bu modelde iç içe nesne bulunmadığı için yüzeysel kopya yeterlidir. İleride job içine address gibi nesne eklerseniz bu varsayımı yeniden değerlendirmeniz gerekir.

`input?.title` optional chaining kullanır. Input null veya undefined ise title okumaya çalışırken çökmez; validateTitle'a undefined gider ve orada kontrollü hata oluşur. Bu, “her alanı ?. ile okuyun, hatalar bitsin” önerisi değildir. Zorunlu olması gereken verinin yokluğunu sessizce yaymak yerine uygun sınırda anlamlı hata vermek gerekir.

## Birim testi: domain.test.mjs

Testler yalnız örnek çalışıyor mu diye bakmayacak. Boş başlığı, sınır uzunluklarını, dışarı dönen nesnenin iç kaydı bozamamasını ve tekrarlanan tamamlamayı da kontrol edeceğiz. Bir testin başarısı, bütün uygulamanın doğru olduğunu kanıtlamaz; yalnız yazdığınız beklentilerin o koşuda sağlandığını gösterir.

```javascript
import test from 'node:test';
import assert from 'node:assert/strict';
import { createStore, validateTitle, InputError } from './domain.mjs';

test('başlık boşluğu temizler', () => {
  assert.equal(validateTitle('  Aylık bakım  '), 'Aylık bakım');
});

test('geçersiz başlıkları reddeder', () => {
  for (const value of [null, 4, '', 'ab', 'x'.repeat(81)]) {
    assert.throws(() => validateTitle(value), InputError);
  }
});

test('başlık sınırları dahil kabul edilir', () => {
  assert.equal(validateTitle('abc').length, 3);
  assert.equal(validateTitle('x'.repeat(80)).length, 80);
});

test('iki kayıt farklı kimlik alır', () => {
  const store = createStore();
  const first = store.add({ title: 'Birinci bakım' });
  const second = store.add({ title: 'İkinci bakım' });
  assert.equal(first.id, 1);
  assert.equal(second.id, 2);
});

test('liste kopyası iç kaydı değiştiremez', () => {
  const store = createStore();
  store.add({ title: 'Aylık bakım' });
  const items = store.list();
  items[0].title = 'Dışarıdan değişti';
  items.push({ id: 9 });
  assert.equal(store.list().length, 1);
  assert.equal(store.list()[0].title, 'Aylık bakım');
});

test('tamamlama tekrarı yeni kayıt yaratmaz', () => {
  const store = createStore();
  const job = store.add({ title: 'Arıza kontrolü' });
  assert.equal(store.complete(job.id).done, true);
  assert.equal(store.complete(job.id).done, true);
  assert.equal(store.list().length, 1);
  assert.equal(store.complete(999), null);
});
```

Çalıştırın:

```powershell
node --test domain.test.mjs
```

Altı testin geçmesini bekliyoruz. Sıfır test çalışıp komutun başarılı çıkması, bu altı davranışın doğrulandığı anlamına gelmez. Toplam ve atlanan sayısını okuyun. Sonra bilinçli olarak domain.mjs içindeki `title.length < 3` koşulunu `< 4` yapın. Sınır testi düşmelidir. Geri alınca yeniden geçmelidir. Bu küçük deney, testin ilgili hatayı yakalayabildiğine dair daha güçlü kanıt üretir.

## HTTP sunucusu: server.mjs

Aşağıdaki sunucu yalnız açıkça izin verdiğimiz üç statik dosyayı sunar. İstek yolunu doğrudan diskteki herhangi bir yola çevirmiyoruz. API ile dosya sunumunu aynı origin'de tutarak dersin CORS karmaşıklığını azaltıyoruz. HTTP katmanı gelen veriyi okur, domain'i çağırır ve sonucu uygun durum koduyla döndürür.

```javascript
import http from 'node:http';
import { readFile } from 'node:fs/promises';
import { createStore, InputError } from './domain.mjs';

const store = createStore();
const files = new Map([
  ['/', ['index.html', 'text/html; charset=utf-8']],
  ['/app.mjs', ['app.mjs', 'text/javascript; charset=utf-8']],
  ['/styles.css', ['styles.css', 'text/css; charset=utf-8']]
]);

function json(response, status, value) {
  response.writeHead(status, {
    'Content-Type': 'application/json; charset=utf-8',
    'Cache-Control': 'no-store'
  });
  response.end(JSON.stringify(value));
}

async function bodyJson(request) {
  const chunks = [];
  let size = 0;
  let tooLarge = false;
  for await (const chunk of request) {
    size += chunk.length;
    if (size > 8192) {
      tooLarge = true;
      chunks.length = 0;
    }
    if (!tooLarge) chunks.push(chunk);
  }
  if (tooLarge) {
    throw new InputError('İstek gövdesi çok büyük.');
  }
  try {
    return JSON.parse(Buffer.concat(chunks).toString('utf8'));
  } catch {
    throw new InputError('Geçerli JSON gönderin.');
  }
}

const server = http.createServer(async (request, response) => {
  try {
    const url = new URL(request.url, 'http://127.0.0.1:5310');
    if (request.method === 'GET' && files.has(url.pathname)) {
      const [name, type] = files.get(url.pathname);
      const data = await readFile(new URL('./public/' + name,
        import.meta.url));
      response.writeHead(200, { 'Content-Type': type });
      response.end(data);
      return;
    }
    if (request.method === 'GET' && url.pathname === '/api/jobs') {
      json(response, 200, store.list());
      return;
    }
    if (request.method === 'POST' && url.pathname === '/api/jobs') {
      const type = request.headers['content-type'] ?? '';
      if (!type.startsWith('application/json')) {
        json(response, 415, { error: 'JSON gerekli.' });
        return;
      }
      const job = store.add(await bodyJson(request));
      json(response, 201, job);
      return;
    }
    const match = /^\/api\/jobs\/(\d+)\/complete$/.exec(url.pathname);
    if (request.method === 'POST' && match) {
      const id = Number(match[1]);
      const job = store.complete(id);
      json(response, job ? 200 : 404,
        job ?? { error: 'İş bulunamadı.' });
      return;
    }
    json(response, 404, { error: 'Adres bulunamadı.' });
  } catch (error) {
    if (error instanceof InputError) {
      json(response, 400, { error: error.message });
    } else {
      console.error('İstek işlenemedi:', error.message);
      json(response, 500, { error: 'Sunucu hatası.' });
    }
  }
});

server.requestTimeout = 10000;
server.headersTimeout = 10000;
server.listen(5310, '127.0.0.1', () => {
  console.log('Eğitim: http://127.0.0.1:5310');
});
```

Bu dersin gövde okuyucusu 8192 bayttan fazlasını bellekte tutmaz; fazla içeriği okuduktan sonra kontrollü 400 verir. Üretimde trafik sınırlama, bağlantıyı erken sonlandırma stratejisi, reverse proxy sınırları ve daha ayrıntılı durum kodları ayrıca tasarlanır. “Sınır koyduk” ile “kötü niyetli bütün trafik biçimlerini çözdük” aynı iddia değildir.

Neden 201? Yeni kaynak oluşturulduğunu anlatır. Neden bulunamayan kayıt 404? Yolun veya istenen kaynağın bulunmadığını anlatır. Neden yanlış içerik türü 415? Sunucunun bu gövde türünü kabul etmediğini anlatır. Her hataya 200 dönüp içine `{ success: false }` koyarsanız HTTP'nin hazır anlamlarını ve birçok aracı gereksiz yere etkisizleştirirsiniz.

## Sayfa: public/index.html

```html
<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Sentetik iş listesi</title>
  <link rel="stylesheet" href="/styles.css">
  <script type="module" src="/app.mjs"></script>
</head>
<body>
  <main>
    <h1>Sentetik iş listesi</h1>
    <p>Bu ekran gerçek müşteri verisi kullanmaz.</p>
    <form id="job-form">
      <label for="title">Yeni iş başlığı</label>
      <input id="title" name="title" required
        minlength="3" maxlength="80">
      <button type="submit">İş ekle</button>
    </form>
    <p id="message" role="status"></p>
    <button id="refresh" type="button">Yenile</button>
    <ul id="jobs"></ul>
  </main>
</body>
</html>
```

Label'ın for değeri ile input'un id değeri eşleşir. Bu ilişki hem tıklama alanını hem erişilebilir adı etkiler. Sayfada görünen metnin input'a yakın durması tek başına programatik ilişki kurmaz. `role=status`, mesaj değiştiğinde yardımcı teknolojilerin bunu uygun biçimde duyurabilmesine yardımcı olur; bütün hataları ekranda yalnız renk değiştirerek anlatmayın.

## İstemci: public/app.mjs

```javascript
const form = document.querySelector('#job-form');
const list = document.querySelector('#jobs');
const message = document.querySelector('#message');
const refresh = document.querySelector('#refresh');
let revision = 0;

async function api(path, options = {}) {
  const response = await fetch(path, options);
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.error ?? `HTTP ${response.status}`);
  }
  return data;
}

function render(jobs) {
  const fragment = document.createDocumentFragment();
  for (const job of jobs) {
    const li = document.createElement('li');
    const title = document.createElement('span');
    title.textContent = job.title + (job.done ? ' - Tamamlandı' : '');
    const button = document.createElement('button');
    button.type = 'button';
    button.textContent = 'Tamamla';
    button.disabled = job.done;
    button.addEventListener('click', async () => {
      button.disabled = true;
      try {
        await api(`/api/jobs/${job.id}/complete`, { method: 'POST' });
        await load();
      } catch (error) {
        message.textContent = error.message;
        button.disabled = false;
      }
    });
    li.append(title, button);
    fragment.append(li);
  }
  list.replaceChildren(fragment);
}

async function load() {
  const current = ++revision;
  message.textContent = 'Yükleniyor...';
  try {
    const jobs = await api('/api/jobs');
    if (current !== revision) return;
    render(jobs);
    message.textContent = jobs.length
      ? `${jobs.length} iş var.` : 'Henüz iş yok.';
  } catch (error) {
    if (current === revision) message.textContent = error.message;
  }
}

form.addEventListener('submit', async event => {
  event.preventDefault();
  const button = form.querySelector('button');
  button.disabled = true;
  try {
    const title = new FormData(form).get('title');
    await api('/api/jobs', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title })
    });
    form.reset();
    await load();
  } catch (error) {
    message.textContent = error.message;
  } finally {
    button.disabled = false;
  }
});

refresh.addEventListener('click', load);
load();
```

Bu istemcide hata mesajı sunucunun bu eğitim API'sinde bilinçli olarak kullanıcıya uygun tuttuğu error alanından gelir. Gerçek uygulamada veri tabanı hata metnini doğrudan kullanıcıya taşımayın. Bir SQL sorgusu, dosya yolu veya iç servis ayrıntısı gereksiz bilgi sızdırabilir. Hata sözleşmesi de API tasarımının parçasıdır.

Listeye başlık yazarken textContent kullandık. Bir iş tamamlandıktan sonra düğme pasifleşiyor ama sunucu aynı tamamlamayı tekrar aldığında yine tutarlı davranıyor. Arayüzde düğmeyi pasifleştirmek sunucu kuralının yerine geçmiyor; yalnız yanlışlıkla tekrar tıklamayı azaltıyor.

## Görünüm: public/styles.css

```css
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #eef4f1;
  color: #163c32;
  font: 16px system-ui, sans-serif;
}
main {
  max-width: 700px;
  margin: 32px auto;
  padding: 24px;
  background: white;
  border-radius: 12px;
}
form { display: grid; gap: 8px; }
input, button { font: inherit; padding: 10px; }
li {
  display: flex;
  gap: 12px;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
li span { overflow-wrap: anywhere; }
button { cursor: pointer; }
button:disabled { cursor: default; opacity: .65; }
@media (max-width: 500px) {
  main { margin: 12px; padding: 16px; }
  li { align-items: stretch; flex-direction: column; }
}
```

## Çalıştırma ve gözle kontrol

Önce testleri çalıştırın, sonra sunucuyu başlatın:

```powershell
npm test
npm start
```

Tarayıcıda `http://127.0.0.1:5310` açın. İlk durumda “Henüz iş yok.” görmelisiniz. “Aylık bakım” yazıp ekleyin. Listede bir kayıt görünmeli. Tamamla düğmesine basınca “Tamamlandı” yazmalı ve düğme pasif olmalı. Sunucuyu Ctrl+C ile kapatıp yeniden başlatınca listenin boşalması beklenir; veri yalnız bellekteydi.

DevTools Network sekmesinde GET /api/jobs isteğini bulun. Status, Response ve Timing alanlarını inceleyin. Ardından yeni iş ekleyip POST isteğinin Request Payload bölümünde title alanını görün. İstemciyle sunucu arasındaki anlaşma artık soyut bir söz değildir; gözünüzün önünde taşınan JSON'dur.

Sunucu açıkken ikinci bir PowerShell penceresinde API'yi arayüz olmadan kullanın:

```powershell
$body = @{ title = 'Terminalden bakım' } | ConvertTo-Json
Invoke-RestMethod -Uri 'http://127.0.0.1:5310/api/jobs' `
  -Method Post -ContentType 'application/json' -Body $body
Invoke-RestMethod -Uri 'http://127.0.0.1:5310/api/jobs'
```

İşte sunucu doğrulamasının neden şart olduğunun somut kanıtı: kullanıcı arayüzünü hiç kullanmadan istek gönderebildiniz. Şimdi title yerine 9 gönderin; 400 beklenir. Bu denemeleri yalnız eğitim sunucusunda yapın. Gerçek sistemde veri değiştiren API'leri merak için çağırmak, okuma yapmakla aynı şey değildir.

# Testçi gibi düşünmek ve debugger kullanmak

## Test türlerinin farkı

Birim testi küçük bir kuralı mümkün olduğunca dış sistemlerden bağımsız sınar. Buradaki validateTitle testi buna örnektir. Entegrasyon testi birden fazla parçanın birlikte davranışını ölçer: HTTP isteği gerçekten domain'e ulaşıyor mu, JSON doğru durum koduyla dönüyor mu? Uçtan uca, yani E2E test ise tarayıcıdaki kullanıcı akışını izler: alanı doldur, kaydet, listede gör. Her testin maliyeti ve yakaladığı hata sınıfı farklıdır.

“Bütün testleri E2E yapalım” pahalı, yavaş ve kırılgan olabilir. “Bütün testleri unit yapalım” da yanlış dosya yolu, yanlış endpoint veya bozuk CSS yerleşimini kaçırabilir. Sağlam yaklaşım, iş kurallarını küçük testlerle korumak ve kritik birleşme noktalarıyla kullanıcı akışları için daha az sayıda anlamlı üst düzey test eklemektir.

Bir test kendi yazdığınız kodla aynı yanlış hesabı tekrar ederse geçebilir. Örneğin istemci şifre kuralını Unicode büyük harf kabul edecek şekilde yazıp testte de “İstanbul-2026 bütün kuralları karşılar” beklentisi kurarsanız test yeşildir ama sunucu aynı şifreyi reddedebilir. Testteki beklenen sonucun bağımsız ve doğru bir dayanağı olmalıdır. İki katmanın aynı isimli kuralı gerçekten aynı örneklerde sınanmalıdır.

## DevTools ile altı adımda hata izleme

Önce kullanıcıdaki belirtiyi tam cümleyle yazın: “Tamamla düğmesine basınca bir iş yerine iki iş kayboluyor.” Sonra tekrar adımlarını en aza indirin. Hatanın belirli kullanıcıda mı, her kullanıcıda mı, yalnız 390 px'te mi, yalnız ikinci açılışta mı oluştuğunu bulun. Bu gözlemler rastgele tahminlerden daha değerlidir.

Console'daki ilk hatayı okuyun; sonradan üretilen on yan hata sizi asıl noktadan uzaklaştırabilir. Sources bölümünde hatanın geldiği satıra breakpoint koyun. Aynı işlemi tekrar yapın. Çalışma durunca yerel değişkenleri, çağrı yığınını ve beklediğiniz türleri inceleyin. Satır satır ilerlerken “şimdi hangi koşul doğru oldu?” diye sorun.

Network sekmesinde ilgili isteğin method, URL, status ve güvenli gövde alanlarını kontrol edin. İstek hiç çıkmıyorsa sunucuyu düzeltmeye başlamayın; olay işleyicisi veya istemci doğrulaması engelliyordur. İstek çıkıyor ama 403 dönüyorsa CSS sorunu çözmez. Yanıt 200 ve doğru veriyse ama ekran yanlışsa gösterim katmanına dönün.

Node tarafında da breakpoint kullanabilirsiniz. Geliştirme için `node --inspect server.mjs` çalıştırınca debugger bağlantısı açılabilir; bu arayüzü genel ağa açmayın. Alternatif olarak kısa, güvenli console.log çıktıları ekleyebilirsiniz. Fakat “her şeyi logla” yaklaşımı hem gürültü hem sır sızıntısı üretir. Hipotezinizi sınayan iki veya üç değer çoğu zaman daha yararlıdır.

## Hata avı 1: string toplama

Belirti: iki iş tutarı 10 ve 20 girilince toplam 1020 görünüyor. Kod `first.value + second.value` kullanıyor. İlk kontrolünüz değerlerin türüdür. İkisi de string çıkar. Düzeltme yalnız Number çağırmak değildir: boşluk, negatiflik, kesir ve geçerli para birimi de iş kuralına göre doğrulanmalıdır. Birim kuruşsa formdan alınan TL değerinin dönüştürme sınırını tek yerde tutun.

Regresyon testi için 10+20, boş alan, 0 ve geçersiz metin örneklerini ekleyin. Yalnız 10+20 testini geçirmekle yetinmeyin; boş metnin 0'a dönüşmesi sessiz hata olmaya devam edebilir.

## Hata avı 2: ilk tıklama çalışıyor, ikinci tıklama çift kayıt yapıyor

Belirti: modal her açıldığında aynı düğmeye yeni bir click dinleyicisi ekleniyor. Önceki dinleyici kaldırılmıyor. İkinci açılışta iki POST gidiyor. Network'te tek kullanıcı hareketi için iki istek gördüğünüzde iki kez kullanıcı tıkladı varsaymayın. Dinleyicilerin ömrünü inceleyin.

Düzeltme ekranın tasarımına göre bir kez dinleyici bağlamak, eski dinleyiciyi kaldırmak, yeni form elemanı üretmek veya event delegation kullanmak olabilir. Sunucu yazmalarında tekrar güvenliği yine ayrı konudur. İstemciyi düzelttiniz diye sunucunun iki eş istekte iki tahsilat üretmesi kabul edilebilir hâle gelmez.

## Hata avı 3: 404 olunca hata ekranı çıkmıyor

Belirti: olmayan /api/jbos adresine fetch atılıyor, catch çalışmıyor ve liste boş kalıyor. Burada iki hata vardır: yol yanlış ve response.ok kontrolü yok. Fetch yanıt aldığı için Promise başarıyla sonuçlanmıştır. Doğru çözüm yolu düzeltmek ve HTTP başarısızlığını açıkça ele almaktır.

Test için sunucuya hiç ulaşılamaması ile sunucunun 404 döndürmesini ayrı senaryolar olarak kurun. İkisine aynı kullanıcı mesajı gösterebilirsiniz ama geliştirici teşhisinde farkı kaybetmeyin. Log veya test çıktısında birini diğerinin kanıtı saymayın.

## Hata avı 4: filtre geri dönüyor

Belirti: hızlıca iki firma seçince eski firmanın listesi ekrana geliyor. DevTools'ta Slow 3G gibi ağ yavaşlatma kullanarak tekrar üretmeyi deneyin. İsteklerin başlama sırası ile bitiş sırasını karşılaştırın. Eski cevap güncel ekranı boyuyorsa revizyon/oturum kontrolü veya uygun iptal düzeni gerekir.

Düzeltme testini yalnız normal hızda yapmayın. İlk isteği bilinçli geciktirip ikinciyi erken tamamlayın. Son görünen kayıtların kullanıcının son seçimine ait olduğunu doğrulayın. Bu, “test çalıştı” cümlesinden daha açık bir kanıttır.

## Hata avı 5: Vazgeç dedim ama satır değişti

Belirti: formdaki düzenleme taslağı asıl nesneye doğrudan bağlıdır. Kullanıcı yazdıkça bellekteki kayıt değişir. Kaydet'e basmadığı hâlde listede yeni isim görünür. Referansları izleyin. `const draft = row` kopya oluşturmaz. İç içe nesnelerde `{ ...row }` da tüm sorunu çözmeyebilir.

Testte formu açın, alanı değiştirin, vazgeçin, listeyi yeniden çizdirin. Kaydın önceki değerinin korunmasını bekleyin. Sunucuya hiç POST çıkmadığını Network'te görmek tek başına yeterli değildir; hata yalnız istemci belleğinde olabilir.

## Hata avı 6: sunucu çalışmıyor mu, port mu dolu?

Belirti: `EADDRINUSE` hatası görülüyor. Bu hata API rotanızdaki if koşulunu anlatmıyor; istenen adreste başka bir dinleyici bulunduğunu söylüyor. Eğitim programının başka terminalde açık olup olmadığını kontrol edin. Başkasının sürecini rastgele kapatmayın. Kendi sürecinizi tanıyıp onu durdurun veya örnekteki portu kontrollü olarak değiştirin.

`ECONNREFUSED` ise çoğu zaman hedef adreste bağlantıyı kabul eden süreç bulunmadığını gösterir. `404` ile aynı şey değildir. Birinde HTTP yanıtı bile alınamamış olabilir, diğerinde bir sunucu cevap vermiştir. Hataları katmanlarına ayırmak ilerleme hızınızı belirgin biçimde artırır.

## Hata avı 7: test yeşil, kullanıcı ekranı bozuk

Belirti: input ve yardımcı kural listesi iki sütunlu formda ayrı grid çocuklarıdır. Küçük unit test listenin var olduğunu doğrular; masaüstünde liste yanlış alanın altında görünür. Testin kontrol etmediği özellik hakkında yeşil sonuçtan güven üretmeyin. Görünüm için boyut, ilişki, taşma ve farklı içerik uzunluğu ayrı incelemelerdir.

Çözüm, yardımcı metni ait olduğu alanla aynı kapsayıcıda tutmak olabilir. Ardından 390 ve 1280 px gibi en az iki farklı genişlikte gerçek görüntüyü kontrol edin. “Yatay taşma yok” testi, metinlerin doğru alanla hizalandığını kanıtlamaz. Her test cümlesinin hangi iddiayı karşıladığını söyleyin.

# Elle çözme çalışmaları ve değerlendirme

## Çözmeden önce kurallar

Aşağıdaki soruların çözümleri bu kısmın sonundadır. Önce çözüme bakmayın. Her soruda önce beklenen davranışı bir cümleyle yazın, sonra en az iki örnek girdi seçin, ardından kodlayın. Hata aldığınızda rastgele satır değiştirmek yerine ilk hatayı ve varsayımınızı not edin. Çözümün sizin yazdığınızdan kısa olması, sizin çözümünüzün mutlaka kötü olduğu anlamına gelmez; doğruluk ve açıklanabilirlik önce gelir.

1. `open` ve `closed` sayılarını alıp toplamı döndüren bir fonksiyon yazın. Negatif değer gelince hata versin. Console'a yazmakla sonuç döndürmeyi karıştırmayın.
2. Metin olarak gelen iki sayıyı toplayın. Boş metni 0 kabul etmeyin. `'12abc'` girdisini reddedin.
3. Fiyat 0 olduğunda 0'ı koruyan, yalnız null/undefined olduğunda 500 kullanan tek satırlık ifade yazın. Neden || kullanmadığınızı açıklayın.
4. İş listesinde yalnız tamamlanmamış kayıtları seçin. Ardından yalnız başlıkların dizisini oluşturun. Asıl diziyi değiştirmeyin.
5. `[2, 10, 1]` dizisini sayısal olarak sıralayın. İlk dizinin neden değişmemesi gerektiğini bir ekran örneğiyle açıklayın.
6. İki bağımsız sayaç üretin. Birinciyi üç kez, ikinciyi bir kez çağırın. Sonuçları tahmin edin ve closure ile açıklayın.
7. İç içe address nesnesi olan bir müşteri için düzenleme taslağı oluşturun. Taslak şehir değişince asıl kaydın şehri değişmesin.
8. `<b>Bakım</b>` başlığını HTML çalıştırmadan aynen metin olarak gösteren bir li elemanı oluşturun.
9. 404 döndüren fetch yanıtını hata olarak ele alan küçük bir GET yardımcı fonksiyonu yazın. JSON olmayan hata gövdesi ihtimalini de düşünün.
10. İlk arama yavaş, ikinci arama hızlı tamamlanınca yalnız ikinci sonucu gösteren bir sıra numarası denetimi kurun.
11. Bir formun submit olayında düğmeyi kapatın. Başarıda da hatada da düğmenin tekrar açıldığını sağlayın.
12. Domain testlerine 80 karakterin kabul, 81 karakterin ret örneğini ekleyin. Testin yanlış koşulu yakaladığını bilinçli bozarak gösterin.
13. createStore'a `countOpen()` ekleyin. Bir iş tamamlanınca açık sayısı bir azalmalı, aynı iş tekrar tamamlanınca tekrar azalmamalı.
14. Mini uygulamada tamamlanan kayıtları göstermeyen bir checkbox ekleyin. Filtre yalnız istemcide olsun; sunucu verisini silmesin.
15. Mini API'de GET /api/health ekleyin. `{ "status": "ok" }` dönsün. Olmayan /api/healt adresi 404 kalmalı.
16. Terminalden yanlış içerik türüyle POST gönderin. 415 aldığınızı gösterin. Başarısız isteğin kayda dönüşmediğini listeyi okuyarak doğrulayın.
17. Bir module dosyasından validateTitle'ı dışa aktarın ve başka bir dosyada kullanın. Dosya uzantısını bilerek yanlış yazıp çıkan hatayı okuyun.
18. `process.env.FEATURE='false'` iken özelliği kapatan bir kontrol yazın. Metnin truthy olmasıyla iş kuralını ayırın.
19. Her kayıt için asenkron işlem yapan `forEach` yerine sırayla bekleyen bir döngü yazın. Son logun bütün işlemler bitince geldiğini kanıtlayın.
20. Kendi uygulamanızdaki bir hatayı en az kodla tekrar üreten dosya hazırlayın. Dosyada gerçek parola, müşteri adı veya token bulunmasın.

## Çözüm yönleri: önce kendi kodunuzla karşılaştırın

Birinci soruda parametreler için Number.isInteger ve negatiflik denetimi yapabilirsiniz. Fonksiyonun sonunda `return open + closed` bulunmalıdır. `console.log` çağırmak sonucu başka fonksiyona taşımaz. Testte `sum(2, 3) === 5`, `sum(-1, 3)` hata beklentileri kurun. İki parametreyi aynı anda kontrol etmek yerine her biri için doğru koşulu yazdığınızı açıklayın.

İkinci soruda önce trim ile boşluğu reddedin, sonra Number ile dönüştürün. Sonuç için Number.isFinite veya ihtiyaç tam sayıysa Number.isSafeInteger kullanın. Her sayı problemi için aynı doğrulayıcı uygun değildir: miktar yalnız tam sayı olabilirken oran kesirli olabilir. Üçüncü sorunun özü `price ?? 500` ifadesidir. 0 geçerli bir değer olduğu için || yanlış tercihtir.

Dördüncü soru `jobs.filter(job => !job.done)` ve ardından `.map(job => job.title)` ile çözülebilir. İsterseniz bunları iki ayrı satırda yazın; tek satıra sıkıştırmak zorunda değilsiniz. Beşinci soruda `[...numbers].sort((a, b) => a - b)` dış diziyi korur. Kullanıcı filtreyi kapattığında özgün sıralamaya dönmeniz gereken bir ekran, diziyi yerinde değiştirmemenin gerekçesidir.

Altıncı soruda her sayaç oluşturma çağrısı ayrı closure çevresi üretmelidir. Sayaç değişkenini fonksiyonun dışında tek yerde tanımlarsanız iki sayaç ortak sayıyı artırır. Birinci 1, 2, 3; ikinci 1 üretmelidir. Yedinci soruda dış nesne ve address alanı ayrı kopyalanır. Kopyalamanın derinliğini veri yapısına göre seçtiğinizi, rastgele JSON dönüşümü yapmadığınızı açıklayın.

Sekizinci sorunun doğru yaklaşımı createElement ve textContent'tir. Metni innerHTML'ye verip sonra “bizim başlıklar güvenilir” demek sorunun amacını kaçırır. Dokuzuncu soruda response.ok kontrol edilir; hata gövdesinin içerik türüne veya ayrıştırılabilirliğine güvenilmez. En basit sağlam sürüm başarısız status'ta HTTP numarasıyla hata verir, yalnız başarılı ve JSON beklenen yanıtta json okur.

Onuncu soruda her yeni arama bir sayaç değeri alır; yanıt döndüğünde bu değer güncel sayaçla karşılaştırılır. Sonuç geçersizse render yapılmaz. On birinci soruda finally kullanın. Düğmeyi yalnız başarı yolunda açarsanız hata alan kullanıcı kilitlenir. Birden fazla kaydet düğmesi bulunan formlarda hangi submitter'ın kapatıldığını da açıkça seçmelisiniz.

On ikinci soruda hem alt hem üst sınır testini ayrı isimlendirmek hata mesajını okunur kılar. 81 karakteri kabul edecek biçimde koşulu bilinçli bozduğunuzda test düşmelidir. Bu bir üretim değişikliği değil, eğitimde testin duyarlılığını kontrol etme deneyidir. Bitince doğru kodu geri getirin.

On üçüncü sorunun basit çözümü şöyledir:

```javascript
countOpen() {
  return jobs.filter(job => !job.done).length;
}
```

Sayıyı ayrı bir değişkende tutup her tamamlamada azaltmak, tekrarlanan tamamlamada negatif veya yanlış sonuç üretmeye daha açıktır. Küçük bir bellek örneğinde sayıyı mevcut kayıtlardan türetmek daha sadedir. Büyük veri tabanında performans ve tutarlılık tasarımı farklı değerlendirilir; bu örnekten “her raporu tüm kayıtları belleğe alarak hesaplayın” sonucu çıkarmayın.

On dördüncü soruda orijinal jobs dizisini saklayın, checkbox değişince render'a filtrelenmiş bir dizi verin. `splice` ile tamamlananları asıl listeden silmeyin. On beşinci soruda mevcut 404 dönüşünden önce tam yol ve GET method koşulu ekleyin. Kısmi string eşleşmesiyle bütün /api/health... adreslerini yanlışlıkla kabul etmeyin.

On altıncı soruda Content-Type başlığını text/plain yapıp aynı JSON metnini gönderin. API 415 vermeli. Sonra GET ile listeyi okuyup toplamın değişmediğini sınayın. Yalnız durum kodunu kontrol edip veriye bakmamak, başarısız yanıta rağmen yazma yapan bir hatayı kaçırabilir. On yedinci soruda import yolunun başındaki `./` ve uzantı önemlidir; terminalde bulunduğunuz klasörle modülün kendi göreli yolu farklı kavramlardır.

On sekizinci soruda `process.env.FEATURE === 'true'` gibi açık bir karşılaştırma kullanın; bilinmeyen metinleri sessizce etkin saymayın. On dokuzuncu soru için `for (const item of items) { await work(item); }` uygundur. İşler bağımsız ve birlikte çalıştırılacaksa Promise.all başka bir seçimdir; problem sıralı çalışma istiyorsa o sözleşmeyi koruyun.

Yirminci sorunun tek doğru kodu yoktur. İyi bir tekrar dosyası, problemi gerekli en küçük veriyle oluşturur, beklenen ve gerçekleşen sonucu yan yana gösterir ve dış sistemlere ihtiyaç duymaz. Hata bir yarışsa tamamlanma sırasını kontrollü gecikmelerle üretin. Hata bir tarih sınırıysa bilgisayar saatini değiştirmeden tarihe parametre alan yardımcıyı sınayın. Hata gerçek kullanıcıya özgüyse kişisel veriyi örnekten çıkarıp aynı biçimi taşıyan sahte veriler kullanın.

## Bu kısmın beceri sınavı

Bir sonraki aşamaya geçmeden şu işi yardım almadan yapmayı deneyin: mini projeye “yalnız açık işler” filtresi, kayıt sayısı ve başlık araması ekleyin. Sonra boş başlığı arayüzden ve doğrudan API'den ayrı ayrı gönderin. Bir işin tamamlanmasının neden iki farklı tarayıcı sekmesinde otomatik aynı anda görünmediğini açıklayın. Bellekte veri tutmanın, her sekmenin kendi DOM'una sahip olmasının ve sunucudan yeniden okumanın farkını anlatın.

Ardından bütün kodu silmeden, boş bir klasörde yeniden kurun. Bu sefer önce domain ve testleri, sonra HTTP katmanını, en son ekranı yazın. Bir satırı hatırlamadığınızda belgeye bakabilirsiniz; gerçek geliştiriciler de bakar. Ölçüt ezber değil, doğru soruyu sormak ve sonucu doğrulamaktır. “Fonksiyon ne alıyor, hangi durumda hata veriyor, ne döndürüyor, dışarıda neyi değiştiriyor?” sorularını her temel parça için cevaplayabiliyorsanız sağlam ilerliyorsunuz.

Mid-level bir geliştirici yalnız bu örneği bitiren kişi değildir. Belirsiz gereksinimi netleştirir, değişikliğin etki alanını sınırlar, ekipte okunabilir kod bırakır, bir hatayı kanıtla anlatır ve testin sınırlarını dürüstçe söyler. Bu kısım size o davranışların küçük bir laboratuvarını verir. Gerçek projede farklı veri hacmi, güvenlik ve bakım kararlarıyla bunu tekrar tekrar uygulamanız gerekir.

## Birincil kaynaklar ve ileri okuma

Bu dersin açıklamaları ve eğitim projesi özgün çalışma malzemesidir. Aşağıdaki belgeler yöntemlerin ayrıntısı ve sürüm uyumluluğu için başvuru noktalarıdır; kitabın kodlarını anlamadan belge örneklerini kopyalamayın.

- MDN, JavaScript Guide: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
- MDN, Using the Fetch API: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
- MDN, Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
- MDN, AbortController: https://developer.mozilla.org/en-US/docs/Web/API/AbortController
- Node.js, HTTP API: https://nodejs.org/api/http.html
- Node.js, Test runner: https://nodejs.org/api/test.html
