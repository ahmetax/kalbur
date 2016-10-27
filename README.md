# bulgur

## BULGUR

Bu proje, Türkçe sözcükleri kök ve eklerine ayırmak amacıyla kullanılacak.

İlk aşamada Türkçe sözcük köklerini, tiplerini ve bağlantı ayrıcalıklarını içeren bir dosya oluşturdum.
Bu dosyanın adı KELIMELER.txt'dir.

KELIMELER.txt dosyasının içeriğini oluştururken, zemberek projesinden ve TDK web sitesinden yararlandım. Ayrıca Google, DuckDUckGo, Bing, Yandex gibi arama motorlarına başvurduğum zamanlar oldu.

Sözkonusu liste hala gözden kaçmış bazı hatalar içerebilir. Çalışmalar sırasında yakalanacak bu hataları da nasılsa kolayca düzeltiriz.

KELIMELER.txt dosyası yaygın kullanılan bazı özel isimleri de içermektedir. Yer ve şahıs isimleri ile kısaltmalar dilimizin önemli ögelerindendir. Normal koşullarda bunların çoğu kesme işareti ile takılarından ayrılmakta olsa da, günlük kullanımda bu kuralın çoklukla gözardı edildiğini görüyoruz. Bu nedenle onları da kök listesine dahil ettim. Özel durumlarda belki basit bir bayrak aracılığı ile çözümlemelerde özel isimlerin dikkate alınmamasını sağlayabiliriz.

Programlama dilimiz yine Python. Halen en son geçerli sürüm olan Python 3.5.2'yi kullanıyorum. Dolayısıyla, kullanmakta olduğum paketler de 3.5 uyumludur.

## ÇALIŞMA YÖNTEMİ

İlk aşamada sözcükleri sadece kök+ek olarak ayrıştırmayı planlıyorum. Eklerin kendi içindeki ögelerine ayrıştırılması bir başka çalışmanın konusu yapılabilir. Büyük olasılıkla bu projenin ikinci aşamasında bu konuyu da ele alırız.

"Kök"lerin bulunmasını -şimdilik- "ek"lerden daha fazla önemsiyorum. Çünkü kelime köklerine "derin öğrenme", "büyük veri", "yapa zeka" vb çalışmalarında daha fazla ihtiyaç duyuyoruz.

Daha ileride cümlelerin ögelerine ayrılması ve anlamlandırılması çalışmalarında "ek"ler yine ön plana çıkacaktır. Ama bu aşamada arka planda kalacaktır.

Kök-ek ayrımında temel olarak iki liste kullanacağız: kökler ve ekler.

Taranacak sözcükler ilk karakterinden son karakterine kadar parçalar halinde kök listesiyle karşılaştırılacak ve olası kök adayları bir liste halinde saptanacaktır. Her kök adayından artakalan harflerin oluşturduğu ek, ekler listesinde aranacak ve bulunursa bu ekin kök tipine uygun olup olmadığı sorgulanacaktır. Ek de uygunsa, kelime çözümlenmiş demektir.

Bu basitleştirilmiş çözümleme yönteminin çok kısa sürede sonuç vermesini umuyorum.

Bu çalışma, ileriki çalışmalar için yolumuzu güçlü bir şekilde aydınlatacaktır.

Ahmet Aksoy
27.10.2016
