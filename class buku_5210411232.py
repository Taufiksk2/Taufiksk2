#5210411232

class Buku :
    def __init__(self, judul, pengarang, tahun_terbit) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

buku1 = Buku("arah langkah", "helman biopsa", 2003)
buku2 = Buku("arah suci", "calya putri", 2009)
buku3 = Buku("candaan malikat", "ranendra", 2007)

bukus = [buku1, buku2, buku3]
print("List Buku")
for buku in bukus :
    teks = 'Buku {} karangan {} pertama kali diterbitkan tahun {}'.format(buku.judul, buku.pengarang, buku.tahun_terbit)
    print(teks) 
print("\n")