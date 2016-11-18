# -*- coding: utf-8 -*-
"""
Proje: kalbur
Yazar: Ahmet Aksoy
Tarih: 29.10.2016
Bu modülde ana fonksiyon, bir bütün halinde aldığı metin bloğunu
tekil sözcüklerine ayıracak ve bir liste halinde geri gönderecek.
Sözcükler inceltme işaretlerinden, rakamlardan temizlenecek ve küçük harfe dönüştürülecek.
Son revizyon tarihi: 14.11.2016
"""

BHARFX = "Iİ"
KHARFX = "ıi"
# AYRACLAR = ",\.;«»!?-:/\*+_=\"<>()'[]|º#&%“’”‘…–´—•`˜·"
NOKTALAMA = list("\"\'\.,/\\&%\+!\*/=(){}[]-_–:;?«»<>|^—¦")
RAKAMLAR = list("0123456789.,")
def noktalama_yok(kelime):
    s = [h for h in kelime if h not in NOKTALAMA else ' ']
    s = ''.join(s)
    # Eğer kelimede boşluk varsa, sonrasını at
    s = s.strip()
    p = s.find(' ')
    if p>0: s = s[:p]
    return s


def rakam_yok(kelime):
    s = [h for h in kelime if h not in RAKAMLAR]
    return "".join(s)

def kucukHarfYap(sozcuk):
    ss = ''
    for i in range(len(sozcuk)):
        ok = False
        for j in range(len(BHARFX)):
            if sozcuk[i]== BHARFX[j]:
                ss += KHARFX[j]
                ok = True
                break
        if ok == False:
            ss += sozcuk[i]
    ss = ss.lower()
    return ss

def inceltme_yok(sozcuk):
    s=""
    for harf in sozcuk:
        if harf=='â' or harf=='Â':
            s += 'a'
        elif harf == 'ê' or harf=='Ê':
            s += 'e'
        elif harf == 'û' or harf=='Û':
            s += 'u'
        elif harf == 'î' or harf=='Î':
            s += 'i'
        else:
            s+=harf
    return s


def kelimelerine_ayir(metin):
    liste = []
    hamliste = metin.split()
    hamliste = list(map(noktalama_yok, hamliste))
    hamliste = list(map(rakam_yok, hamliste))
    hamliste = list(map(inceltme_yok, hamliste))
    hamliste = list(map(kucukHarfYap, hamliste))
    return hamliste

if __name__ == "__main__":
    #dosya='nana'
    dosya='damdadelivar'
    fad="veri/{}.txt".format(dosya)
    with open(fad,"r") as f:
        metin = f.read()

    liste = set(kelimelerine_ayir(metin))

    print(liste)
    fad = "veri/{}_kelimeler.txt".format(dosya)
    with open(fad,"w") as f:
        for w in liste:
            if w.strip()>'':
                print("{}".format(w),file=f)

