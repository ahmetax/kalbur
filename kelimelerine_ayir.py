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
    s = [h if h not in NOKTALAMA else ' ' for h in kelime]
    s = ''.join(s)
    # Eğer kelimede boşluk varsa, sonrasını at
    s = s.strip()
    p = s.find(' ')
    if p > 0:
        s = s[:p]
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


def inceltme_harf(harf):
    """ inceltme yok fonksiyonu sadeleştirmesi"""
    harfler = {'â': 'a', 'Â': 'a', 'ê': 'e', 'Ê': 'e',
               'û': 'u', 'Û': 'u', 'î': 'i', 'Î': 'i'}
    return harfler[harf] if harf in harfler else harf


def inceltme_yok(sozcuk):
    s = [inceltme_harf(harf) for harf in sozcuk]
    return "".join(s)


def kelimelerine_ayir(metin):
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

