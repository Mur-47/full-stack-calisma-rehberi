# Sıfırdan Full Stack Geliştiriciliğe

**Hazırlayan ve yayımlayan: Murat AKTAŞ ([Mur-47](https://github.com/Mur-47)).**

Türkçe, uygulamalı ve katkıya açık bir çalışma rehberi. Git/GitHub, HTML/CSS,
JavaScript, Node.js, C#, ASP.NET Core, SQL, ORM/EF Core, Docker/Compose,
Caddy, test, hata ayıklama ve güvenli geliştirme temellerini birlikte ele alır.

**Güncel baskı: v0.2.0 · 23 Kasım 2026.**

## Kitabı oku

- **[PDF'yi aç veya indir](pdf/full-stack-calisma-rehberi.pdf)**
- [Bölümleri GitHub üzerinde oku](book/README.md)
- [Çalışan Node.js örneğini aç](examples/node-is-listesi/)
- [.NET API ve xUnit testleri](examples/dotnet-study/)
- [TypeScript / Express örneği](examples/ts-express/)
- [Doğrulama kapsamı ve sınırlar](VALIDATION.md)

44 bölüm ve yaklaşık 34.500 kelime; elle yazılacak örnekler, çözümlü alıştırmalar, hata avları, 24 haftalık rota,
bitirme projesi ve çalışan Node.js, .NET/xUnit, TypeScript/Express örnekleri içerir.
Güncel PDF'nin sayfa sayısı fonta ve üretim ortamına göre değişebilir.

Bu bir **çalışma kitabıdır**; tek başına mesleki seviye, iş veya sertifika
garantisi vermez. Okumak kadar yazmak, bozmak, test etmek ve geri bildirim
almak gerekir. Örnekler öğretim içindir; üretime hazır altyapı değildir.

## Kitap 2: Sıfırdan Mid-Level'a Yazılım

Aynı konuları çok daha ayrıntılı anlatan, yaklaşık 770 sayfalık ikinci bir Türkçe kitap da bu depoda. Ek olarak TypeScript, React, Linux, xUnit testleri, güvenlik ve mülakat soruları gibi konuları da kapsıyor.

- **[PDF'yi aç](kitap-2/sifirdan-mid-level-yazilim.pdf)** · [Kitap hakkında](kitap-2/README.md)

## Nereden başlamalı?

1. [Başlangıç ve çalışma yöntemi](book/00-baslangic.md)
2. [Bilgisayar, internet, Git/GitHub, HTML/CSS ve DevTools](book/01-temeller.md)
3. [JavaScript, asenkron kod, Node.js ve mini uygulama](book/02-javascript-node.md)
4. [C#/.NET, SQL, EF Core, Docker ve operasyon](book/03-backend-veri-operasyon.md)
5. [24 haftalık plan, bitirme projesi ve terim rehberi](book/04-uygulama-plani.md)
6. [C#, xUnit, Git kurtarma, Linux/SSH ve TypeScript/Express pratiği](book/05-profesyonel-pratik.md)

## Node örneğini çalıştır

Node.js 24 veya uyumlu daha yeni bir sürüm kullan. Harici npm bağımlılığı yoktur.

```powershell
cd examples/node-is-listesi
npm test
npm start
```

Tarayıcı: **http://127.0.0.1:5310**. Bitirince aynı terminalde `Ctrl+C`.
HTTP senaryolarını otomatik doğrulamak için önce sunucuyu kapatıp
`node verify.mjs` çalıştır. Betik kendi boş portunu seçer ve yalnız kendi
başlattığı süreci kapatır.

Örnek yalnız localhost'a bağlanır; veriler bellektedir, yeniden başlatınca
silinir. Kimlik doğrulaması yoktur. Gerçek müşteri veya şifre kullanma.
.NET laboratuvarı hem kitapta adım adım kurulur hem examples/dotnet-study altında çalıştırılabilir dosyalarla bulunur.

## PDF'yi yeniden üret

Python 3.11+ ve Arial veya DejaVu fontları gerekir. Font dosyaları repoya
eklenmez. Windows'ta standart Arial; Linux'ta
`/usr/share/fonts/truetype/dejavu` aranır. Farklı yerdeyse `BOOK_FONT_DIR`
ortam değişkenini uygun klasöre ayarla.

```powershell
python -m venv .venv
.venv/Scripts/Activate.ps1
python -m pip install -r requirements.txt
python scripts/build_pdf.py
```

Linux/macOS'ta sanal ortam etkinleştirmesi `source .venv/bin/activate`
biçimindedir. Font kurulumunu işletim sistemine göre yap. Linux/macOS
PDF üretimi bu ilk baskıda ayrıca denenmedi; Windows koşusu doğrulandı.

## Katkı ve hatalar

Hata fark edersen bölüm/dosya, beklenen sonuç, gerçek sonuç ve en küçük
tekrar adımlarıyla issue açın. Düzeltmeler PR ile gelir; kaynak Markdown
önce güncellenir, ilgili örnek kontrol edilir, PDF yeniden üretilir.
[Katkı rehberi](CONTRIBUTING.md)

## Yapay zekâ desteği ve sorumluluk

İlk taslak ve düzenleme OpenAI Codex ve alt ajanlarının desteğiyle hazırlandı.
Örneklerin belirli bir kısmı çalıştırıldı; bütün kod blokları veya bütün
işletim sistemleri test edilmiş değildir. İnsan incelemesi ve topluluk
düzeltmesine açıktır. [Kapsamı oku](VALIDATION.md).

Bakım ve yayın: [Murat AKTAŞ / Mur-47](https://github.com/Mur-47).

## Lisans

- Rehber metinleri ve PDF: **CC BY 4.0**. Atıf vererek paylaşabilir ve
  uyarlayabilirsin; lisans bağlantısını koruyun, değişiklikleri belirtin.
- Örnek kodlar, Markdown içindeki özgün kod örnekleri ve PDF üretim
  betikleri: **MIT**.
- Bağlantı verilen üçüncü taraf belgeleri, araçları ve fontları kendi
  koşullarına tabidir; bu depo onlara yeni lisans vermez.

Atıf örneği: “Sıfırdan Full Stack Geliştiriciliğe, Murat AKTAŞ (Mur-47), CC BY 4.0,
https://github.com/Mur-47/full-stack-calisma-rehberi”.

[Metin lisansı](LICENSE) · [Kod lisansı](LICENSE-CODE) · [Kaynaklar ve atıf](ATTRIBUTION.md)

## Yayımlamadan önce gizlilik kontrolü

Kişiye/kuruma özel arama terimlerini kaynak kodda tutma. Repo kökünde Git'in
dışladığı `.publication-private.json` dosyasına JSON string dizisi yaz veya
aynı diziyi `PUBLICATION_PRIVATE_TERMS` ortam değişkeninden ver. Terimlerin
kendisi hata çıktısına yazılmaz. Başka bir dosya için
`PUBLICATION_PRIVATE_TERMS_FILE` kullanabilirsin; repo içindeki politika
dosyası Git tarafından dışlanmış ve takipsiz olmalıdır.

```powershell
python -m unittest discover -s scripts -p 'test_*.py'
python scripts/check_publication.py
```

Özel terim listesi olmadan genel kontrolü bilerek çalıştırmak istersen
`python scripts/check_publication.py --allow-no-private-terms` kullan.
Bu kip yerel özel terim denetimini atladığını açıkça bildirir. Kaynak kod,
bağlantılar ve PDF metni taranır. Eski etiket ve Git geçmişi bu sürümde
yeniden yazılmamıştır; yeni politika bundan sonraki yayınlara uygulanır.
