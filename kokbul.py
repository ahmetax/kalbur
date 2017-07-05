#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, getopt
import time
import kelime_bol as bol
import kelimelerine_ayir as ayir

"""
Yazar: Ahmet Aksoy
Betik: kokbul.py
Sürüm: 0.01
Tarih: 2017.05.30
Revizyon: 2017.07.05
Bu programcık, kendisine aktarılan kelimeleri bölüp
sadece köklerini, eklerini ve tiplerini döndürecek.
Girdi olarak string alacak.
Ya da girdiyi bir dosyadan okuyacak.
Noktalama işaretlerini ve rakamları yok edecek.
Kelimelerin köklerini, eklerini ve tiplerini bir liste halinde geri döndürecek.
"""
NOKTALAMA = r'.,:;-_<>/\?()[]''`{}&%+="«»'+"'!–--``''...′’‘~#``"

def Ii_degis(harf):
    """
    İşlev: I ve İ harfleri lower() ile doğru dönüşmüyor.
    Bu fonksiyon, gerekli düzeltmeyi yapıyor.
    Return: Düzeltilmiş Türkçe karakteri döndürür
    """
    if harf=='I':harf='ı'
    elif harf=='İ':harf='i'
    return harf

def kucukHarfTR(sozcuk):
    """
    İşlev: Girdi olarak bir string alır ve tüm karakterleri Türkçe küçük harfe çevirir.
    Return: Küçük harf Türkçe karakterlre dönüştürülen stringi döndürür
    """
    s =[Ii_degis(harf) for harf in sozcuk]
    return ("".join(s)).lower()

def noktalama_temizle(kl):
    kr=""
    for h in kl:
        if h in NOKTALAMA:
            continue
        kr+=h
    return kr

def inceltme_yok(kl):
    kr=""
    for h in kl:
        if h=='â': h='a'
        elif h=='ê': h ='e'
        elif h=='î': h ='i'
        elif h=='û': h ='u'
        elif h=='ô': h ='o'
        kr+=h
    return kr

def ktestet():
    """
    sozluk = {
        "dansın":"dans:ın",
        "resimler":"resim:ler",
        "duyduğumuz":"duy:duğumuz",
        "dönerdi":"döner:di",
        "çaya":"çay:a"

    }
    """
    sozluk={}
    satsay=0
    with open("veri/KOKBULTEST.txt","r") as f:
        for s in f.readlines():
            if s.startswith('#'): continue
            ss = s.split(',')
            if len(ss)==2:
                sozluk[ss[0]]=ss[1].strip()
                satsay+=1
    hatasay =0
    for k in sozluk.keys():
        tamam, kok, tip = bol.kok_tara(k)
        s = sozluk[k]
        t = tamam[0]
        if t!=s:
            #print(tamam[0], sozluk[k])
            try:
                assert(t == s)
            except:
                print("Assertion hatası: ",t,s)
                hatasay+=1
    if hatasay>0:
        print('Hatalı test sayısı = {}/{}'.format(hatasay,satsay))
    else:
        print ("Toplam {} test hatasız tamamlandı!".format(satsay))

def main(argv):
    ifile = ''
    ofile = ''
    metin = ''
    mesaj= "Kullanım: python3 kokbul.py -i input_dosya -o output_dosya -h kullanım"
    myopts, args = getopt.getopt(argv,"h:i:o")
    for o, a in myopts:
        if o == '-h':
            print(mesaj)
        elif o == '-i':
            ifile = a
        elif o == '-o':
            ofile = a
        else:
            metin = argv

    if myopts==[]:
        metin=str(argv)

    ss = ifile+metin
    if len(ss.strip())>2:
        #print(len(ss))
        pass
    else:
        print(mesaj)
        exit()

    sozcukler =[]
    t0 = time.perf_counter()
    if ifile>'':
        dosya = ifile
        print(dosya)
        with open(dosya,"r") as f:
            metin = f.read()

    liste = set(ayir.kelimelerine_ayir(metin))

    sozcukler = set(liste)
    for k in sozcukler:
        if len(k)==0:continue
        tamam, kok, tip = bol.kok_tara(k)
        #print("{} -> {} -> {}".format(k, kok, tamam))
        if len(tamam)>0: t=tamam[0]
        else: t = tamam
        if tip=='': tip='***'
        print("{},{} {}".format(k, t, tip))

    print("\nToplam süre = {}".format(time.perf_counter()-t0))

if __name__ == "__main__":
    ktestet()
    main(sys.argv[1:])
