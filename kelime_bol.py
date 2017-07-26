# -*- coding: utf-8 -*-
import time
import pickle

"""
Proje: kalbur
Modül: kelime_bol.py
Yazar: Ahmet Aksoy
Tarih: 30.05.2017
Bu modülde KOKLER.txt ve EKLER.txt dosyaları kullanılarak
kelimeler kök ve eklerine ayrılacak.
Çözümlenemeyen sözcükler ayrı bir dosyada toplanacak.
Son revizyon tarihi: 27.07.2017
"""

YUMUSAT = {'ç': 'c', 't': 'd', 'p': 'b', 'k': 'ğ', 'g':'ğ'}
SERTLES = {'c': 'ç', 'd': 't', 'b': 'p', 'g': 'k'}
SESLILER = {'ı', 'O', 'e', 'o', 'u', 'Ö', 'Ü', 'I',
            'ü', 'E', 'A', 'a', 'İ', 'ö', 'U', 'i'}
KALINSESLILER = {'ı', 'O', 'o', 'u', 'I', 'A', 'a', 'U'}
INCESESLILER = {'i', 'Ö', 'e', 'Ü', 'E', 'İ', 'ö', 'ü'}
kokler_dict = {}
ekler_dict = {}
dusenler = {}

"""
sonsesli() ve kontrol_simdiki_zaman() fonksiyonlarını ekledim
"""
def sonsesli(s):
    len_s = len(s)
    for i in range(len_s, 0, -1):
        if s[-i] in SESLILER:
            return s[-i]
    return None

def kok_fiil_mi(kok):
    return (kok in kokler_dict.keys()) and ('FI' in kokler_dict[kok])


def kontrol_simdiki_zaman(kelime):
    pos = kelime.find('yor')
    arases = kelime[pos-1]
    if arases not in ["ı","i","u","ü"]:
        return None,None

    kok = kelime[:pos-1]
    if len(kok)==4 and kok=='söyl':
        kok='söyle'
    elif len(kok)>2:
        # olumsuzlama eki olup olmadığını kontrol et
        if (kelime[pos-2]=='m') and (kelime[pos-3] in ['e','a']):
            pos1 = kelime.find('emiyor')
            if pos1>0:
                pos = pos1
                kok = kelime[:pos]
                if kok=='d':
                    kok='de'
                    pos+=1
                elif kok=='y':
                    kok='ye'
                    pos+=1
                elif kok =='diy':
                    kok = 'de'
                    pos=1
                elif kok =='yiy':
                    kok = 'ye'
                    pos=1
                if kok_fiil_mi(kok)==False:
                    pos+=1
                    kok =kelime[:pos]
                    pos+=1
                else:
                    pos+=1
            else:
                pos1 = kelime.find('amıyor')
                if pos1>0:
                    pos = pos1
                    kok = kelime[:pos]
                    if kok_fiil_mi(kok)==False:
                        pos+=1
                        kok =kelime[:pos]
                        pos+=1
                    elif kok_fiil_mi(kok+'a')==True:
                        kok+='a'
                        pos+=2
                    else:
                        pos+=1
    elif len(kok)==2:
        if kok=='ed': kok='et'
    if kok == 'diy': kok = 'de'
    elif kok == 'yiy': kok = 'ye'
    elif kok=='d': kok='de'
    elif kok=='y': kok = 'ye'
    ek = kelime[pos-1:]
    # ek sözlükte varsa işlemlere devam et
    if ek in ekler_dict.keys():
        if 'FI' in ekler_dict[ek]:
            if kok in kokler_dict.keys():
                if 'FI' in kokler_dict[kok]:
                   return kok,ek
    if ek in ekler_dict.keys():
        sses = sonsesli(kok)
        if sses in KALINSESLILER:
            if arases=='ı' or arases=='u':
                kok1=kok+'a'
                if kok1 in kokler_dict.keys():
                    return kok1, ek
        elif sses in INCESESLILER:
            if arases=='i' or arases=='ü':
                if kok not in ['de','ye']:
                    kok1=kok+'e'
                else:
                    kok1 = kok
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
                len_sat = len(sat)
                if len_sat <= 0:
                    continue
                kelime = sat[0].strip()
                try:
                    tip = sat[1].strip()
                except:
                    print("Hatalı kelime: ",kelime)

                for ek in range(2, len_sat):
                    tip += ' ' + sat[ek].strip()

                if kelime in kokler_dict.keys():
                    if tip not in kokler_dict[kelime]:
                        kokler_dict[kelime] += ' '+tip
                else:
                    kokler_dict[kelime] = tip

                # Ünlü düşmesi varsa, gereğini yap
                if 'DUS' in tip:
                    if len(kelime) > 2:
                        kelime0 = kelime
                        kelime = kelime[:-2]+kelime[-1]
                        dusenler[kelime0] = kelime
                        if kelime not in kokler_dict.keys():
                            kokler_dict[kelime] = tip + ' DUS'
                        else:
                            if 'DUS' not in kokler_dict[kelime]:
                                kokler_dict[kelime] = tip + ' DUS'


