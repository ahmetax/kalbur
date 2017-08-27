"""
Bu betik ile addan ad yapan eklerle gövde türetimini gerçekleştireceğim.
Yazar: Ahmet Aksoy
İlk tarih: 20170810
Son değişiklik: 20170810
"""

# TODO: Yumuşayan köklerde ekler değişiyor

import kelime_bol as bol
import kelimelerine_ayir as ayir

SESLILER = 'aeıioöuü'
SERTLER = 'çfhkpsşt'

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

def kokoku():
    ff = "veri/KOKLER.txt"

    with open(ff, "r", encoding="utf-8") as f:
        for sat in f.readlines():
            sat = sat.strip().split()
            len_sat = len(sat)
            if len_sat <= 0:
                continue
            kelime = sat[0].strip()
            tipi=''
            try:
                tip = sat[1].strip()
            except:
                print("Hatalı kelime: ",kelime)
            if 'IS' in tip:
                if 'YUM' in tip:
                    tipi='YUM'
                yield kelime, tipi

def son_sesli(kelime,tipi):
    for i in range(1,len(kelime)+1):
        c=kelime[-i]
        if c in SESLILER:
            return c

def sertmi(kok,tipi):
    if 'YUM' in tipi:
        pass
    return kok[-1] in SERTLER

def lUk_eki(kok,tipi):
    sonsesli = son_sesli(kok,tipi)
    sert = sertmi(kok,tipi)
    yum= 'YUM' in tipi
    govde=kok
    if sonsesli=='i' or sonsesli=='e':
        govde=kok+'lik'
    elif sonsesli== 'ı' or sonsesli=='a':
        if yum:
            govde=kok+'lik'
        else:
            govde=kok+'lık'
    elif sonsesli== 'u' or sonsesli=='o':
        if yum:
            govde = kok + 'lük'
        else:
            govde=kok+'luk'
    elif sonsesli== 'ü' or sonsesli=='ö':
        govde=kok+'lük'
    else:
        print("sonsesli hatası: ",kok)
    return govde

def lU_eki(kok, tipi):
    sonsesli = son_sesli(kok,tipi)
    sert = sertmi(kok,tipi)
    yum= 'YUM' in tipi
    govde=kok
    if sonsesli=='i' or sonsesli=='e':
        govde=kok+'li'
    elif sonsesli== 'ı' or sonsesli=='a':
        if yum:
            govde = kok + 'li'
        else:
            govde=kok+'lı'
    elif sonsesli== 'u' or sonsesli=='o':
        if yum:
            govde = kok + 'lü'
        else:
            govde=kok+'lu'
    elif sonsesli== 'ü' or sonsesli=='ö':
        govde=kok+'lü'
    else:
        print("sonsesli hatası: ",kok)
    return govde

def sUz_eki(kok,tipi):
    sonsesli = son_sesli(kok,tipi)
    sert = sertmi(kok,tipi)
    yum= 'YUM' in tipi
    govde=kok
    if sonsesli=='i' or sonsesli=='e':
        govde=kok+'siz'
    elif sonsesli== 'ı' or sonsesli=='a':
        if yum:
            govde = kok + 'siz'
        else:
            govde=kok+'sız'
    elif sonsesli== 'u' or sonsesli=='o':
        if yum:
            govde = kok + 'süz'
        else:
            govde=kok+'suz'
    elif sonsesli== 'ü' or sonsesli=='ö':
        govde=kok+'süz'
    else:
        print("sonsesli hatası: ",kok)
    return govde

def CU_eki(kok,tipi):
    sonsesli = son_sesli(kok,tipi)
    sert = sertmi(kok,tipi)
    yum= 'YUM' in tipi
    govde=kok
    if sonsesli=='i' or sonsesli=='e':
        if sert:
            govde=kok+'çi'
        else:
            govde=kok+'ci'
    elif sonsesli== 'ı' or sonsesli=='a':
        if sert:
            if yum:
                govde = kok+'çi'
            else:
                govde=kok+'çı'
        else:
            if yum:
                govde=kok+'ci'
            else:
                govde=kok+'cı'
    elif sonsesli== 'u' or sonsesli=='o':
        if sert:
            if yum:
                govde=kok+'çü'
            else:
                govde=kok+'çu'
        else:
            if yum:
                govde=kok+'cü'
            else:
                govde=kok+'cu'
    elif sonsesli== 'ü' or sonsesli=='ö':
        if sert:
            govde = kok + 'çü'
        else:
            govde=kok+'cü'
    else:
        print("sonsesli hatası: ",kok)
    return govde


