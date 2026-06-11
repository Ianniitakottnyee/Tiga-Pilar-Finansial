import os
import pencatatan
import anggota
import perhitungan
import time
import pengelolaan
import trans
suasana = time.localtime()

#==============================================================================================================================================
...
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
#==============================================================================================================================================
...
class Tree:                                                                         #Tree [11]
    def __init__(self, menu, action=None):
        self.menu = menu
        self.action = action
        self.children = []

    def tambahkanAnak(self, child):
        self.children.append(child)

    def tampilkanIan(self, level=0):
        print(" " * (level * 4) + self.menu)
        for index, child in enumerate(self.children, start=1):
            print(" " * (level * 4) + f"[{index}] {child.menu}")

    def pilihAnak(self, nomor):
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
#==============================================================================================================================================
...
def keluarAplikasi():
    print("=================  Terimakasih!!  =================")
    exit()
...
def pohon():
    akar = Tree("Menu Utama")

    tambahAnggota = Tree("Tambah Anggota", action=anggota.tambahkanAnggata)

    catatTransaksi = Tree("Catat Transaksi")
    pembagianRata = Tree("Pembagian Rata", action=lambda: pencatatan.Transaksi(mode=1))
    pembagianPerItem = Tree("Pembagian Per Item", action=lambda: pencatatan.Transaksi(mode=2))

    tampilkanTransaksi = Tree("Tampilkan Transaksi", action=lambda: trans.tampilkanTransaksi(trans.ambilAngga()))

    hutang = Tree("Hutang")
    tampilkanHutang = Tree("Tampilkan Hutang", action=lambda: perhitungan.relasi(tmplknHutang=False))
    cariHutang = Tree("Cari Hutang", action=lambda: perhitungan.relasi(pencarian=False))
    pembayaranHutang = Tree("Pembayaran Hutang", action=lambda: perhitungan.relasi(pembayaran=False))
    tampilkanPembayaran = Tree("Tampilkan Pembayaran", action=lambda: perhitungan.relasi(tmplknPembayaran=False))

    fiturTambahan = Tree("Fitur Tambahan")
    pengaturan = Tree("Pengaturan Anggota")
    tampilkanAnggota = Tree("Tampilkan Anggota", action=lambda: anggota.daftarAngguta(anggota.ambilAnggita()))
    editProfil = Tree("Edit Profil Anggota", action=lambda: anggota.editProfil())
    lihatProfil = Tree("Lihat Profil masing-masing Anggota", action=lambda: anggota.profilAnggeta(anggota.ambilAnggeta()))
    tampilkanRiwayatPerhitungan = Tree("Tampilkan Riwayat Perhitungan", action=lambda: perhitungan.relasi(tmplkanPerhitungan=False))
    backupData = Tree("Backup Data", action=pengelolaan.upbackup)
    ambilDataBackup = Tree("Ambil Data Dari Backup", action=pengelolaan.openbackup)

    keluar = Tree("Keluar", action=keluarAplikasi)

    akar.tambahkanAnak(tambahAnggota)
    akar.tambahkanAnak(catatTransaksi)
    akar.tambahkanAnak(tampilkanTransaksi)
    akar.tambahkanAnak(hutang)
    akar.tambahkanAnak(fiturTambahan)
    akar.tambahkanAnak(keluar)

    catatTransaksi.tambahkanAnak(pembagianRata)
    catatTransaksi.tambahkanAnak(pembagianPerItem)

    hutang.tambahkanAnak(tampilkanHutang)
    hutang.tambahkanAnak(cariHutang)
    hutang.tambahkanAnak(pembayaranHutang)
    hutang.tambahkanAnak(tampilkanPembayaran)

    fiturTambahan.tambahkanAnak(pengaturan)
    pengaturan.tambahkanAnak(tampilkanAnggota)
    pengaturan.tambahkanAnak(editProfil)
    pengaturan.tambahkanAnak(lihatProfil)

    fiturTambahan.tambahkanAnak(tampilkanRiwayatPerhitungan)
    fiturTambahan.tambahkanAnak(backupData)
    fiturTambahan.tambahkanAnak(ambilDataBackup)

    return akar

#==============================================================================================================================================
...
def inputMenu(menu):
    current = menu
    parent = []
    undoStak = []                                                                   #Stack [6]
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===================================================")
        print("================== HITUNG BARENG ==================")
        print("===================================================\n")

        current.tampilkanIan(level=len(parent))
        if parent:
            print(" " * (len(parent) * 4) + "[0] Kembali")

        print("\n===================================================")
        print(sambutan() + " " + pencatatan.waktuSaatIni())
        print("===================================================")
        user_input = input("Pilih menu: ").strip()
        if user_input.lower() in ['/undo', 'undo', '/back', 'back']:
            if undoStak:
                current = undoStak.pop()
                if parent:
                    parent.pop()
            else:
                print("Sudah berada di menu utama.")
                input("Tekan Enter untuk lanjut...")
            continue

        try:
            pilihan = int(user_input)
        except ValueError:
            print("Input harus berupa angka atau '/undo'.")
            input("Tekan Enter untuk lanjut...")
            continue

        if pilihan == 0 and parent:
            current = parent.pop()
            if undoStak:
                undoStak.pop()
            continue

        try:
            selected = current.pilihAnak(pilihan)
        except IndexError:
            print("Menu tidak valid.")
            input("Tekan Enter untuk lanjut...")
            continue

        if selected.children:
            parent.append(current)
            undoStak.append(current)
            current = selected
            continue

        if selected.action:
            selected.action()
        else:
            print("Menu belum diimplementasikan.")

        input("Tekan Enter untuk kembali ke menu utama...")
        current = menu
        parent = []
        undoStak = []

def tampilkanMenu():
    menu = pohon()
    inputMenu(menu)


tampilkanMenu()



"""
menu
    tambah anggota /

    catat transaksi /
        pembagian rata /
        pembagian per item /

     transaksi /
    
    hutang /
        hutang /
        search /
        pembayaran /

    fitur tambahan
        tampilkan anggota
        hapus anggota
        riwayat perhitungan
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
    print(sambutan() + " " + pencatatan.waktuSaatIni())
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
                        .History(p[1])
                except KeyError: print("Belum ada riwayat transaksi.")
                break
            elif r == 2:
                try:
                    if p[2] == []:
                        print("Riwayat hutang kosong.")
                    else:
                        .History_Hutang(p[2])
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
            .History_Perhitungan()
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