def ekoku():
    with open("veri/EKLER.txt", "r", encoding="utf-8") as f:
        for sat in f.readlines():
            sat = sat.strip().split()
            if len(sat) >= 2:
                kelime = sat[0].strip()
                tip = sat[1].strip()
                if kelime in ekler_dict.keys():
                    if tip not in ekler_dict[kelime]:
                        ekler_dict[kelime] += ' '+tip
                else:
                    ekler_dict[kelime] = tip

def ekkaydet():
    with open("veri/EKLER2.txt", "w", encoding="utf-8") as f:
        for e in ekler_dict.keys():
            print("{} {}".format(e, ekler_dict[e]), file=f, flush=True)

def uzatma_temizle(kelime):
    if kelime in ['www','ııı','vııı','xııı']:
        return kelime
    k=''
    kk=kelime+'.'
    while len(kk)>1:
        c=kk[0]
        k+=c
        for say in range(1,len(kk)+1):
            if kk[say]!=c:
                kk = kk[say:]
                break
        if say ==2: k += c

    return k


def kok_tara(kelime1):
    """
    İşlev: Verilen kelimeyi kök ve ek adaylarına ayırır. En uzun kökü döndürür.
    Return: tamam ve kök ikilisini döndürür. Kök tipi stringdir. tamam ise kök
    ve ek adaylarından oluşan bir listedir.
    """
    if len(kokler_dict)<1: kokoku()
    if len(ekler_dict)<1: ekoku()
    koklen = len(kokler_dict)
    eklen = len(ekler_dict)
    tamam = []
    tip=''

    # Kelime uzatmalarla deforme edilmişse, orijinal haline çevir
    kelime = uzatma_temizle(kelime1)
    # kelime kök listesinde varsa işlem tamam
    if kelime in kokler_dict.keys():
        tamam.append(kelime)
        tip = kokler_dict[kelime]
        return tamam, kelime, tip
    elif kelime in ekler_dict.keys():
        #tamam.append("YALIN EK: "+kelime)
        #tip = ekler_dict[kelime]
        #return tamam, kelime, tip
        pass
    else:   # Kelime aslında bir ek ise
        #if kelime in ekler_dict.keys():
        #    tamam.append(":" + kelime)
        #    return tamam, None
        pass

    if len(kelime)<3: # kök de değil, ek de değil
        if tamam == []: tamam.append(kelime)
        return tamam, kelime, tip
    # Kelimenin tamamı kök sözlüğünde varsa başka şey aramaya gerek yok

    enuzunkok=''    # en uzun kökü belirlemek için
    basla=1
    # yor- eki varsa ses düşmesi ihtimalini değerlendir
    if "yor" in kelime:
        k1, e1 = kontrol_simdiki_zaman(kelime)
        if k1 != None and e1 != None:
            tamam.append(k1 + ":" + e1)
            tip='FI'
            # demek ve yemek fiilleri için özel durum
            if k1 in['de','ye']:
                enuzunkok = k1
                #return tamam, enuzunkok, tip
            basla=len(k1)
            if len(k1)>len(enuzunkok): enuzunkok=k1
            return tamam, enuzunkok, tip

    # de ve ye için özel durumlar
    if kelime[0] in ['d','y']:
        for dyek in ['iyebil','iyeceğ','iyecek','iyerek','iyeme','iyen','iyip','iyince']:
            if dyek in kelime:
                e1 = kelime[1:]
                if e1 in ekler_dict.keys():
                    k1 = kelime[0]+'e'
                    tamam.append(k1+':'+e1)
                    tip='FI'
                    if len(k1)>len(enuzunkok): enuzunkok=k1
                    return tamam, enuzunkok, tip

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
                        # Ünlü düşmesi varsa kontrol et
                        if 'DUS' in tip:
                            if kok in dusenler.values():
                                for kik in dusenler.keys():
                                    if dusenler[kik]==kok:
                                        kok=kik
                                        break
                        tamam.append(kok + ":" + ek)
                        if len(kok) > len(enuzunkok): enuzunkok = kok
                        return tamam, enuzunkok, tip
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
                            if 'YUM' in tip:
                                if ('KIS' in tip or 'OZ' in tip) and ('IS' not in tip):
                                    tip += ' IS'
                                etipler = etip.split(' ')
                                for etp in etipler:
                                    if etp in tip:  # tipler uyuşuyor -> işlem tamam
                                        tamam.append(kok + ":" + ek)
                                        if len(kok) > len(enuzunkok): enuzunkok = kok
                                        return tamam, enuzunkok, tip

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
                                    return tamam, enuzunkok, tip

    if len(kok) > len(enuzunkok): enuzunkok = kok
    if tamam==[]: tamam.append(kelime)
    return tamam, enuzunkok, tip

