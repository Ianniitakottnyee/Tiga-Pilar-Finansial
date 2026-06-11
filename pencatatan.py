import anggota
import time
import perhitungan
import pengelolaan
import pencatatan

#==============================================================================================================================================
...
def Transaksi(mode=None):
    berhenti = False
    while berhenti is False:
        if mode is None:
            print("Pilih Menu:\n1. Pembagian Rata (Pembelian Item Yang Sama)\n2. Pembagian Per-item (Pembelian Item Yang Berbeda)")
        while True:
            if mode is None:
                menu = pencatatan.cek("Menu: ", "Menu Harus Berupa Angka!")
            else:
                menu = mode
            if menu > 2 or menu < 1:
                print("Menu Tidak Tersedia.")
                if mode is not None:
                    return
            else:
                break
        
        anggota.daftarAngguta(anggota.ambilAnggita())

        peserta = []
        i = 1
        print("Masukkan Nama Anggota Yang Ikut Dalam Transaksi. Ketik '/' Jika Sudah Selesai.")
        while True:
            ikut = input(f"{i}. ").title()
            if ikut == "/":
                break
            for terdaftar in pengelolaan.akses()[0]:
                if ikut == terdaftar["nama"]:
                    break
            else:
                print("Anggota belum terdaftar. Daftarkan terlebih dahulu!")
                berhenti = True
                break
            peserta.append(ikut)
            i += 1

        if berhenti == True:
            continue

        peserta = set(peserta)
        peserta = list(peserta)
        pembayar = pesertaSah("Pembayar: ", "Pembayar Belum Terdaftar, Ingin Menambahkannya Sebagai Anggota?(ya/tidak): ", "Silahkan Input Ulang Pembayar." )

        waktu = waktuSaatIni()
        deskripsi = input("Tambahkan Deskripsi: ")

        if menu == 1:
            perhitungan.pembagianRata(peserta=peserta, pembayar=pembayar, waktu=waktu, deskripsi=deskripsi)
        else:
            perhitungan.pembagianPerItem(peserta=peserta, pembayar=pembayar, waktu=waktu, deskripsi=deskripsi)
        print("Transaksi Berhasil Dicatat")
        return

#==============================================================================================================================================
...
def cek(pesan, eror):
    while True:    
        try:
            x = int(input(pesan))
            break
        except ValueError: print(f"\033[91m{eror}\033[0m")
    return x

...
def pesertaSah(pesan, eror, ulang):
    valid = input(pesan)
    try:
        aidi = int(valid)
    except ValueError: aidi = 0
    p = pengelolaan.akses()
    daftarAnggota = p[0]
    for nama in daftarAnggota:
        if valid == "." or valid == "/":
            return valid
            break
        if valid.lower() == nama["nama"].lower() or aidi == nama["id"]:
            return nama["nama"]
            break
    else:
        repeat = input(eror)
        if repeat.lower() == "ya":
            anggota.tambahkanAnggata()
            print("Berhasil menambahkan anggota baru!")
            return valid
        else:
            print(ulang)
            pesertaSah(pesan, eror, ulang)
            return valid

#==============================================================================================================================================
...
def waktuSaatIni():
    atimess = time.localtime()
    waktu = {"tahun" : atimess[0], "bulan" : atimess[1], "tanggal": atimess[2], "jam" : atimess[3], "menit": atimess[4], "detik": atimess[5]}
    bulan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    bulan_ = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    er = "error"
    for i in range(12):
        if waktu["bulan"] == bulan[i]:
            moon = bulan_[i]
            break
    if waktu["jam"]<10:
        if waktu["menit"]<10:
            if waktu["detik"]<10:
                return (f" {waktu['tanggal']} {moon} {waktu['tahun']} jam 0{waktu["jam"]}:0{waktu["menit"]}:0{waktu["detik"]}")
            else: return (f" {waktu['tanggal']} {moon} {waktu['tahun']} jam 0{waktu["jam"]}:0{waktu["menit"]}:{waktu["detik"]}")
        elif waktu["menit"]>=10 and waktu["detik"]<10:
            return (f" {waktu['tanggal']} {moon} {waktu['tahun']} jam 0{waktu["jam"]}:{waktu["menit"]}:0{waktu["detik"]}")
        else: return (f" {waktu['tanggal']} {moon} {waktu['tahun']} jam 0{waktu["jam"]}:{waktu["menit"]}:{waktu["detik"]}")
    elif waktu["jam"]>=10:
        if waktu["menit"]<10:
            if waktu["detik"]<10:
                return (f" {waktu['tanggal']} {moon} {waktu['tahun']} jam {waktu["jam"]}:0{waktu["menit"]}:0{waktu["detik"]}")
            else: return (f" {waktu['tanggal']} {moon} {waktu['tahun']} jam {waktu["jam"]}:0{waktu["menit"]}:{waktu["detik"]}")
        elif waktu["menit"]>=10 and waktu["detik"]<10:
            return (f" {waktu['tanggal']} {moon} {waktu['tahun']} jam {waktu["jam"]}:{waktu["menit"]}:0{waktu["detik"]}")
        else: return (f" {waktu['tanggal']} {moon} {waktu['tahun']} jam {waktu["jam"]}:{waktu["menit"]}:{waktu["detik"]}")
    else: return (f"{er.ljust(27)}")