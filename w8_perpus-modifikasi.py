#5210411232

class Perpustakaan :
    def __init__(self, kode, judul, subjek, lokasi, info) :
        self.kode = kode
        self.judul = judul      
        self.subjek = subjek
        self.lokasi = lokasi
        self.info = info

class Buku(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, isbn, pengarang, jmlhal, ukuran):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jmlhal = jmlhal        
        self.ukuran = ukuran      
           

    def Tampil(self) :
        print(f"Judul : {self.judul} <{self.kode}>")
        print(f"Pengarang : {self.pengarang}")
        print(f"Jumlah Halaman : {self.jmlhal}")
        print(f"Kategori : {self.subjek}\n")

class Majalah(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, volume, issue):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.volume = volume
        self.issue = issue

    def Tampil(self) :  #Overriding
        print(f"Judul : {self.judul} <{self.kode}>")
        print(f"Volume : {self.volume}")
        print(f"Issue : {self.issue}")
        print(f"Kategori : {self.subjek}\n")

class DVD(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, aktor, genre):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.aktor = aktor
        self.genre = genre     

    def Tampil(self) :  #Overriding
        print(f"Judul : {self.judul} <{self.kode}>")
        print(f"Aktor : {self.aktor}")
        print(f"Genre : {self.genre}")
        print(f"Kategori : {self.subjek}\n") 

#Objek Buku
buku_A = Buku("123", "Pemrograman Python", "Buku Cetak", "Rak 2", "Dipinjam", "945-884-98-05", "Yogi Syarif", 20, "25x15")
buku_B = Buku("124", "dasar dasar teknik IT", "Buku Ajar", "Rak 2", "Dipinjam", "945-194-110-100-1", "Navegs Pratama adiputra", 110, "20x25")
buku_C = Buku("125", "Algoritma & Teknik pemograman", "Buku Cetak", "Rak 2", "Ada", "945-654-604-20-3", "ade jodho maturidi", 150, "25x22")

#Objek Majalah
majalah_A = Majalah("234", "Dunia Komputer", "Majalah Cetak", "Rak 3", "Ada", "VII", "Komputer")
majalah_B = Majalah("235", "sistem informasi", "Majalah Cetak", "Rak 3", "Ada", "III", "Jaringan")
majalah_C = Majalah("236", "pengantar per codingan", "Majalah Cetak", "Rak 3", "Ada", "IV", "Komputer") 

#Objek DVD
dvd_A = DVD("312", "Shingeki no kyojin", "softcopy", "Rak 1", "Ada", "Mikasa", "Anime")
dvd_B = DVD("313", "Naruto shipuden", "softcopy", "Rak 1", "Dipinjam", "Naruto", "Anime")
dvd_C = DVD("314", "boruto movie", "softcopy", "Rak 1", "Dipinjam", "Boruto", "Anime")    

while True :
    print("=======================\n    SEARCH ITEM \n=======================")
    print("1. BUKU ") 
    print("2. MAJALAH")
    print("3. DVD")
    print("0. selesai")
    menu = input("Pilihan Menu : ") 

    if menu == '1' :
        print("\nMENU BUKU\n===============\n1. Tampil Buku")
        print("2. Cari Buku")   
        pilihan = input("Pilihan : ")  
        buku = [buku_A, buku_B, buku_C]

        if pilihan == '1' :
            print("\n==============================================")
            for buku in buku :
                buku.Tampil()

        elif pilihan == '2' :
            kode = input("Masukan Kode Buku\t: ")
            for x in buku :
                if kode == x.kode :
                    print("\n==============================================")
                    print(f"Judul : {x.judul}")
                    print(f"Letak : {x.lokasi}")    
                    print(f"Status : {x.info}\n")
                    print("==============================================")

    elif menu == '2' :
        print("\nMENU MAJALAH\n===============\n1. Tampil Data Majalah")
        print("2. Cari Majalah")        
        pilihan = input("Pilihan : ") 
        majalah = [majalah_A, majalah_B, majalah_C] 

        if pilihan == '1' :
            print("\n==============================================")
            for majalah in majalah :
                majalah.Tampil()

        elif pilihan == '2' :
            kode = input("Masukan Kode Majalah\t: ")
            for x in majalah :
                if kode == x.kode :
                    print("\n==============================================")
                    print(f"Judul : {x.judul}")
                    print(f"Letak : {x.lokasi}")
                    print(f"Status : {x.info}\n")
                    print("==============================================")

    elif menu == '3' :
        print("\nMENU DVD\n===============\n1. Tampil Data DVD")
        print("2. Cari DVD")
        pilihan = input("Pilihan : ")  
        dvd = [dvd_A, dvd_B, dvd_C]  

        if pilihan == '1' :
            print("\n==============================================")
            for dvd in dvd :
                dvd.Tampil()#

        elif pilihan == '2' :
            kode = input("Masukan Kode DVD\t: ")
            for x in dvd :
                if kode == x.kode :
                    print("\n==============================================")
                    print(f"Judul : {x.judul}")
                    print(f"Letak : {x.lokasi}")
                    print(f"Status : {x.info}\n")
                    print("==============================================")

    elif menu == '0' :
        print("TERIMA KASIH :)\n")
        break

    else : 
        print("\nPilihan Tidak Ada Menu\n")
    input("\nEnter Untuk Melanjutkan......")