# eylemden_eylem.py
# Python 3.5.2
"""
Bu betik ile eylemden eylem yapan eklerle gövde türetimini gerçekleştireceğim.
Yazar: Ahmet Aksoy
İlk tarih: 20170829
Son değişiklik: 20170829
"""

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
            if 'FI' in tip:
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

def DIr_eki(kok,tipi):
    sonsesli = son_sesli(kok,tipi)
    sert = sertmi(kok,tipi)
    yum= 'YUM' in tipi
    govde=kok
    if sonsesli=='i' or sonsesli=='e':
        if sert:
            govde=kok+'tir'
        else:
            govde=kok+'dir'
    elif sonsesli== 'ı' or sonsesli=='a':
        if sert:
            if yum:
                govde = kok+'tir'
            else:
                govde=kok+'tır'
        else:
            if yum:
                govde=kok+'dir'
            else:
                govde=kok+'dır'
    elif sonsesli== 'u' or sonsesli=='o':
        if sert:
            if yum:
                govde=kok+'tür'
            else:
                govde=kok+'tur'
        else:
            if yum:
                govde=kok+'dür'
            else:
                govde=kok+'dur'
    elif sonsesli== 'ü' or sonsesli=='ö':
        if sert:
            govde = kok + 'tür'
        else:
            govde=kok+'dür'
    else:
        print("sonsesli hatası: ",kok)
    return govde

def Il_eki(kok,tipi):
    sonsesli = son_sesli(kok,tipi)
    sert = sertmi(kok,tipi)
    yum= 'YUM' in tipi
    govde=kok
    if sonsesli=='i' or sonsesli=='e':
        govde=kok+'il'
    elif sonsesli== 'ı' or sonsesli=='a':
        if yum:
            govde=kok+'il'
        else:
            govde=kok+'ıl'
    elif sonsesli== 'u' or sonsesli=='o':
        if yum:
            govde = kok + 'ül'
        else:
            govde=kok+'ul'
    elif sonsesli== 'ü' or sonsesli=='ö':
        govde=kok+'ül'
    else:
        print("sonsesli hatası: ",kok)
    return govde

def In_eki():
    liste =['alın','bakın','çırpın','kaçın','kalkın', 'salın','sarın','sığın',
            'takın','tapın','taşın','tıkın','yırtın','ılın', 'değin','gerin',
            'gezin','giyin','silkin','şişin','tepin','yırtın','bulun','soyun',
            'tutun','çözün','dökün','dövün','görün','örtün','övün','sürtün',]
    return liste

def Ir_eki():
    liste =['artır','aşır','batır','kaçır','şaşır','taşır','yatır','bitir',
            'geçir','pişir','şişir','yetir','yitir','doğur','doyur','duyur',
            'savur','uçur','düşür','göçür']
    return liste

def Is_eki():
    liste =['atış','çatış','çıkış','kakış','kalkış','kapış','karış','katış',
            'kırpış','kızış','sığış','sıkış','tanış','tartış','yatış',
            'bitiş','çekiş','çeliş','deriş','eriş','geçiş','itiş','kesiş',
            'pekiş','seviş','bozuş','buluş','kokuş','koşuş','oluş','tutuş',
            'uçuş','uyuş','bölüş','büzüş','dönüş','görüş','küsüş','öpüş',
            'sürtüş','üşüş']
    return liste

def t_eki():
    liste =['acıt','akıt','aksat','aksırt','aktart','alçalt','aldırt',
            'anımsat','anırt','anlat','apart','arat','arıt','aşırt',
            'atlat','ayart','ayılt','belirt','benzet','boşalt','boşat',
            'boyat', 'böğürt', 'büyüt', 'çığırt', 'çıkart', 'çıtlat', 'düzelt',
            'fışırdat', 'hopurdat', 'höpürdet','ılıt','ısıt', 'kapat',
            'kaynat', 'kışkırt', 'kıvrat', 'kavrat', 'kızart', 'kirlet',
            'kokut', 'korkut', 'koyult','kuşat', 'öğret', 'sapıt', 'seğirt', 
            'sıvat', 'soğut', 'somurt', 'sürt', 'tıngırdat', 'tingirdet',
            'uğrat','uzat', 'üret', 'ürküt', 'üşüt', 'yassılt', 'yıprat',
            'yürüt', 'zangırdat']
    return liste

if __name__=="__main__":
    kelimeler_dict={}

    for kok, tipi in kokoku():
        kelimeler_dict[kok]=tipi

    #for kelime in kelimeler_dict.keys():
        # print(DIr_eki(kelime,kelimeler_dict[kelime]))
        #if not kelime[-1] in SESLILER:
        #    if not kelime[-1] in ['l']:
        #        print(Il_eki(kelime, kelimeler_dict[kelime]))


    print('\nIn_eki')
    print(In_eki())
    print('\nIr_eki')
    print(Ir_eki())
    print('\nIs_eki')
    print(Is_eki())
    print('\nt_eki')
    print(t_eki())
