## KALBUR

Bu proje, Türkçe sözcükleri kök ve eklerine ayırmak amacıyla kullanılacak.

İlk aşamada Türkçe sözcük köklerini, tiplerini ve bağlantı ayrıcalıklarını içeren bir dosya oluşturdum.
Bu dosyanın adı KELIMELER.txt'dir.

KELIMELER.txt dosyasının içeriğini oluştururken, zemberek projesinden ve TDK web sitesinden yararlandım. Ayrıca Google, DuckDuckGo, Bing, Yandex gibi arama motorlarına başvurduğum zamanlar oldu.

Sözkonusu liste hala gözden kaçmış bazı hatalar içerebilir. Çalışmalar sırasında yakalanacak bu hataları da nasılsa kolayca düzeltiriz.

KELIMELER.txt dosyası yaygın kullanılan bazı özel isimleri de içermektedir. Yer ve şahıs isimleri ile kısaltmalar dilimizin önemli ögelerindendir. Normal koşullarda bunların çoğu kesme işareti ile takılarından ayrılmakta olsa da, günlük kullanımda bu kuralın çoklukla gözardı edildiğini görüyoruz. Bu nedenle onları da kök listesine dahil ettim. Özel durumlarda belki basit bir bayrak aracılığı ile çözümlemelerde özel isimlerin dikkate alınmamasını sağlayabiliriz.

Programlama dilimiz yine Python. Halen en son geçerli sürüm olan Python 3.5.2'yi kullanıyorum. Dolayısıyla, kullanmakta olduğum paketler de 3.5 uyumludur.

## ÇALIŞMA YÖNTEMİ

İlk aşamada sözcükleri sadece kök+ek olarak ayrıştırmayı planlıyorum. Eklerin kendi içindeki ögelerine ayrıştırılması bir başka çalışmanın konusu yapılabilir. Büyük olasılıkla bu projenin ikinci aşamasında bu konuyu da ele alırız.

"Kök"lerin bulunmasını -şimdilik- "ek"lerden daha fazla önemsiyorum. Çünkü kelime köklerine "derin öğrenme", "büyük veri", "yapay zeka" vb çalışmalarında daha fazla ihtiyaç duyuyoruz.

Daha ileride cümlelerin ögelerine ayrılması ve anlamlandırılması çalışmalarında "ek"ler yine ön plana çıkacaktır. Ama bu aşamada arka planda kalabilirler.

Kök-ek ayrımında temel olarak iki liste kullanacağız: kökler ve ekler.

Taranacak sözcükler ilk karakterinden son karakterine kadar parçalar halinde kök listesiyle karşılaştırılacak ve olası kök adayları bir liste halinde saptanacaktır. Her kök adayından artakalan harflerin oluşturduğu ek, ekler listesinde aranacak ve bulunursa bu ekin kök tipine uygun olup olmadığı sorgulanacaktır. Ek de uygunsa, kelime çözümlenmiş demektir.

Bu basitleştirilmiş çözümleme yönteminin çok kısa sürede sonuç vermesini umuyorum.

Bu çalışma, eminim ki, ileriki çalışmalarımız için yolumuzu güçlü bir şekilde aydınlatacaktır.

Ahmet Aksoy
27.10.2016

# 29.10.2016: 
Projenin adını bulgur yerine kalbur olarak değiştirdim

# 14.11.2016: 

Kök ve eklerin ayrıştırılması çalışmalarında kullandığım temel kod dosyası kelime_bol02.py. Yeni sürümlerde bu dosyanın adı değişebilir.

İlk çalışmamda köklerdeki ses düşmesi ve yumuşama mekanizmalarını ele almıştım. 

a) Yumuşama mekanizmasının etkisi altındaki köklerin son karakterinde ç->c, t->d, p->b ve k->ğ şeklinde bir değişim meydana geliyor. Örneğin: kitap -> kitabı, taç -> taca, vb.
Bir köke yumuşama uygulanıp uygulanmayacağını KOKLER.txt dosyasındaki ilgili kökün yanına YUM terimini ekleyerek tanımlıyoruz. 

b) Ses düşmesi yaşayan köklerde ise, sondan ikinci harf olan ünlüler tamamen kayboluyor. Örneğin: sabır -> sabrı, hüzün -> hüznü, vb. Ses düşmesini ilgili kök satırına DUS terimini ekleyerek tanımlıyoruz.

