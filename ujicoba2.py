import pencatatan
import pengelolaan
import perhitungan

data = pengelolaan.akses()
"""
transaksi + pembayaran > hutang > tampilkan hutang

transaksi = {"peserta": peserta, "pembayar": pembayar, "item": item, "harga": harga, "waktu": waktu, "deskripsi": deskripsi, "kode": r} rata

transaksi = {"peserta": persetuy, "pembayar": pembayar, "waktu": waktu, "deskripsi": deskripsi, "kode": p} peritem

peserta 1 > pembayar

nama 1 > nama 2 > jumlah

        y = [{peserta[i]: kumpulanItem},{peserta[i]: kumpulanItem},{peserta[i]: kumpulanItem}]
        kumpulanItem = [{"item": harga, "harga": harga}, {"item": item, "harga": harga}, {"item": item, "harga": harga}]

"""



    # Simpan transaksi ke dalam kumpulanTransaksi

class graph:
    def __init__(self):
        self.hutang = data[1]
        """y = [{peserta[i]: kumpulanItem},{peserta[i]: kumpulanItem},{peserta[i]: kumpulanItem}]."""

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
                    if perorang.keys() != pembayar:
                        for item in perorang[perorang.keys()]:
                            totalHarga += item["item"]
                    self.tambahHutang(perorang, pembayar, totalHarga)


            peserta = transaksi["peserta"]
            pembayar = transaksi["pembayar"]

            jumlahPeserta = len(peserta)
            if jumlahPeserta == 0:
                print("Tidak ada peserta dalam transaksi ini.")
                return


            jumlahPerOrang = sum(item["harga"] for part in transaksi["peserta"] for item in part["produk"]) / jumlahPeserta

            for orang in peserta:
                if orang != pembayar:
                    perhitungan.graph().tambahHutang(orang, pembayar, jumlahPerOrang)

    def tambahOrang(self, nama):
        if nama not in self.hutang:
            self.hutang[nama] = {}

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

transaksi = pengelolaan.akses()[1]
hutang = graph().transaksiKeHutang(transaksi)

print("Hutang setelah transaksi:")
graph().tampilkanHutang()