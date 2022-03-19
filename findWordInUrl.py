import operator

import requests
from bs4 import BeautifulSoup


def sozlukOlustur(tumKelimeler):
    kelimeSayisi = {}
    for kelime in tumKelimeler:
        if kelime in kelimeSayisi:
            kelimeSayisi[kelime] += 1
        else:
            kelimeSayisi[kelime] = 1
    return kelimeSayisi


def sembolleriTemizle(tumkelimeler):
    sembolsuzKelimeler = []
    semboller = "-,.;/'`:?\"(){}"
    for kelime in tumkelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol, "")
        if len(kelime) > 0:
            sembolsuzKelimeler.append(kelime)
    return sembolsuzKelimeler


url = "https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w#:~:text=Aziz%20Sancar%2C%20h%C3%BCcrelerin%20hasar%20g%C3%B6ren,Nobel%20Kimya%20%C3%96d%C3%BCl%C3%BC'n%C3%BC%20kazanm%C4%B1%C5%9Ft%C4%B1."

tumKelimeler = []

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

for kelimeGruplari in soup.find_all("p"):
    icerik = kelimeGruplari.text
    kelimeler = icerik.lower().split()
    for kelime in kelimeler:
        tumKelimeler.append(kelime)

tumKelimeler = sembolleriTemizle(tumKelimeler)

sozluk = sozlukOlustur(tumKelimeler)

for anahtar, deger in sorted(sozluk.items(), key=operator.itemgetter(1)):
    print(anahtar, deger)
