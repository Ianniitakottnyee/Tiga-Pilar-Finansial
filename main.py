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


