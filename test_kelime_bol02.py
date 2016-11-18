# -*- coding: utf-8 -*-
import unittest
import kelime_bol02 as testi
"""
Proje: kalbur
Yazar: Ahmet Aksoy
Tarih: 14.11.2016
Test işlemleri
Son revizyon tarihi: 15.11.2016
"""

def test_et():
    sozler ={'metelik':'metelik'}
    for soz in sozler:
        sonuc, kok = testi.kok_tara(soz)
        assert(soz==kok)

class TestStringMethods(unittest.TestCase):
    # test hazırlıkları
    def setUp(self):
        print ("Test setUp_:begin")
        testi.kokoku()
        testi.ekoku()
        print("Test setUp_:end")

    # test sonu
    def tearDown(self):
        print("Test tearDown_:begin")
        testi.kokler_dict={}
        testi.ekler_dict={}
        print("Test tearDown_:end")

    def test_kok_tara(self):
        sozler = {'metelik': 'metelik','konuşabiliyordur':'konuş',
                  'bekliyorlar':'bekle', 'geldiği':'gel',
                  'derdimin':'dert', 'ahenginden':'ahenk',
                  'dengiyle':'denk','balığın':'balık',
                  }
        for soz in sozler.keys():
            koku = sozler[soz]
            sonuc,kok = testi.kok_tara(soz)
            self.assertEqual(kok, koku)
            print(soz,kok,koku)

if __name__ == "__main__":
    unittest.main()
