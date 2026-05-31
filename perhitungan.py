import pencatatan
import pengelolaan
import tampilkan

data = pengelolaan.akses()
kumpulanTransaksi = data[1]

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
        for nama1 in self.hutang:
            for nama2 in self.hutang[nama1]:
                if nama1 in self.hutang[nama2]:
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
        for nama1 in self.hutang:
            for nama2 in self.hutang[nama1]:
                print(f"{nama1} berhutang {self.hutang[nama1][nama2]} kepada {nama2}")

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
    

def Net_Debt():
    p = pengelolaan.akses()
    debt = p[2]
    rihu = p[3]
    panjang = len(debt)
    waktu = pencatatan.Timeisit()
    srh = {"net": "waktu", "waktu": waktu}
    rihu.append(srh)
    try:    
        for i in range(panjang):
            for j in range(panjang):
                srh = {}
                jmlh = 0
                if i == j:
                    continue
                if debt[i]["jumlah"] < 0:
                    nama = debt[i]["nama"]
                    debt[i]["nama"] = debt[i]["ke"]
                    debt[i]["ke"] = nama
                    debt[i]["jumlah"] = debt[i]["jumlah"] / -1
                    srh = {"nama": debt[i]["ke"], "hutang": debt[i]["jumlah"], "ke": debt[i]["nama"], "net": "swap"}
                    rihu.append(srh)                 
                if debt[i]["nama"] == debt[j]["nama"] and debt[i]["ke"] == debt[j]["ke"]:
                    jmlh = debt[i]["jumlah"] + debt[j]["jumlah"]
                    srh = {"nama": debt[i]["nama"], "jumlah": f"{debt[i]["jumlah"]} + {debt[j]["jumlah"]} = {jmlh}", "ke": debt[j]["ke"], "net": "tambah"}
                    debt[i]["jumlah"] = jmlh
                    rihu.append(srh)
                    debt[j]["ke"] = ""
                elif debt[i]["nama"] == debt[j]["ke"] and debt[i]["ke"] == debt[j]["nama"]:
                    if debt[i]["jumlah"] > debt[j]["jumlah"]:
                        jmlh = debt[i]["jumlah"] - debt[j]["jumlah"]
                        srh = {"nama": debt[i]["nama"], "jumlah": f"{debt[i]["jumlah"]} - {debt[j]["jumlah"]} = {jmlh}", "ke": debt[i]["ke"], "net": "gabung"}
                        debt[i]["jumlah"] = jmlh
                        rihu.append(srh)
                        debt[j]["ke"] = ""
                    elif debt[i]["jumlah"] < debt[j]["jumlah"]:
                        jmlh = debt[j]["jumlah"] - debt[i]["jumlah"]
                        srh = {"nama": debt[j]["nama"], "jumlah": f"{debt[j]["jumlah"]} - {debt[i]["jumlah"]} = {jmlh}", "ke": debt[j]["ke"], "net": "gabung"}
                        debt[j]["jumlah"] = jmlh
                        rihu.append(srh)                        
                        debt[i]["ke"] = ""
                    else:
                        srh = {"nama": debt[i]["nama"], "jumlah": f"{debt[i]["jumlah"]} - {debt[j]["jumlah"]} = 0", "ke": debt[i]["ke"], "status": "Lunas", "net": "gabung"}
                        rihu.append(srh)                        
                        debt[i]["ke"] = ""
                        debt[j]["ke"] = ""
    except IndexError: pass

    for i in range(panjang, -1, -1):
        try:
            if debt[i]["ke"] == "" or debt[i]["jumlah"] == 0.0:
                debt.pop(i)
        except IndexError: pass
    simpan = {"users": p[0], "riwayat": p[1], "hutang": debt, "rh": rihu}
    pengelolaan.Save(simpan)

    p = pengelolaan.akses()
    tampilkan.History_Hutang(p[2])
    return [debt, rihu]

def elimination():
    p = pengelolaan.akses()
    hutang = p[2]
    rihu = p[3]
    waktu = pencatatan.Timeisit()
    srh = {"net": "waktu", "waktu": waktu}
    rihu.append(srh)
    print("===================  Simplikasi  ==================")
    for x in hutang:
        for y in hutang:
            if x["ke"] == y["nama"]:
                if x["jumlah"] == y["jumlah"]:
                    x["ke"] = y["ke"]
                    srh = {"nama1": x["nama"], "nama2": y["ke"], "nama3": x["ke"], "jumlah": x["jumlah"], "net": "simpel"}
                    rihu.append(srh)
                    y["ke"] = ""
                elif x["jumlah"] > y["jumlah"]:
                    y["nama"] = x["nama"]
                    x["jumlah"] = x["jumlah"] - y["jumlah"]
                    srh = {"nama1": x["nama"], "nama2": x["ke"], "nama3": y["ke"], "jumlah": x["jumlah"], "net": "simpel"}
                    rihu.append(srh)
                elif x["jumlah"] < y["jumlah"]:
                    x["ke"] = y["ke"]
                    y["jumlah"] = y["jumlah"] - x["jumlah"]
                    srh = {"nama1": x["nama"], "nama2": y["nama"], "nama3": x["ke"], "jumlah": y["jumlah"], "net": "simpel"}
                    rihu.append(srh)
                else:
                    print("error")
    for i in range(len(hutang), -1, -1):
        try:
            if hutang[i]["ke"] == "":
                hutang.pop(i)
        except IndexError: pass
    simpan = {"users": p[0], "riwayat": p[1], "hutang": hutang, "rh": rihu}
    pengelolaan.Save(simpan)

    p = pengelolaan.akses()
    tampilkan.History_Hutang(p[2])