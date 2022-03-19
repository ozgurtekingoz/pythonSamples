# sayi1 = input("sayı1: ")
# sayi2 = input("sayı2: ")
#
# try:
#     sayi2 = int(sayi2)
#     sayi1 = int(sayi1)
#     print(sayi1 / sayi2)
# except ValueError:
#     print("hatalı değer")
# except ZeroDivisionError:
#     print("sıfıra bölünemez")
# except:
#     print("bir hata oluştu")

try:
    dosya = open("yazilim.txt", "r")
except IOError:
    print("dosya bulunamadı")
finally:
    print("all done")
