#muchamad taufik nawawi
#5210411232

class Mahasiswa :
    def __init__ (self, nama, nim, prodi) :
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.__universitas = universitas

    def Tampil(self) :
        print(f"{self.nama} adalah mahasiswa {self.__universitas} prodi {self.prodi} dengan nim {self.nim}")

mahasiswa1 = Mahasiswa("taufik", "5210411232", "Informatika", "UGM")
mahasiswa2 = Mahasiswa("Zidni", "5210411217", "Informatika", "UTY")
mahasiswa3 = Mahasiswa("havin", "5210411212", "Informatika", "UST")
mahasiswa4 = Mahasiswa("ananda", "5210411247", "Informatika", "UNY")

mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4]
print("List Mahasiswa")
for mhs in mahasiswa :
    teks = '{} adalah mahasiswa {} dengan nim {}'. format(mhs.nama, mhs.prodi, mhs.nim )
    print(teks)
print("\n")