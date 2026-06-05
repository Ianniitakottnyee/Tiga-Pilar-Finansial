import pencatatan
import pengelolaan


...
class graph:
    def __init__(self):
        self.hutang = {}

    def tambahOrang(self, nama):
        if nama not in self.hutang:
            self.hutang[nama] = {}

    def transaksiKeHutang(self, kumpulanTransaksi):
        for transaksi in kumpulanTransaksi:
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
                            hitem = list(item.keys())[0]
                            totalHarga += item[hitem]
                        self.tambahHutang(nama, pembayar, totalHarga)

    def tambahHutang(self, nama1, nama2, jumlah):
        self.tambahOrang(nama1)
        self.tambahOrang(nama2)
        if nama2 in self.hutang[nama1]:
            self.hutang[nama1][nama2] += jumlah
        else:
            self.hutang[nama1][nama2] = jumlah

    def netHutang(self):
        for nama1 in list(self.hutang):
            for nama2 in list(self.hutang[nama1]):
                if nama2 in self.hutang and nama1 in self.hutang[nama2]:
                    if self.hutang[nama1][nama2] > self.hutang[nama2][nama1]:
                        self.hutang[nama1][nama2] -= self.hutang[nama2][nama1]
                        del self.hutang[nama2][nama1]
                    elif self.hutang[nama1][nama2] < self.hutang[nama2][nama1]:
                        self.hutang[nama2][nama1] -= self.hutang[nama1][nama2]
                        del self.hutang[nama1][nama2]
                    else:
                        del self.hutang[nama1][nama2]
                        del self.hutang[nama2][nama1]

    def tampilkanHutang(self):
        self.hutang = {k: v for k, v in self.hutang.items() if v}
        
        if not self.hutang:
            print("Tidak ada hutang.")
            return
        
        print("+----+--------------------+--------------------+---------------+")
        print("| No |        NAMA        |  Berhutang Kepada  |     Jumlah    |")
        print("+----+--------------------+--------------------+---------------+")
        no = 0
        kosong = ""
        for nama1 in self.hutang:
            pertama = True
            no += 1
            print(f"| {no}. ", end = "")
            for nama2 in self.hutang[nama1]:
                if pertama == True:
                    print(f"| {nama1.ljust(18)} | {nama2.ljust(18)} | {str(self.hutang[nama1][nama2]).ljust(13)} |")
                    pertama = False
                    print("+----+--------------------+--------------------+---------------+")
                else:
                    print(f"| {kosong.ljust(2)} | {nama1.ljust(18)} | {nama2.ljust(18)} | {str(self.hutang[nama1][nama2]).ljust(13)} |")
                    print("+----+--------------------+--------------------+---------------+")

    def pembayaran(self, nama1, nama2, jumlah):
        if nama2 in self.hutang[nama1]:
            if self.hutang[nama1][nama2] > jumlah:
                self.hutang[nama1][nama2] -= jumlah
            elif self.hutang[nama1][nama2] < jumlah:
                sisa = jumlah - self.hutang[nama1][nama2]
                del self.hutang[nama1][nama2]
                self.tambahHutang(nama2, nama1, sisa)
            else:
                del self.hutang[nama1][nama2]
        else:
            print(f"{nama1} tidak berhutang kepada {nama2}")

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
    

    