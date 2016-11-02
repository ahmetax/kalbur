# -*- coding: utf-8 -*-
import time

"""
Proje: kalbur
Yazar: Ahmet Aksoy
Tarih: 27.10.2016
Bu modülde KOKLER.txt ve EKLER.txt dosyaları kullanılarak
kelimeler kök ve eklerine ayrılacak.
Çözümlenemeyen sözcükler ayrı bir dosyada toplanacak.
Son revizyon tarihi: 29.10.2016
"""

YUMUSAT ={'ç':'c','t':'d','p':'b','k':'ğ'}
SERTLES ={'c':'ç','d':'t','b':'p','g':'k'}

kokler_dict = {}
ekler_dict = {}
dusenler = {}

def kokoku():
    with open("KOKLER.txt", "r", encoding="utf-8") as f:
        for sat in f.readlines():
            sat = sat.strip().split()
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
                    if kelime=='oğul':
                        tip = tip+''
                    kelime0= kelime
                    kelime = kelime[:-2]+kelime[-1]
                    dusenler[kelime0]=kelime
                    if kelime not in kokler_dict.keys():
                        kokler_dict[kelime] = tip + ' DUS'
                    else:
                        if 'DUS' not in kokler_dict[kelime]:
                            kokler_dict[kelime] = tip + ' DUS'

            # YUMUŞAMA
            if 'YUM' in tip:    # kökte yumuşama var mı?
                if kelime[-1] in YUMUSAT.keys():
                    kelime = kelime[:-1] + YUMUSAT[kelime[-1]]
                    if kelime not in kokler_dict.keys():
                        kokler_dict[kelime] = tip + ' EKSI'

def ekoku():
    with open("EKLER.txt", "r", encoding="utf-8") as f:
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
    with open("EKLER2.txt","w",encoding="utf-8") as f:
        for e in ekler_dict.keys():
            print("{} {}".format(e,ekler_dict[e]),file=f,flush=True)

def kok_tara(kelime):
    tamam = []
    tip=''
    if len(kelime)<3:
        tamam.append(kelime)
        return tamam, kelime
    for i in range(len(kelime)+1):
        kok = kelime[:i+1]
        if kok in kokler_dict.keys():
            tip = kokler_dict[kok]
            # ek kontrolü yap
            ek = kelime[i+1:]
            if ek=='':  # ek yoksa işlemi tamamla
                tamam.append(kok)
            else:
                # kök tipine göre ek kontrolü yap
                if 'KIS' in tip or 'OZ' in tip:
                    tipi= 'IS'
                else:
                    tipi=tip
                if tip!=tipi:
                    tip+=' '+tipi
                if ek in ekler_dict.keys():
                    tip2 = ekler_dict[ek]
                    # kök tiplerinden herhangi biri eklerden herhangi biriyle uyuşuyorsa doğru kabul et
                    for tip3 in tip.split():
                        if tip3 in tip2:
                            tamam.append(kok+":"+ek)

        # hiç kök adayı bulunamamışsa kelimeyi ekler içinde ara
        if len(tamam)==0:
            ek=kelime
            if ek in ekler_dict.keys():
                tamam.append(":" + ek)
    # En uzun kökü doğru kabul edelim
    kok = None
    l = len(tamam)
    if l==0:
        pass    # burada bir sorun var
    else:
        kok = tamam[l-1]
        p = kok.find(':')
        if p>=0:
            kok = kok[:p]

    # kökte ünlü düşmüş olabilir. Kontrol et.
    if 'DUS' in tip:
        if kok in dusenler.keys():
            kok = dusenler[kok]

    # kökte yumuşama olmuş mu?
    if 'EKSI' in tip:
        y= kok[-1]
        if y in YUMUSAT.values():
            for z in YUMUSAT.keys():
                if YUMUSAT[z]==y:
                    kok = kok[:-1]+z
                    break


    return tamam, kok

def main():
    user_input=[]
    say=0
    kokoku()
    ekoku()
    # ekkaydet()
    # exit()
    detayGoster = True
    t0 = time.perf_counter()
    ftamam = open("cozulenler.txt","w",encoding="utf-8")
    ftamamkok = open("cozulen-kokler.txt","w",encoding="utf-8")
    fname = "alice_kelimeler.txt"
    with open(fname,"r") as f:
        for line in f.readlines():
            l = line.split()
            for k in l:
                user_input.append(k.strip())
                say+=1
                #if say>=1000: break

    # Daha dar bir kelime grubunu test etmek istersek
    #user_input = ["etti","ediyor","ederek","ederlerse","etmemeliler"]
    say = 0
    yoksay = 0
    fout = open("COZULEMEYEN.txt","w",encoding="utf-8")
    for word in user_input:
        sonuc, kok = kok_tara(word)
        if len(sonuc)==0: mesaj=' bulunamadı'
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
    pass

if __name__ == "__main__":
    test_et()
    main()
