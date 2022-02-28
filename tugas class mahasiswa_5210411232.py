#5210411232

class Mahasiswa :
    def __init__ (self, nama, nim, prodi) :
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

mahasiswa1 = Mahasiswa("taufik", "5210411232", "Informatika")
mahasiswa2 = Mahasiswa("Zidni", "5210411217", "Informatika")
mahasiswa3 = Mahasiswa("havin", "5210411212", "Informatika")
mahasiswa4 = Mahasiswa("ananda", "5210411247", "Informatika")

mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4]
print("List Mahasiswa")
for mhs in mahasiswa :
    teks = '{} adalah mahasiswa {} dengan nim {}'. format(mhs.nama, mhs.prodi, mhs.nim )
    print(teks)
print("\n")
