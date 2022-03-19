class Employee():
    def __init__(self, isim, maas, departman):
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileriGoster(self):
        print("İsim:", self.isim, "Maaş:", self.maas, "Departman:", self.departman)

    def zamYap(self, artisMiktarı):
        print("Maaşa zam yapıldı")
        self.maas += artisMiktarı

    def departmanDegistir(self, yeniDepartman):
        print("Departman Değiştirildi.")
        self.departman = yeniDepartman


# employee1 = Employee("Özgür köse", 3000, "IK")
# employee1.bilgileriGoster()

class Yonetici(Employee):
    def __init__(self, isim, maas, departman, kisiSayisi):
        #süper ile kalıtım alınan clasın metotları çağırılabilir
        super().__init__(isim, maas, departman)
        self.kisiSayisi = kisiSayisi

    def bilgileriGoster(self):
        print("İsim:", self.isim, "Maaş:", self.maas, "Departman:", self.departman, "Kişi Sayısı:", self.kisiSayisi)


yonetici = Yonetici("Bilge", 3200, "IK", 20)
yonetici.bilgileriGoster()