def CUl_eki(kok,tipi):
    sonsesli = son_sesli(kok,tipi)
    sert = sertmi(kok,tipi)
    yum= 'YUM' in tipi
    govde=kok
    if sonsesli=='i' or sonsesli=='e':
        if sert:
            govde=kok+'çil'
        else:
            govde=kok+'cil'
    elif sonsesli== 'ı' or sonsesli=='a':
        if sert:
            if yum:
                govde = kok+'çil'
            else:
                govde=kok+'çıl'
        else:
            if yum:
                govde=kok+'cil'
            else:
                govde=kok+'cı'
    elif sonsesli== 'u' or sonsesli=='o':
        if sert:
            if yum:
                govde=kok+'çül'
            else:
                govde=kok+'çul'
        else:
            if yum:
                govde=kok+'cül'
            else:
                govde=kok+'cul'
    elif sonsesli== 'ü' or sonsesli=='ö':
        if sert:
            govde = kok + 'çül'
        else:
            govde=kok+'cül'
    else:
        print("sonsesli hatası: ",kok)
    return govde

def CA_eki(kok,tipi):
    sonsesli = son_sesli(kok,tipi)
    sert = sertmi(kok,tipi)
    yum= 'YUM' in tipi
    govde=kok
    if sonsesli=='i' or sonsesli=='e':
        if sert:
            govde=kok+'çe'
        else:
            govde=kok+'ce'
    elif sonsesli== 'ı' or sonsesli=='a':
        if sert:
            if yum:
                govde = kok+'çe'
            else:
                govde=kok+'ça'
        else:
            if yum:
                govde=kok+'ce'
            else:
                govde=kok+'ca'
    elif sonsesli== 'u' or sonsesli=='o':
        if sert:
            if yum:
                govde=kok+'çe'
            else:
                govde=kok+'ça'
        else:
            if yum:
                govde=kok+'ce'
            else:
                govde=kok+'ca'
    elif sonsesli== 'ü' or sonsesli=='ö':
        if sert:
            govde = kok + 'çe'
        else:
            govde=kok+'ce'
    else:
        print("sonsesli hatası: ",kok)
    return govde

def cAk_eki(kok,tipi):
    sonsesli = son_sesli(kok,tipi)
    sert = sertmi(kok,tipi)
    yum= 'YUM' in tipi
    govde=kok
    if sonsesli=='i' or sonsesli=='e':
        govde=kok+'cek'
    elif sonsesli== 'ı' or sonsesli=='a':
        if yum:
            govde=kok+'cek'
        else:
            govde=kok+'cak'
    elif sonsesli== 'u' or sonsesli=='o':
        if yum:
            govde=kok+'cek'
        else:
            govde=kok+'cak'
    elif sonsesli== 'ü' or sonsesli=='ö':
        govde=kok+'cek'
    else:
        print("sonsesli hatası: ",kok)
    return govde

def cUk_eki(kok,tipi):
    sonsesli = son_sesli(kok,tipi)
    sert = sertmi(kok,tipi)
    yum= 'YUM' in tipi
    govde=kok
    if sonsesli=='i' or sonsesli=='e':
        govde=kok+'cik'
    elif sonsesli== 'ı' or sonsesli=='a':
        if yum:
            govde=kok+'cik'
        else:
            govde=kok+'cık'
    elif sonsesli== 'u' or sonsesli=='o':
        if yum:
            govde = kok + 'cük'
        else:
            govde=kok+'cuk'
    elif sonsesli== 'ü' or sonsesli=='ö':
        govde=kok+'cük'
    else:
        print("sonsesli hatası: ",kok)
    return govde

def DEkI_eki(kok,tipi):
    sonsesli = son_sesli(kok,tipi)
    sert = sertmi(kok,tipi)
    yum= 'YUM' in tipi
    govde=kok
    if sonsesli=='i' or sonsesli=='e':
        if sert:
            govde=kok+'teki'
        else:
            govde=kok+'deki'
    elif sonsesli== 'ı' or sonsesli=='a':
        if sert:
            if yum:
                govde = kok+'teki'
            else:
                govde=kok+'taki'
        else:
            if yum:
                govde=kok+'deki'
            else:
                govde=kok+'daki'
    elif sonsesli== 'u' or sonsesli=='o':
        if sert:
            if yum:
                govde=kok+'teki'
            else:
                govde=kok+'taki'
        else:
            if yum:
                govde=kok+'deki'
            else:
                govde=kok+'daki'
    elif sonsesli== 'ü' or sonsesli=='ö':
        if sert:
            govde = kok + 'teki'
        else:
            govde=kok+'deki'
    else:
        print("sonsesli hatası: ",kok)
    return govde


def DAm_eki():
    print()
    print("DAm_eki()")
    print("erdem, gündem, yöntem")

def Ar_eki():
    print()
    print("Ar_eki()")
    print("""birer,ikişer, üçer, dörder, beşer, altışar, yedişer, sekizer, dokuzar, onar, yirmişer, otuzar, kırkar, ellişer,
altmışar, yetmişer, seksener, doksanar, yüzer, biner""")

