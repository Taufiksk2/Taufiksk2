#muchamad taufik nawawi
#5210411232

class Buku :
    def __init__(self, judul, pengarang, tahun_terbit) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.__jmlh_halaman = jmlh_halaman

    def Tampil(self) :
        print(f"Buku {self.judul} karangan {self.pengarang} pertama kali diterbitkan tahun {self.tahun_terbit}")
        print(f"Buku {self.judul} jumlah halamannya adalah {self.__jmlh_halaman}\n")

buku1 = Buku("arah langkah", "helman biopsa", 2003, 188)
buku2 = Buku("arah suci", "calya putri", 2009, 232)
buku3 = Buku("candaan malikat", "ranendra", 2007, 147)

bukus = [buku1, buku2, buku3]
print("List Buku")
for buku in bukus :
    teks = 'Buku {} karangan {} pertama kali diterbitkan tahun {}'.format(buku.judul, buku.pengarang, buku.tahun_terbit)
    print(teks) 
print("\n")