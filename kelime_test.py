# -*- coding: utf-8 -*-

import pydawg
import time

"""
26.10.2016
Bu modülde pydawg kullanımı ile direkt sözlük kullanımı arasında
dikkate değer bir hız farkı olup olmadığını kontrol edeceğim.
Okuma ve hazırlık aşamaları dikkate alınmayacak,
sadece arama ve print işlemlerinin aldığı toplam süre hesaplanacaktır.
"""

kelimeler_dict = {}

with open("KELIMELER.txt", "r", encoding="utf-8") as f:
    for sat in f.readlines():
        sat = sat.strip().split()
        kelime = sat[0].strip()
        tip = sat[1].strip()
        for ek in range(2, len(sat)):
            tip += ' ' + sat[ek].strip()
        kelimeler_dict[kelime]=tip

def write_dawg(D):
    with open('kelime001.bin','wb') as f:
        f.write(D.bindump())

def kok_tara(D,kelime):
    kokler = []
    for i in range(len(kelime)+1):
        kok = kelime[:i]
        if D.exists(kok):
            kokler.append(kok)
    return kokler

def kok_tara_dict(kelime):
    kokler = []
    for i in range(len(kelime)+1):
        kok = kelime[:i]
        if kok in kelimeler_dict:
            kokler.append(kok)
    return kokler

def main():
    D = pydawg.DAWG()
    # anahtarların yüklenmesi
    for key in sorted(kelimeler_dict):
        D.add_word_unchecked(key)

    # item bilgilerinin bir diziye yüklenmesi
    V = [None] * len(D)

    for key, value in kelimeler_dict.items():
        index = D.word2index(key)
        assert index is not None

        V[index - 1] = value

    # örnek sözcüklerin yüklenmesi
    """
    githuba büyük dosyaların yüklenmesi sorun yarattığı için gensozluk-kontrol.txt
    dosyasının yerine içinde en az bir milyon satır bulunan herhangi bir text dosyasını
    kullanabilirsiniz.
    Her satırda önce frekans sayısı sonra da sözcük bulunmaktadır.
    Dilerseniz frekans yerine rasgele bir sayı girebilir, ya da
    ilgili kod satırlarını revize ederek sadece sözcükleri kullanabilirsiniz.
    """
    user_input=[]
    say=0
    with open("gensozluk-kontrol.txt","r") as f:
        for line in f.readlines():
            l = line.split()
            if len(l)==2:
                user_input.append(l[1])
                say+=1
                if say>=1000000: break

    for tur in range(3):
        t0 = time.perf_counter()
        say=0
        kokler = []
        for word in user_input:
            if tur == 0:
                pass
            elif tur == 1:
                kokler = kok_tara(D, word)
            elif tur == 2:
                kokler = kok_tara_dict(word)

            say+=1
            #print(say, word, kokler)
        print("Toplam süre: ",time.perf_counter()-t0)

if __name__ == "__main__":
    main()
