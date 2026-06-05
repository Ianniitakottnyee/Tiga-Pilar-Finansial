import os
import pencatatan
import anggota
import perhitungan
import tampilkan
import time
import pengelolaan
suasana = time.localtime()

def sambutan():
    try:
        pengelolaan.buka()
    except ValueError:
        kurawal = {}
        pengelolaan.Save(kurawal)

    if suasana[3]<4 or suasana[3]>19:
        return "Selamat malam!"
    elif suasana[3]<11:
        return "Selamat pagi!"
    elif suasana[3]<14:
        return "Selamat siang!"
    else:
        return "Selamat sore!"
    
class Tree:
    def __init__(self, menu, action=None):
        self.menu = menu
        self.action = action
        self.children = []

    def tambahkanTeks(self, child):
        self.children.append(child)

    def tampilkanIan(self, level=0):
        print(" " * (level * 4) + self.menu)
        for index, child in enumerate(self.children, start=1):
            print(" " * (level * 4) + f"[{index}] {child.menu}")

    def pilihChild(self, nomor):
        if nomor < 1 or nomor > len(self.children):
            raise IndexError("Menu tidak valid.")
        return self.children[nomor - 1]

    def temuknMenu(self, menu_name):
        if self.menu == menu_name:
            return self
        for child in self.children:
            found = child.temuknMenu(menu_name)
            if found:
                return found
        return None
    


def load_transaksi():
    return pengelolaan.akses()[1]


def show_transactions():
    transaksi = load_transaksi()
    if not transaksi:
        print("Belum ada riwayat transaksi.")
        return
    tampilkan.History(transaksi)


def build_hutang_graph():
    graf = perhitungan.graph()
    graf.transaksiKeHutang(load_transaksi())
    graf.netHutang()
    return graf


def show_hutang():
    graf = build_hutang_graph()
    graf.tampilkanHutang()


def search_hutang():
    graf = build_hutang_graph()
    graf.pencarianAin()


def pembayaran_hutang():
    graf = build_hutang_graph()
    nama1 = input("Nama yang berhutang: ").title()
    nama2 = input("Nama yang dihutangi: ").title()
    jumlah = pencatatan.cek(pesan="Jumlah pembayaran: ", eror="Input harus berupa angka!")
    graf.pembayaran(nama1, nama2, jumlah)


def clear_riwayat_perhitungan():
    data = pengelolaan.akses()
    pengelolaan.simpan(anggota=data[0], transaksi=data[1], hutang=data[2], perhitungan=[])
    print("Riwayat perhitungan dibersihkan.")


def exit_program():
    print("=================  Terimakasih!!  =================")
    exit()


def pohon():
    akar = Tree("Menu Utama")

    tambah_anggota = Tree("Tambah Anggota", action=anggota.tambahkanAnggata)

    catatTransaksi = Tree("Catat Transaksi")
    pembagian_rata = Tree("Pembagian Rata", action=lambda: pencatatan.Transaksi(mode=1))
    pembagian_per_item = Tree("Pembagian Per Item", action=lambda: pencatatan.Transaksi(mode=2))

    tampilkan_transaksi = Tree("Tampilkan Transaksi", action=show_transactions)

    hutang = Tree("Hutang")
    tampilkan_hutang = Tree("Tampilkan Hutang", action=show_hutang)
    search_hutang = Tree("Search Hutang", action=perhitungan.graph().pencarianAin)
    pembayaran_hutang = Tree("Pembayaran Hutang", action=perhitungan.graph().pembayaran)

    fitur_tambahan = Tree("Fitur Tambahan")
    tampilkan_anggota = Tree("Tampilkan Anggota", action=anggota.Show_Users)
    hapus_anggota = Tree("Hapus Anggota", action=anggota.Delete_User)
    tampilkan_riwayat_perhitungan = Tree("Tampilkan Riwayat Perhitungan", action=tampilkan.History_Perhitungan)
    bersihkan_riwayat_perhitungan = Tree("Bersihkan Riwayat Perhitungan", action=clear_riwayat_perhitungan)
    backup_data = Tree("Backup Data", action=pengelolaan.upbackup)
    ambil_data_dari_backup = Tree("Ambil Data Dari Backup", action=pengelolaan.openbackup)

    keluar = Tree("Keluar", action=exit_program)

    akar.tambahkanTeks(tambah_anggota)
    akar.tambahkanTeks(catatTransaksi)
    akar.tambahkanTeks(tampilkan_transaksi)
    akar.tambahkanTeks(hutang)
    akar.tambahkanTeks(fitur_tambahan)
    akar.tambahkanTeks(keluar)

    catatTransaksi.tambahkanTeks(pembagian_rata)
    catatTransaksi.tambahkanTeks(pembagian_per_item)
    hutang.tambahkanTeks(tampilkan_hutang)
    hutang.tambahkanTeks(search_hutang)
    hutang.tambahkanTeks(pembayaran_hutang)
    fitur_tambahan.tambahkanTeks(tampilkan_anggota)
    fitur_tambahan.tambahkanTeks(hapus_anggota)
    fitur_tambahan.tambahkanTeks(tampilkan_riwayat_perhitungan)
    fitur_tambahan.tambahkanTeks(bersihkan_riwayat_perhitungan)
    fitur_tambahan.tambahkanTeks(backup_data)
    fitur_tambahan.tambahkanTeks(ambil_data_dari_backup)

    return akar


