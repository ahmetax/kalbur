# -*- coding: utf-8 -*-
import time

"""
Proje: kalbur
Yazar: Ahmet Aksoy
Tarih: 27.10.2016
Bu modülde KOKLER.txt ve EKLER.txt dosyaları kullanılarak
kelimeler kök ve eklerine ayrılacak.
Çözümlenemeyen sözcükler ayrı bir dosyada toplanacak.
Son revizyon tarihi: 18.11.2016
"""
# TODO: 20161114 - KOKLER.txt dosyasına güncel bilgi dosyası eklenecek
"""
20161114:
KOKLER.txt dosyasının yanına taranacak dokümanlarda geçen ve
Türkçe açısından teorik olarak geçerli olmayan, ama özel durumlar için
geçerli sözcükler ek bir dosyada toplanabilir.
Böylece temel dosyalar daha durağan hale dönüşür. Eklemeler
diğer dosyada birikir. Belli aralarla bu bilgilerin bir kısmı
ana dosyaya aktarılır.
KOKLER.txt dosyası bozulmalara karşı bir önlem olarak daha korunaklı
bir formata dönüştürülebilir.
"""

YUMUSAT ={'ç':'c','t':'d','p':'b','k':'ğ'}
SERTLES ={'c':'ç','d':'t','b':'p','g':'k'}
SESLILER=list('aeıioöuüAEIİOÖUÜ')
KALINSESLILER=list('aıouAIOU')
INCESESLILER=list('eiöüEİÖÜ')
kokler_dict = {}
ekler_dict = {}
dusenler = {}

"""
sonsesli() ve kontrol_simdiki_zaman() fonksiyonlarını ekledim
"""
def sonsesli(s):
    l = len(s)
    i = l
    while i>0:
        if s[-1*i] in SESLILER:
            return s[-1*i]
        i-=1

    return None

def kontrol_simdiki_zaman(kelime):
    pos = kelime.find('yor')
    arases = kelime[pos-1]
    if arases not in ["ı","i","u","ü"]:
        return None,None
    kok = kelime[:pos-1]
    ek = kelime[pos-1:]
    # ek sözlükte varsa işlemlere devam et
    if ek in ekler_dict.keys():
        sses = sonsesli(kok)
        if sses in KALINSESLILER:
            if arases=='ı' or arases=='u':
                kok1=kok+'a'
                if kok1 in kokler_dict.keys():
                    return kok1, ek
        elif sses in INCESESLILER:
            if arases=='i' or arases=='ü':
                kok1=kok+'e'
                if kok1 in kokler_dict.keys():
                    return kok1,ek

    return None,None

def kokoku():
    for ab in [1,2]:
        if ab==1:
            ff = "veri/KOKLER.txt"
        else:
            ff = "veri/KOKOZLER.txt"
        with open(ff, "r", encoding="utf-8") as f:
            for sat in f.readlines():
                sat = sat.strip().split()
                if len(sat)<=0:continue
                kelime = sat[0].strip()
                tip = sat[1].strip()

                for ek in range(2, len(sat)):
                    tip += ' ' + sat[ek].strip()

                if kelime in kokler_dict.keys():
                    kokler_dict[kelime]+=' '+tip
                else:
                    kokler_dict[kelime]=tip

                # Ünlü düşmesi varsa, gereğini yap
                if 'DUS' in tip:
                    if len(kelime)>2:
                        kelime0= kelime
                        kelime = kelime[:-2]+kelime[-1]
                        dusenler[kelime0]=kelime
                        if kelime not in kokler_dict.keys():
                            kokler_dict[kelime] = tip + ' DUS'
                        else:
                            if 'DUS' not in kokler_dict[kelime]:
                                kokler_dict[kelime] = tip + ' DUS'


def ekoku():
    with open("veri/EKLER.txt", "r", encoding="utf-8") as f:
        for sat in f.readlines():
            sat = sat.strip().split()
            if len(sat)>=2:
                kelime = sat[0].strip()
                tip = sat[1].strip()
                if kelime in ekler_dict.keys():
                    if tip not in ekler_dict[kelime]:
                        ekler_dict[kelime]+= ' '+tip
                else:
                    ekler_dict[kelime]=tip

def ekkaydet():
    with open("veri/EKLER2.txt","w",encoding="utf-8") as f:
        for e in ekler_dict.keys():
            print("{} {}".format(e,ekler_dict[e]),file=f,flush=True)