def main():
    user_input=[]
    say=0
    detayGoster = True
    t0 = time.perf_counter()

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
    #user_input = ["sırada","aklından","balığa","parmağının","derdimin" ,"yuzuyordu","yureğinin","yuzlerle","duzelten"]
    #user_input = ["diyordu","diyormuş"]
    user_input = ['kaydığına']
    say = 0
    yoksay = 0
    fad="veri/{}-COZULEMEYEN.txt".format(dosya)
    fout = open(fad,"w",encoding="utf-8")
    for word in user_input:
        if len(word.strip())==0:continue
        sonuc, kok, tip = kok_tara(word)
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
                print("{} -> {} {}".format(word, kok, tip), file=ftamamkok)

    print("Toplam süre: ",time.perf_counter()-t0)
    fout.close()
    if ftamam: ftamam.close()

def test_et():
    sozler = {'metelik': 'metelik', 'konuşabiliyordur': 'konuş',
              'bekliyorlar': 'bekle', 'geldiği': 'gel',
              'derdimin': 'dert', 'ahenginden': 'ahenk',
              'dengiyle': 'denk', 'balığın': 'balık',
              'aklından':'akıl','sırada':'sıra',
              'olurlar':'ol','rabbimiz':'rab',
              }
    hatasay=0
    for soz in sozler:
        try:
            sonuc, kok, tip = kok_tara(soz)
            assert (sozler[soz] == kok)
            print("{} -> {} = {} {}".format(soz, sozler[soz], kok, tip))
        except Exception as e:
            print("{} -> {} != {} {} SORUNLU".format(soz, sozler[soz], kok, tip))
            hatasay += 1

    if hatasay == 0:
        print("Testler sorunsuz tamamlandı.")
    else:
        print("{}/{} testte sorun var.".format(hatasay, len(sozler)))

if __name__ == "__main__":
    #kokoku()
    #ekoku()
    # ekkaydet()
    # exit()
    #test_et()
    #main()
    kelime ='çoookkkk'
    kelime = 'eeeeyyyyvaaaahhhhhh'
    print(kelime, uzatma_temizle(kelime))