def inputMenu(menu):
    current = menu
    parents = []
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===================================================")
        print("================== HITUNG BARENG ==================")
        print("===================================================\n")

        current.tampilkanIan(level=len(parents))
        if parents:
            print(" " * (len(parents) * 4) + "[0] Kembali")

        print("\n===================================================")
        print(sambutan() + " " + pencatatan.Timeisit())
        print("===================================================")
        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus berupa angka.")
            input("Tekan Enter untuk lanjut...")
            continue

        if pilihan == 0 and parents:
            current = parents.pop()
            continue

        try:
            selected = current.pilihChild(pilihan)
        except IndexError:
            print("Menu tidak valid.")
            input("Tekan Enter untuk lanjut...")
            continue

        if selected.children:
            parents.append(current)
            current = selected
            continue

        if selected.action:
            selected.action()
        else:
            print("Menu belum diimplementasikan.")

        input("Tekan Enter untuk kembali ke menu utama...")
        current = menu
        parents = []


def tampilkanMenu():
    menu = pohon()
    inputMenu(menu)


tampilkanMenu()
"""
menu
    tambah anggota

    catat transaksi
        pembagian rata
        pembagian per item

    tampilkan transaksi
    
    hutang
        tampilkan hutang  
        search
        pembayaran

    fitur tambahan
        tampilkan anggota
        hapus anggota
        tampilkan riwayat perhitungan
        bersihkan riwayat perhitungan
        backup data
        ambil data dari backup
    keluar


"""

'''
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===================================================")
    print("================== HITUNG BARENG ==================")
    print("===================================================")
    print(sambutan() + " " + pencatatan.Timeisit())
    print("menu:")
    print("     [1] Tambahkan anggota baru.")
    print("     [2] Catat transaksi.")
    print("     [3] Riwayat.")
    print("     [4] Pembayaran.")
    print("     [5] Fitur tambahan.")
    print("     [6] Keluar.")

    fitur = pencatatan.cek(pesan="Input angka untuk mengakses menu: ", eror="input tidak valid")
    if fitur == 0:
        ...
    if fitur == 1:
        print("==== Menu Tambahkan Anggota ====")
        anggota.Add_Users()
    elif fitur == 2:
        pencatatan.Transaction()
    elif fitur == 3:
        p = pengelolaan.akses()
        while True:
            print("Riwayat:\n1. Transaksi.\n2. Hutang.")
            r = pencatatan.cek(pesan="riwayat: ", eror="mode yang dipilih tidak valid!")            
            if r == 1:
                try:
                    if p[1] == []:
                        print("Belum ada riwayat transaksi.")
                    else:
                        tampilkan.History(p[1])
                except KeyError: print("Belum ada riwayat transaksi.")
                break
            elif r == 2:
                try:
                    if p[2] == []:
                        print("Riwayat hutang kosong.")
                    else:
                        tampilkan.History_Hutang(p[2])
                        print("[1] Rapikan\n[2] Simplikasi\n[3] Keluar")
                        simp = pencatatan.cek(pesan="menu: ", eror="Input hanya berbentuk angka!")
                        if simp == 1:
                            perhitungan.Net_Debt()
                        elif simp == 2:
                            perhitungan.elimination()
                except KeyError: print("Riwayat hutang kosong.")
                break
            else:
                print("mode tidak valid.")
    elif fitur == 4:
        pencatatan.pay()
    elif fitur == 5:
        print("========  Fitur Tambahan ========")
        print("")
        print("     [1] Tampilkan Anggota.")
        print("     [2] Hapus Anggota.")
        print("     [3] Tampilkan Riwayat Perhitungan.")
        print("     [4] Bersihkan Riwayat Perhitungan.")
        print("     [5] Backup Data.")
        print("     [0] Ambil data dari backup.")
        pilih = pencatatan.cek(pesan="pilih: ", eror="input tidak valid")
        if pilih == 1:
            anggota.Show_Users()
        elif pilih == 2:
            anggota.Delete_User()
        elif pilih == 3:
            tampilkan.History_Perhitungan()
        elif pilih == 4:
            pengelolaan.clearrh()
        elif pilih == 5:
            pengelolaan.upbackup()
        elif pilih == 0:
            pengelolaan.openbackup()
        else:
            print("fitur baru akan segera hadir!!")
    elif fitur == 6:
        print("=================  Terimakasih!!  =================")
        exit()
    else:
        print("Fiturnya cuman 4 wok\n")


if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print(f"\n=================  Terimakasih!!  =================")

'''
