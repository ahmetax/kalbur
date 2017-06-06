# -*- coding: utf-8 -*-
import unittest
import kelime_bol02 as testi
import datetime
"""
Proje: kalbur
Yazar: Ahmet Aksoy
Tarih: 14.11.2016
Test işlemleri
Son revizyon tarihi: 06.06.2017
"""

class TestStringMethods(unittest.TestCase):
    # test hazırlıkları
    def setUp(self):
        print("Testing started at {}".format(datetime.datetime.now()))
        print("Test setUp_:begin")
        testi.kokoku()
        testi.ekoku()
        print("Test setUp_:end")

    # test sonu
    def tearDown(self):
        print("Test tearDown_:begin")
        testi.kokler_dict={}
        testi.ekler_dict={}
        print("Test tearDown_:end")
        print("Testing completed at {}".format(datetime.datetime.now()))

    def test_kok_tara(self):
        sozler = {'metelik': 'metelik','konuşabiliyordur':'konuş',
                  'bekliyorlar':'bekle', 'geldiği':'gel',
                  'derdimin':'dert', 'ahenginden':'ahenk',
                  'dengiyle':'denk','deliğin':'delik',
                  'alabalığın':'alabalık',
                  'balığın':'balık',
                  'aklından': 'akıl', 'sırada': 'sıra',
                  }
        for soz in sozler.keys():
            koku = sozler[soz]
            sonuc,kok = testi.kok_tara(soz)
            self.assertEqual(kok, koku)
            print(soz,kok,koku)

if __name__ == "__main__":
    unittest.main()