def DAs_eki():
    print()
    print("DAs_eki()")
    print("""adaş, anlamdaş, arkadaş, bağdaş, boydaş, çağdaş, dildaş, dindaş, duygudaş, düşündaş, gönüldaş, görevdaş, gündaş,
kadehdaş, kandaş, kardaş, karındaş, kıyıdaş, koldaş, korkudaş, mevkidaş, okuldaş, omuzdaş, oydaş, paydaş, sınırdaş,
sırdaş, soydaş, şekildaş, toplumdaş, ülküdaş, vatandaş, yandaş, yoldaş, zamandaş""")
    print("""evdeş, kardeş, kızkardeş, köydeş, özdeş, sütkardeş, türdeş, yöndeş""")
    print("""aşıktaş, ayaktaş, büzüktaş, denktaş, ırktaş, meslektaş, renktaş, sestaş, yurttaş""")
    print("""işteş, kökteş, sesteş""")

def Ak_eki():
    print()
    print("Ak_eki()")
    print("""solak, ortak, başak, benek, topak""")

def UmsU_eki():
    print()
    print("UmsU_eki()")
    print("""acımsı, beyazımsı, ekşimsi, fiilimsi, kırmızımsı, mavimsi, örümceğimsi, pembemsi, sarımsı, siyahımsı, yeşilimsi""")

def Imtirak_eki():
    print()
    print("Imtirak_eki()")
    print("""acımtırak, beyazımtırak, ekşimtırak, kırmızımtırak, mavimtırak, morumtırak, sarımtırak, siyahımtırak, yeşilimtırak""")

def Un_eki():
    print()
    print("Un_eki()")
    print("""yazın, kışın, güzün, demin, ansızın""")

def leyin_eki():
    print()
    print("leyin_eki()")
    print("""geceleyin, öğleyin, sabahleyin, akşamleyin""")

def sAl_eki():
    print()
    print("sAl_eki()")
    print("""duygusal, hayvansal, kalıtsal, kırsal, kumsal, kutsal, sayısal, tarımsal, toplumsal
kişisel, yüzeysel, bitkisel, küresel, belgesel""")

def sI_eki():
    print()
    print("sI_eki()")
    print("""camsı, çanaksı, dalsı, destansı, hayvansı, kadınsı, masalsı, olası, yabansı, yansı
dikensi, erkeksi, eylemsi, hissi, ipeksi, irsi, kutsi, mermersi, şahsi 
bulutsu, çocuksu, otsu, pamuksu
köksü""")

def IncI_eki():
    print()
    print("IncI_eki()")
    print("""birinci, ikinci, üçüncü, dördüncü, beşinci, altıncı, yedinci, sekizinci, dokuzuncu, onuncu, yirmini, otuzuncu,
kırkıncı, ellinci, altmışıncı, yetmişinci, sekseninci, doksanıncı, yüzüncü, bininci, sonuncu, kaçıncı""")

def tI_eki():
    print()
    print("tI_eki()")
    print("""cızırtı, çatırtı, fısıltı, gıcırtı, hırıltı, patırtı, şırıltı
geğirti, inilti
homurtu
gürültü""")

def z_eki():
    print()
    print("z_eki()")
    print("""ikiz, üçüz, dördüz, beşiz, altız""")

def kI_eki():
    print()
    print('kI_eki()')
    print("""akşamki, sabahki, öğlenki, geceki, yarınki, dünkü""")



if __name__=="__main__":
    kelimeler_dict={}
    for kok, tipi in kokoku():
        kelimeler_dict[kok]=tipi

    # kelimeler_dict=dict()
    # kelimeler_dict['celal']='YUM'

    for kelime in kelimeler_dict.keys():
        #print(lUk_eki(kelime,kelimeler_dict[kelime]))
        #print(lU_eki(kelime,kelimeler_dict[kelime]))
        #print(sUz_eki(kelime,kelimeler_dict[kelime]))
        #print(CU_eki(kelime,kelimeler_dict[kelime]))
        #print(CUl_eki(kelime,kelimeler_dict[kelime]))
        #print(CA_eki(kelime, kelimeler_dict[kelime]))
        #print(cAk_eki(kelime, kelimeler_dict[kelime]))
        #print(cUk_eki(kelime, kelimeler_dict[kelime]))
        print(DEkI_eki(kelime, kelimeler_dict[kelime]))

    DAm_eki()

    Ar_eki()

    DAs_eki()

    Ak_eki()

    UmsU_eki()

    Imtirak_eki()

    Un_eki()

    leyin_eki()
    sAl_eki()
    sI_eki()
    IncI_eki()
    tI_eki()
    z_eki()
