
#init ve self
#kolayca ornekleyelim..

class Personel():
    def __init__(self,ad,soyad,perNo,sehir,telNo):
        self.ad=ad
        self.soyad=soyad
        self.perNo=perNo
        self.sehir=sehir
        self.telNo=telNo

personel1=Personel("Ali","Asaf","12354879","Kayseri","05002145484")
personel2=Personel("Eylul","Can","14658793","Ankara","05103214565")

print(personel1.ad)
print(personel1.sehir)            #Ali-Kayseri
print("\n")
print(personel2.ad)               #Eylul-Ankara
print(personel2.sehir)
