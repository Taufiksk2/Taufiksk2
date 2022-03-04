#muchamad taufik nawawi
#5210411232

class Menu :
    def __init__(self, nama, deskripsi, harga) :
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.__stok = stok

    def Tampil(self) :
        print(f"{self.nama} harga Rp {self.harga} \n---> {self.deskripsi} sisa stok {self.__stok}\n")

minuman1 = Menu("Jus Jambu", "Jus jambu merah tanpa gula", 8500, 24)
minuman2 = Menu("Jus Alpukat", "Jus alpukat dengan gula merah", 15000, 16)
minuman3 = Menu("Jus Alpukat Ektra Milk", "Jus alpukat dengan campuran susu cokelat dan tapuran kepingan choco", 15000, 8)
minuman4 = Menu("Red & Smooth", "Smoothie pisang susu dengan strawberry", 17500, 15)

makanan1 = Menu("lesah", "soto dengan santan", 12000, 40)
makanan2 = Menu("geprek nyos", "ayam geprek sambal matah", 25000, 25)
makanan3 = Menu("orak arik", "telur campur sayuran", 8000, 20)
makanan4 = Menu("magelangan", "nasigoreng mie", 10000, 30)

makanan = [makanan1, makanan2, makanan3, makanan4]
minuman = [minuman1, minuman2, minuman3, minuman4]

print("Daftar Menu Makanan")
for makan in makanan :
    teks = '{} harga Rp {}, {}'. format(makan.nama, makan.harga, makan.deskripsi)
    print(teks)
print("\nDaftar Menu Minuman")
for minum in minuman :
    teks = '{} harga Rp {}, {}'. format(minum.nama, minum.harga, minum.deskripsi)
    print(teks)
print("\n")