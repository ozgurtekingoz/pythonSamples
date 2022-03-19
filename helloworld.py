# coding=utf-8
from __future__ import division  # küsuratlı olarak bölmek
import recursiveFuncSample
#from recursiveFuncSample import * #Üstteki importun farklı şekilde yapılması
#from recursiveFuncSample import recSum #Metot bazlı referans verilmesini sağlıyor

# Denemeler

"""
#print function
print("özgür " + "tekingöz")

#deger atama
my_name = "Sample"
print("Hello and welcome " + my_name + "!")

a = 3
b = 3.14
c = "python"
d = [1, 2, 3, 4, "Python"]
e = (1, 2, 3, 4, 5, "python")
f = {"elma": 2, "armut": 3}
g = True

#parametre tipi bastırma
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g))
print(a, b, c, d, e, f, g)

#4 işlem
print(2 + 3)
print(3 - 1)
print(2 * 3)
print(6 / 2)
print(10 / 9)  # küsuratlı bölme işlemi
print(10 // 9)  # tam sayı olarak bölme işlemi
print(10 % 9)  # kalan bulma

a = 5
b = 8
c = a + 12 * b
print(c)
x = 2 + 3
print("{} + {} = {}".format(2, 3, x))

a = "deneme1 "
b = "deneme2 "
c = "deneme3"
d = a + b + c
print(d)

a = "python "
print(a * 5)  # string ile integer çarpıldığında, integer değeri ne ise o kadar string ifade yazar

a = "*"
print(a * 1)
print(a * 2)
print(a * 3)
print(a * 4)
print(a * 5)

a = "python"
print (a[0], a[1], a[2])
print (len(a))
print (a[len(a) - 1])  # son elemanı bul
print(a[0:2])  # sıfırıncı indexden başla iki tane al
print(a[:2])  # baştan başla iki tane al(üsttekiyle aynı anlam ifade ediyor)
print(a[2:])  # ikinci indexden başla sona kadar git.
print(a[0::2])  # sıfırdan başlayarak  ikişer atlayarak sona kadar git.
print(a[::2])  # sıfırdan başlayarak  ikişer atlayarak sona kadar git.(üsttekiyle aynı anlam ifade ediyor)

a = {"Elma": 1, "Armut": 2, "Portakal": 3}
print(a["Elma"])
print(a["Armut"])
print(a["Portakal"])

a = {1: "Elma", 2: "Armut", 3: "Portakal"}
print(a[1])
print(a[2])
print(a[3])

#kullanıcıdan input almak
a = input("ilk deger: ")
b = input("ikinci deger: ")
c = input("üçüncü deger: ")
print ("üç sayının toplamı = {} ".format(a + b + c))

if condition
<
>
<=
>=
==
!=
yas = input("yaşınızı giriniz:")

if yas == 20:
    print ("20 yaşında")
elif yas < 20:
    print ("20 yaşından küçük")
else:
    print ("20 yaşından büyük")

a = input("a:")
b = input("b:")
if a == 5 and b == 6:
    print(1)
else:
    print(0)

if a == 5 or b == 6:
    print(1)
else:
    print(0)

if not(a == 5):
    print(1)
else:
    print(0)

#döngüler
i = 0
while i < 6:
    print ("i:{}".format(i))
    i += 1

while i < 10:
    if i < 5:
        print ("i:{}".format(i))
    elif i == 5:
        i += 1
        continue
    elif i == 6:
        print ("i:{}".format(i))
    else:
        break
    i += 1
a = [1, 2, 3, 4, 5]
b = "python"
for item in a:
    print (item)
for item in b:
    print (item)
for sayi in range(0, 20, 2):  # 0 dan başla 20 ye kadar 2 şer atlayarak yaz
    print (sayi)


#fonksiyonlar

def nasilsin():
    print("nasılsın?")


def selamla(isim="İsimsiz"):
    print("Merhaba " + isim)


selamla("özgür")
selamla()
nasilsin()

def topla(a, b, c):
    print (a + b + c)
    return a + b + c

a = topla(3, 4, 5)
print (a + 5)


def selamla(isim="İsimsiz", soyadi="Soyadı", yas=0):
    print("Merhaba {} {}.Yaşınız {} ".format(isim, soyadi, yas))

selamla("özgür")
selamla()
selamla(isim="özgür", yas=35)
"""
sum = recursiveFuncSample.recSum([1, 4, 6, 78, 9])
print (sum)
