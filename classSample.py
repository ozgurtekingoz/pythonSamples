# coding=utf-8

class Account:
    def __init__(self, isim, numara, bakiye):
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye

    def hesapBilgileri(self):
        print ("isim:{}".format(self.isim))
        print ("numara:{}".format(self.numara))
        print ("bakiye:{}".format(self.bakiye))

    def paraCek(self, miktar):
        print ("kalanPara:{}".format(self.bakiye - miktar))


acc = Account("test", 55555555, 88)
acc.hesapBilgileri()
acc.paraCek(33)
