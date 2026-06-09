import pencatatan
import pengelolaan


...
class PerhitunganNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class PerhitunganList:
    def __init__(self, initial=None):
        self.head = None
        self._len = 0
        if initial:
            self.extend_from_list(initial)

    def append(self, data):
        node = PerhitunganNode(data)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self._len += 1

    def extend_from_list(self, lst):
        for item in lst:
            self.append(item)

    def to_list(self):
        out = []
        cur = self.head
        while cur:
            out.append(cur.data)
            cur = cur.next
        return out

    def save(self):
        pengelolaan.simpan(perhitungan=self.to_list())

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next

    def __len__(self):
        return self._len

    def __bool__(self):
        return self._len > 0

class graph:
    def __init__(self):
        self.hutang = {}
        # load saved perhitungan (if any) into the singly linked list
        try:
            saved = pengelolaan.akses()[3]
        except Exception:
            saved = None
        self.perhitungan = PerhitunganList(initial=saved if isinstance(saved, list) else None)

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
                            totalHarga += item[list(item.keys())[0]]
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
                        awal = self.hutang[nama1][nama2]
                        self.hutang[nama1][nama2] -= self.hutang[nama2][nama1]
                        perhitungan = {"t1": awal, "nama1": nama1, "nama2": nama2, "t2": self.hutang[nama2][nama1], "akhir": self.hutang[nama1][nama2], "berhutang": nama1, "ke": nama2, "tipe": "simplikasi"}
                        del self.hutang[nama2][nama1]
                    elif self.hutang[nama1][nama2] < self.hutang[nama2][nama1]:
                        awal = self.hutang[nama2][nama1]
                        self.hutang[nama2][nama1] -= self.hutang[nama1][nama2]
                        perhitungan = {"t1": self.hutang[nama1][nama2], "nama1": nama1, "nama2": nama2, "t2": awal, "akhir": self.hutang[nama2][nama1], "berhutang": nama2, "ke": nama1, "tipe": "simplikasi"}
                        del self.hutang[nama1][nama2]
                    else:
                        perhitungan = {"t1": self.hutang[nama1][nama2], "nama1": nama1, "nama2": nama2, "t2": self.hutang[nama2][nama1], "akhir": 0, "tipe": "simplikasi"}
                        del self.hutang[nama1][nama2]
                        del self.hutang[nama2][nama1]
                    # record the simplification step into the linked list and persist
                    self.perhitungan.append(perhitungan)
                    try:
                        self.perhitungan.save()
                    except Exception:
                        pass

    def _clone_hutang(self):
        return {nama: debts.copy() for nama, debts in self.hutang.items()}

    def _net_hutang_map(self, hutang_map):
        for nama1 in list(hutang_map):
            for nama2 in list(hutang_map[nama1]):
                if nama2 in hutang_map and nama1 in hutang_map[nama2]:
                    if hutang_map[nama1][nama2] > hutang_map[nama2][nama1]:
                        hutang_map[nama1][nama2] -= hutang_map[nama2][nama1]
                        del hutang_map[nama2][nama1]
                    elif hutang_map[nama1][nama2] < hutang_map[nama2][nama1]:
                        hutang_map[nama2][nama1] -= hutang_map[nama1][nama2]
                        del hutang_map[nama1][nama2]
                    else:
                        del hutang_map[nama1][nama2]
                        del hutang_map[nama2][nama1]

    def tampilkanRiwayatPerhitungan(self):
        if not self.perhitungan:
            print("Tidak ada perhitungan yang tersedia.")
            return
        
        for x in self.perhitungan:
            if x['tipe'] == "simplikasi":
                try:
                    print(f"{x['nama1']} berhutang {x['t1']} ke {x['nama2']}, dan {x['nama2']} berhutang {x['t2']} ke {x['nama1']}. {x['berhutang']} berhutang ke {x['ke']} sebanyak {x['akhir']}.")
                except KeyError:
                    print(f"{x['nama1']} berhutang {x['t1']} ke {x['nama2']}, dan {x['nama2']} berhutang {x['t2']} ke {x['nama1']}. {x['akhir']}. Status: Lunas.")
            else:
                print(f"{x['nama1']} membayar hutang ke {x['nama2']} sebanyak {x['jumlah']}. sisa hutang = {x['awal']} - {x['jumlah']} = {x['akhir']}")
    def tampilkanHutang(self):
        hutang = self.hutangFinal()
        try:
            hutang = {k: v for k, v in hutang.items() if v}
        except AttributeError:
            hutang.popitem()

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
                
                # record this payment into persistent pembayaran history
                pembayaran.append(riwayatPembayaran)
                pengelolaan.simpan(pembayaran=pembayaran)

                # also record the change as a perhitungan node (linked list)
                try:
                    perhit = {"tipe": "pembayaran", "nama1": nama1, "nama2": nama2, "awal": riwayatPembayaran["awal"], "jumlah": riwayatPembayaran["jumlah"], "akhir": riwayatPembayaran["akhir"]}
                    self.perhitungan.append(perhit)
                    self.perhitungan.save()
                except Exception:
                    pass
                break


    def tampilkanRiwayatPembayaran(self):
        pembayaran = pengelolaan.akses()[2]
        if not pembayaran:
            print("Tidak ada riwayat pembayaran.")
            return
        
        print("+----+--------------------+--------------------+---------------+---------------------+")
        print("| No |       Nama         |     Bayar Ke       |    Jumlah     |       Waktu         |")
        print("+----+--------------------+--------------------+---------------+---------------------+")
        no = 0
        kosong = ""
        for x in pembayaran:
            print(f"| {no+1}. | {x['nama'].ljust(18)} | {x['ke'].ljust(18)} | {str(x['jumlah']).ljust(13)} | {str(x['waktu']).ljust(19)} |")
            no += 1
            print("+----+--------------------+--------------------+---------------+---------------------+")

    def hutangFinal(self): #transaksi + pembayaran = hutang final
        hutang = self._clone_hutang()
        hutang = {k: v for k, v in hutang.items() if v}
        pembayaran = pengelolaan.akses()[2]

        # Process each payment to reduce the corresponding debt without mutating self.hutang
        for x in pembayaran:
            berhutang = x['nama']  # person paying
            ke = x['ke']          # person receiving payment
            jumlah = x['jumlah']  # amount paid

            if berhutang in hutang and ke in hutang[berhutang]:
                hutang[berhutang][ke] -= jumlah
                if hutang[berhutang][ke] <= 0:
                    del hutang[berhutang][ke]

        # Net remaining hutang on the temporary copy
        self._net_hutang_map(hutang)
        hutang = {k: v for k, v in hutang.items() if v}
        return hutang

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
    

    