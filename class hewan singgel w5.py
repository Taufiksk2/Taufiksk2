#Muchamad Taufik Nawawi
#5210411232

# Single Inheritance

#Parent Class
class Hewan :   #5210411232
    def bersuara(self) :
        print("Kucing Bersuara")

# Anak class mewarisi parent class
class Kucing(Hewan) :
    def suara(self) :
        print("meong...meong")
#5210411232

#Objek
cat = Kucing()
cat.suara()#5210411232
cat.bersuara()
#5210411232