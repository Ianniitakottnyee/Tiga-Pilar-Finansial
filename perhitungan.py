import pencatatan
import pengelolaan

...
class graph:
    def __init__(self):
        self.hutang = {}
        self.perhitungan = []
    
    ...
    def tambahOrang(self, nama):
        if nama not in self.hutang:
            self.hutang[nama] = {}

    ...
    def tambahHutang(self, nama1, nama2, jumlah):
        self.tambahOrang(nama1)
        self.tambahOrang(nama2)
        if nama2 in self.hutang[nama1]:
            self.hutang[nama1][nama2] += jumlah
        else:
            self.hutang[nama1][nama2] = jumlah

    ...
    def transaksiKeHutang(self):
        for transaksi in pengelolaan.akses()[1]:
            if transaksi["kode"] == "r":
                peserta = transaksi["peserta"]
                pembayar = transaksi["pembayar"]
                hutangPerOrang = transaksi["harga"]
                for orang in peserta:
                    if orang != pembayar:
                        self.tambahHutang(orang, pembayar, hutangPerOrang)
            else:
                kumpulanPeserta = transaksi["peserta"]
                pembayar = transaksi["pembayar"]
                for perorang in kumpulanPeserta:
                    totalHarga = 0
                    if list(perorang.keys())[0] != pembayar:
                        nama = list(perorang.keys())[0]
                        for item in perorang[nama]:
                            totalHarga += item[list(item.keys())[0]]
                        self.tambahHutang(nama, pembayar, totalHarga)
    ...
    def pembayaranKeHutang(self):
        for pembayaran in pengelolaan.akses()[2]:
            hutang = pembayaran["jumlah"]
            pembayar = pembayaran["nama"]
            piutang = pembayaran["ke"]
            self.tambahHutang(pembayar, piutang, -hutang)

    ...
    def jaringHutang(self):
        for nama1 in list(self.hutang):
            for nama2 in list(self.hutang[nama1]):
                if nama2 in self.hutang and nama1 in self.hutang[nama2]:
                    if self.hutang[nama1][nama2] > self.hutang[nama2][nama1]:
                        hutang1 = self.hutang[nama1][nama2]
                        self.hutang[nama1][nama2] -= self.hutang[nama2][nama1]
                        self.perhitungan.append({"nama1": nama1, "nama2": nama2, "hutang1": hutang1, "hutang2": self.hutang[nama2][nama1], "sisa": self.hutang[nama1][nama2]})
                        del self.hutang[nama2][nama1]
                    elif self.hutang[nama1][nama2] < self.hutang[nama2][nama1]:
                        hutang1 = self.hutang[nama2][nama1]
                        self.hutang[nama2][nama1] -= self.hutang[nama1][nama2]
                        self.perhitungan.append({"nama1": nama1, "nama2": nama2, "hutang1": self.hutang[nama1][nama2], "hutang2": hutang1, "sisa": self.hutang[nama2][nama1]})
                        del self.hutang[nama1][nama2]
                    else:
                        self.perhitungan.append({"nama1": nama1, "nama2": nama2, "hutang1": self.hutang[nama1][nama2], "hutang2": self.hutang[nama2][nama1], "sisa": 0})
                        del self.hutang[nama1][nama2]
                        del self.hutang[nama2][nama1]

    ...
    def pencarianAin(self):
        self.hutang = {k: v for k, v in self.hutang.items() if v}
        nama = input("Masukkan nama yang ingin dicari: ").title()
        hutang = list(self.hutang.keys())
        for i in range(len(hutang)):
            if nama == hutang[i]:
                no = 0
                kosong = ""
                print("+----+--------------------+--------------------+---------------+")
                print("| No |        Nama        |  Berhutang Kepada  |     Jumlah    |")
                print("+----+--------------------+--------------------+---------------+")
                for nama2 in self.hutang[hutang[i]]:
                    print(f"| {no+1}. | {nama.ljust(18)} | {nama2.ljust(18)} | {str(self.hutang[hutang[i]][nama2]).ljust(13)} |")
                    no += 1
                    print("+----+--------------------+--------------------+---------------+")
                break
        else:
            print(f"{nama} Tidak Memiliki Hutang.")

    ...
    def pembayaran(self):
        self.tampilkanHutang()
        pembayaran = pengelolaan.akses()[2]
        ulang = True
        while ulang:
            nama1 = input("Siapa yang membayar: ").title()
            if nama1 not in self.hutang:
                print(f"{nama1} tidak memiliki hutang.")
                continue
            nama2 = input("Bayar ke: ").title()
            if nama2 not in self.hutang[nama1]:
                print(f"{nama1} tidak memiliki hutang ke {nama2}.")
                print("")
                continue
            jumlah = pencatatan.cek("Jumlah: ", "Jumlah Harus Berupa Angka!")
            if nama2 in self.hutang[nama1]:
                if self.hutang[nama1][nama2] > jumlah:
                    awal = self.hutang[nama1][nama2]
                    self.hutang[nama1][nama2] -= jumlah
                    riwayatPembayaran = {"awal": awal, "nama": nama1, "ke": nama2, "jumlah": jumlah, "waktu": pencatatan.waktuSaatIni(), "akhir": self.hutang[nama1][nama2]}
                elif self.hutang[nama1][nama2] < jumlah:
                    sisa = jumlah - self.hutang[nama1][nama2]
                    riwayatPembayaran = {"awal": self.hutang[nama1][nama2], "nama": nama1, "ke": nama2, "jumlah": jumlah, "waktu": pencatatan.waktuSaatIni(), "akhir": -sisa}
                    del self.hutang[nama1][nama2]
                    self.tambahHutang(nama2, nama1, sisa)
                else:
                    riwayatPembayaran = {"awal": self.hutang[nama1][nama2], "nama": nama1, "ke": nama2, "jumlah": jumlah, "waktu": pencatatan.waktuSaatIni(), "akhir": 0}
                    del self.hutang[nama1][nama2]
                
                pembayaran.append(riwayatPembayaran)
                pengelolaan.simpan(pembayaran=pembayaran)
                         
    ...
    def tampilkanHutang(self):
        hutang = self.hutang
        if not hutang:
            print("Tidak ada hutang.")
            return
        
        print("+----+--------------------+--------------------+---------------+")
        print("| No |        Nama        |  Berhutang Kepada  |     Jumlah    |")
        print("+----+--------------------+--------------------+---------------+")
        no = 0
        kosong = ""
        for nama1 in hutang:
            pertama = True
            if hutang[nama1]:
                no += 1
                print(f"| {no}. ", end = "")
            for nama2 in hutang[nama1]:
                if pertama == True:
                    print(f"| {nama1.ljust(18)} | {nama2.ljust(18)} | {str(hutang[nama1][nama2]).ljust(13)} |")
                    pertama = False
                    print("+----+--------------------+--------------------+---------------+")
                else:
                    print(f"| {kosong.ljust(2)} | {nama1.ljust(18)} | {nama2.ljust(18)} | {str(hutang[nama1][nama2]).ljust(13)} |")
                    print("+----+--------------------+--------------------+---------------+")

    ...
    def tampilkanRiwayatPembayaran(self):
        pembayaran = pengelolaan.akses()[2]
        if not pembayaran:
            print("Tidak ada riwayat pembayaran.")
            return
        print("+----+--------------------+--------------------+---------------+--------------------------------------------+")
        print("| No |       Nama         |     Bayar Ke       |    Jumlah     |                    Waktu                   |")
        print("+----+--------------------+--------------------+---------------+--------------------------------------------+")
        no = 0
        for x in pembayaran:
            print(f"| {no+1}. | {x['nama'].ljust(18)} | {x['ke'].ljust(18)} | {str(x['jumlah']).ljust(13)} | {str(x['waktu']).ljust(29)} |")
            no += 1
            print("+----+--------------------+--------------------+---------------+--------------------------------------------+")
    
    ...
    def tampilkanRiwayatPerhitungan(self):
        if not self.perhitungan:
            print("Tidak ada perhitungan yang tersedia.")
            return
        
        for x in self.perhitungan:
            print(f"[Simplikasi] {x["nama1"]}: {x["hutang1"]} <--> {x["nama2"]}: {x["hutang2"]} | {f"sisa: {x['sisa']}" if x["sisa"] != 0 else "Status: Lunas"}")
    
    def mengurutkanDevin(self):
        self.hutang = {k: v for k, v in self.hutang.items() if v}
        hutang = list(self.hutang.keys())
        print(hutang)
        while True:
            orang = input("Nama: ").title()
            if orang not in hutang:
                print(f"{orang} tidak memiliki hutang. Silahkan input ulang.")
                continue
            else:
                break

        while True:
            berdasarkan = input("Dari terbesar(b) / terkecil(k): ").lower()
            if berdasarkan == "b" or berdasarkan == "k":
                break
            else:
                print("Pilih berdasarkan pengurutan dari terbesar atau terkecil.")
                continue
        
        if berdasarkan == "b": 
            def mergeSort(arr):
                if len(arr) <= 1:
                    return arr

                mid = len(arr) // 2
                leftHalf = arr[:mid]
                rightHalf = arr[mid:]

                sortedLeft = mergeSort(leftHalf)
                sortedRight = mergeSort(rightHalf)

                return merge(sortedLeft, sortedRight)

            def merge(left, right):
                result = []
                i = j = 0

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        result.append(left[i])
                        i += 1
                    else:
                        result.append(right[j])
                        j += 1

                result.extend(left[i:])
                result.extend(right[j:])

                return result
        else:
            ...
        