Bu yaklaşım, Zemberek projesinde de kullanılmaktaydı. Temel verilerin okunaklığını ve anlaşılırlığını korumak amacıyla biz de bu yaklaşımı sürdürüyoruz. Ancak ileriki aşamalarda kısaltmalar için daha pratik terimler kullanabiliriz.

kelime_bol02.py dosyamızdaki son güncellemede şimdiki zaman eki "YOR" eklenen ve ünlüyle biten fiil köklerindeki son harf düşmesini ele aldık.

Bir sonraki işlem ise "NK" harfleriyle biten köklerin son harfindeki değişim olacak.

Benzer projelerdeki temel sıkıntının dokümantasyon olduğunun farkındayım. Hem kod yazıp, hem de bunları düzenli bir şekilde dokümante edebilmek oldukça zor bir uğraş. Buna rağmen, yapılan çalışmaların kalıcılığını sağlayabilmek için hem kodların daha kolay anlaşılır olmasına; hem de ek bilgilerle donatılmasına özen göstermenin gerekli olduğuna inanıyorum.

# 18.11.2016

KOKLER.txt, KOKOZLER.txt ve EKLER.txt dosyalarını veri klasörünün altına aldım.

KOKOZLER.txt dosyasını yeni ekledim. Bu dosya, KOKLER.txt dosyası ile aynı yapıdadır ve aynı amaca hizmet etmektedir. Yeni kökler bu dosyaya girilecek ve KOKLER.txt dosyasına hiç müdahale edilmeden yeni kökler sisteme tanıtılmış olacaktır. Bu dosyaya, özel durumlarda kullanılan argo sözcükler, belli bir dokümana özgü farklı sözcükler de eklenebilir. İleride, farklı meslek alanlarına vb yönelik teknik terimler bu veya benzeri dosyalarda toplanabilecektir.
Bu şekilde orijinal kök dosyası yanlışlıkla bozulmalara karşı korunmuş olacaktır.

Henüz devreye almamakla beraber, YAYGIN.txt isimli yeni bir dosyayı daha devreye sokacağım. Bu dosyada sıklıkla kullanılan yanlış sözcük veya sözcük grupları yer alacak. Örneğin: yalnış -> yanlış, gülegüle -> güle güle, vb.

EKLER.txt ve KOKLER.txt dosyalarında hala bazı düzeltmelere, ekleme ve çıkartmalara ihtiyaç var. Bu süreç tamamlanmadan kalbur kodlarını bir paket haline dönüştürmek istemiyorum. Yine de bu sürenin fazla uzayacağını sanmıyorum. Sonraki değişiklikleri yeni sürümler halinde sunmak daha pratik bir çözüm olacaktır.

Yumuşama kodları devreye girdi. Ayrıca basit bir "unit test" dosyasını devreye aldım. Kontrol amacıyla kullanılmasında yarar olan sözcükler test_kelime_bol02.py dosyasına eklenebilir.

# 19.11.2016

*Bartu Demirkıran* arkadaşımız mevcut kodların optimizasyonuna başladı. Özellikle makine öğrenmesi uygulamalarına girdiğimizde kullanacağımız kodların maksimum verimlilikte çalışıyor olması önemli. Şimdiden zaman kazanmaya başlıyoruz.

# 06.06.2017

Uzun bir aradan sonra sistemi yeniden harekete geçiriyorum.
Betik dosyalarının adlarında küçük değişiklikler yaptım. 
kokbul.py betiği komut modunda ve parametre alarak çalışabilir durumda. 
Parametre olarak çözümlenecek bir sözcük grubunu, veya -i ön eki ile belirtilen bir metin dosyası adı verilebilir. -o ile belirtilecek dosya adı şu anda işlevsiz. Daha sonra kullanılacak.
Genel kullanım şekli şöyle:
python3 kokbul.py -i input_dosya -o output_dosya -h kullanım
veya
python3 kokbul.py "sözcük grubu"

kelime_bol02.py betiği artık kullanılmayacak.

# 22.07.2017

EKLER.txt dosyasını yeniden düzenliyorum. Öyle görünüyor ki, boyutu oldukça küçülecek.
KOKLER.txt dosyasına da bazı eklemeler yapacağım. Bu dosyada ÖZEL isimlere yer vermeyeceğim. Bu tür sözcükler KOKOZLER.txt dosyasında veya ayrı dosyalarda tutulacak. Ayrı -özel- kök dosyaları, farklı alanlardaki metinleri tararken işimizi kolaylaştırabilir. Örneğin tıbbi metinleri sadece Türkçe köklere göre taramak, oldukça dar ve eksik sonuçlar elde etmemize neden olacaktır. 