def kok_tara(kelime):
    """
    İşlev: Verilen kelimeyi kök ve ek adaylarına ayırır. En uzun kökü döndürür.
    Return: tamam ve kök ikilisini döndürür. Kök tipi stringdir. tamam ise kök
    ve ek adaylarından oluşan bir listedir.
    """
    tamam = []
    tip=''
    # kelime kök listesinde varsa işlem tamam
    if kelime in kokler_dict.keys():
        tamam.append(kelime)
        return tamam, kelime
    else:   # Kelime aslında bir ek ise
        if kelime in ekler_dict.keys():
            tamam.append(":" + kelime)
            return tamam, None

    if len(kelime)<3: # kök de değil, ek de değil
        return [], None
    # Kelimenin tamamı kök sözlüğünde varsa başka şey aramaya gerek yok

    enuzunkok=''    # en uzun kökü belirlemek için
    basla=1
    # yor- eki varsa ses düşmesi ihtimalini değerlendir
    if "yor" in kelime:
        k1, e1 = kontrol_simdiki_zaman(kelime)
        if k1 != None and e1 != None:
            tamam.append(k1 + ":" + e1)
            basla=len(k1)
            if len(k1)>len(enuzunkok): enuzunkok=k1

    ll = len(kelime)
    for i in range(basla,len(kelime)+1):
        l=ll-i
        kok = kelime[:l]
        ek = kelime[l:]
        tip=''
        etip=''
        # Önce eki kontrol et. Çünkü kökte değişiklik olabiliyor.
        if ek in ekler_dict.keys():
            etip=ekler_dict[ek]
            if kok in kokler_dict.keys():
                tip = kokler_dict[kok]
                if ('KIS' in tip or 'OZ' in tip) and ('IS' not in tip):
                    tip += ' IS'
                # Aynı ek farklı kök tiplerine bağlanıyor olabilir
                etipler = etip.split(' ')
                for etp in etipler:
                    if etp in tip: # tipler uyuşuyor -> işlem tamam
                        tamam.append(kok + ":" + ek)
                        if len(kok) > len(enuzunkok): enuzunkok = kok
                        return tamam, enuzunkok
        if tip>'':
            # kökte yumuşama olmuş mu?
            if 'EKSI' in tip:
                try:
                    y = kok[-1]
                    if y in YUMUSAT.values():
                        for z in YUMUSAT.keys():
                            if YUMUSAT[z] == y:
                                kok = kok[:-1] + z
                                break
                except Exception as e:
                    print("YUM: {} {} : {}".format(kelime, kok, e))

            # kökte ünlü düşmüş olabilir. Kontrol et.
            if 'DUS' in tip:
                if kok in dusenler.keys():
                    kok = dusenler[kok]
        elif etip>'' and len(kok)>0:
            #try:
            y=kok[-1]
            if y in SERTLES.keys():
                for z in SERTLES.keys():
                    if z==y:
                        kok = kok[:-1]+SERTLES[z]
                        if kok in kokler_dict.keys():
                            # tipler uyuşuyor mu?
                            tip = kokler_dict[kok]
                            if ('KIS' in tip or 'OZ' in tip) and ('IS' not in tip):
                                tip += ' IS'
                            etipler = etip.split(' ')
                            for etp in etipler:
                                if etp in tip:  # tipler uyuşuyor -> işlem tamam
                                    tamam.append(kok + ":" + ek)
                                    if len(kok) > len(enuzunkok): enuzunkok = kok
                                    return tamam, enuzunkok

            #except Exception as e:
            #    print("SERT: {} {} : {}".format(kelime, kok, e))
            # Yumuşama olmuş mu?
            y=kok[-1]
            if y in YUMUSAT.values():
                for z in YUMUSAT.keys():
                    if YUMUSAT[z]==y:
                        kok = kok[:-1]+z
                        if kok in kokler_dict.keys():
                            # tipler uyuşuyor mu?
                            tip = kokler_dict[kok]
                            if ('KIS' in tip or 'OZ' in tip) and ('IS' not in tip):
                                tip += ' IS'
                            etipler = etip.split(' ')
                            for etp in etipler:
                                if etp in tip:  # tipler uyuşuyor -> işlem tamam
                                    tamam.append(kok + ":" + ek)
                                    if len(kok) > len(enuzunkok): enuzunkok = kok
                                    return tamam, enuzunkok

    if len(kok) > len(enuzunkok): enuzunkok = kok
    return tamam, enuzunkok

def main():
    user_input=[]
    say=0
    detayGoster = True
    t0 = time.perf_counter()

    #dosya='nana'
    #dosya='damdadelivar'
    #dosya='kirikayna'
    dosya='alice'
    fad="veri/{}-cozulenler.txt".format(dosya)
    ftamam = open(fad,"w",encoding="utf-8")
    fad="veri/{}-cozulen-kokler.txt".format(dosya)
    ftamamkok = open(fad,"w",encoding="utf-8")
    fname = "veri/{}_kelimeler.txt".format(dosya)
    with open(fname,"r") as f:
        for line in f.readlines():
            l = line.split()
            for k in l:
                user_input.append(k.strip())
                say+=1
                #if say>=1000: break

    # Daha dar bir kelime grubunu test etmek istersek
    #user_input = ["balığa","parmağının","derdimin" ,"yuzuyordu","yureğinin","yuzlerle","duzelten"]
    say = 0
    yoksay = 0
    fad="veri/{}-COZULEMEYEN.txt".format(dosya)
    fout = open(fad,"w",encoding="utf-8")
    for word in user_input:
        if len(word.strip())==0:continue
        sonuc, kok = kok_tara(word)
        if sonuc==None or len(sonuc)==0: mesaj=' bulunamadı'
        else: mesaj = ''
        say+=1
        if mesaj>'':
            yoksay+=1
            print("{} {} {} {} {} ".format(yoksay,say, word, sonuc, mesaj))
            print("{}".format(word),file=fout)
        else:
            if detayGoster == True:
                print("{} {} {} {}".format(say, word, sonuc, kok),file=ftamam)
                print("{} -> {}".format(word, kok), file=ftamamkok)

    print("Toplam süre: ",time.perf_counter()-t0)
    fout.close()
    if ftamam: ftamam.close()

def test_et():
    # uygun bir zamanda test mekanizması devreye sokulacak
    sozler ={'derdimin':'dert','metelik':'metelik','konuşabiliyordur':'konuş','bekliyorlar':'bekle',
             }
    hatasay=0
    for soz in sozler:
        try:
            sonuc, kok = kok_tara(soz)
            assert (sozler[soz]==kok)
            print("{} -> {} = {}".format(soz,sozler[soz],kok))
        except Exception as e:
            print("{} -> {} != {} SORUNLU".format(soz,sozler[soz],kok))
            hatasay+=1

    if hatasay==0:
        print("Testler sorunsuz tamamlandı.")
    else:
        print("{}/{} testte sorun var.".format(hatasay,len(sozler)))

if __name__ == "__main__":
    kokoku()
    ekoku()
    # ekkaydet()
    # exit()
    #test_et()
    main()