"""================================================================================================================================================="""
...
def pembagianRata(peserta, pembayar, waktu, deskripsi):
    item = input("Nama Produk: ")
    while True:
        harga = input("Harga Satuan/Harga Total(s/t): ").lower()
        if harga == "s":
            harga = pencatatan.cek("Harga: ", "Harga Harus Berupa Angka!")
            break
        elif harga == "t":
            total = pencatatan.cek("Harga: ", "Harga Harus Berupa Angka!")
            harga = total/len(peserta)
            if harga % 10 != 0:
                if harga % 1000 < 500:
                    harga = harga - (harga % 1000)
                else:
                    harga = harga - (harga % 1000) + 1000
            break
        else:
            print(f"\033[91mPembagian Harus Berupa Satuan/Total \033[0m")
            continue
    transaksi = {"peserta": peserta, "pembayar": pembayar, "item": item, "harga": harga, "waktu": waktu, "deskripsi": deskripsi, "kode": "r"}
    global kumpulanTransaksi
    kumpulanTransaksi.append(transaksi)
    pengelolaan.simpan(transaksi=kumpulanTransaksi)

...
def pembagianPerItem(peserta, pembayar, waktu, deskripsi):
    print("Catat Item Yang Dibeli:")
    print("Ketik '/' Pada Item Untuk Selesai Menambahkan")
    persetuy = []
    for i in range(len(peserta)):
        print(f"{i+1}. {peserta[i]}:")
        kumpulanItem = []
        while True:
            item = input("Item: ")
            if item == "/":
                break
            harga = pencatatan.cek("Harga: ", "Harga Harus Berupa Angka!")
            x = {item: harga}
            kumpulanItem.append(x)
        y = {peserta[i]: kumpulanItem}
        persetuy.append(y)
    
    transaksi = {"peserta": persetuy, "pembayar": pembayar, "waktu": waktu, "deskripsi": deskripsi, "kode": "p"}
    global kumpulanTransaksi
    kumpulanTransaksi.append(transaksi)
    pengelolaan.simpan(transaksi=kumpulanTransaksi)  
    

    