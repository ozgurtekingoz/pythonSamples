# w ==> write
# a==> append
# r==> read
# r+ ==> read and write

# file = open("test.txt", "a")
# file.write(" Test2")

# try:
#     file = open("test2.txt", "r")
# except FileNotFoundError:
#     print("File not found")

# try:
#     file = open("test.txt", "r")
#     # print(file.read())
#     # print(file.readline())#ilk satırı alıyor
#     # print(file.readline())#ikinci satırı alıyor.readline her satır için ayrı ayrı yazılabilir.
#     list = file.readlines()
#     print(list[0])
#     file.close()
# except FileNotFoundError:
#     print("File not found")

# otomatik dosya kapatıyor. bizim close dememize gerek kalmadan
# with  open("test.txt", "r") as file:
#     #print(file.read())
#     file.seek(3)#dosya içindeki verilen değerden sonra başla.bütün dosyayı çekmek yerine o sayıdan sonrakini çek anlamına gelir
#     print(file.read(4))#dosya içindeki 4 karekteri al

#     #sonuna veri eklemek
# with  open("test.txt", "a") as file:
#     file.write("Test4" + '\n')

# sonuna başına eklemek
# with open("test.txt", "r+") as file:
#     data = file.read()
#     file.seek(0)
#     data = "Test5\n" + data
#     file.write(data)

# ortaya data eklemek
with open("test.txt", "r+") as file:
    data = file.readlines()
    index = data.index('Test1\n')
    data.insert(index + 1, "Test6\n")
    file.seek(0)
    file.writelines(data)
