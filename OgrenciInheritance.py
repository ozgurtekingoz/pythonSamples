class Ogrenci():
    def dersCalis(self):
        print("Öğrenci ders çalışıyor")


class Calisan():
    def calis(self):
        print("Personel şu anda çalışıyor")


# birden fazla sınıftan kalıtım alma
class Yazilimci(Ogrenci, Calisan):
    # hiç bir değişiklik yapmadan kalıtım aldığı sınıftaki özellikleri kullanması için pass anahtar sözcüğü
    # pass
    def dersCalis(self):
        print("Yazılımcı ders çalışıyor")


yazilimci = Yazilimci()
yazilimci.dersCalis()
yazilimci.calis()
