import anggota
import time
import perhitungan
import pengelolaan
import tampilkan
import pencatatan

...
def Transaksi():
    print("Pilih Menu:\n1. Pembagian Rata (Pembelian Item Yang Sama)\n2. Pembagian Per-item (Pembelian Item Yang Berbeda)")
    while True:
        menu = pencatatan.cek("Menu: ", "Menu Harus Berupa Angka!")
        if menu > 2 or menu < 1:
            print("Menu Tidak Tersedia.")
        else:
            break
    
    #TO DO Tampilkan anggota
    anggota.Show_Users()

    peserta = []
    i = 1
    print("Masukkan Nama Anggota Yang Ikut Dalam Transaksi. Ketik '/' Jika Sudah Selesai.")
    while True:
        ikut = pesertaSah(f"{i}. ", "Anggota Belum Terdaftar, Ingin Menambahkannya Sebagai Anggota?(ya/tidak): ", "Silahkan Input Ulang Anggota.").title()
        
        if ikut == "/":
            break
        if ikut in peserta:
            print("Anggota Sudah Ditambahkan")
        else:
            peserta.append(ikut)
            i+=1

    pembayar = pesertaSah("Pembayar: ", "Pembayar Belum Terdaftar, Ingin Menambahkannya Sebagai Anggota?(ya/tidak): ", "Silahkan Input Ulang Pembayar." )

    waktu = Timeisit()
    deskripsi = input("Tambahkan Deskripsi: ")

    if menu == 1:
        perhitungan.pembagianRata(peserta=peserta, pembayar=pembayar, waktu=waktu, deskripsi=deskripsi)
    else:
        perhitungan.pembagianPerItem(peserta=peserta, pembayar=pembayar, waktu=waktu, deskripsi=deskripsi)
    print("Transaksi Berhasil Dicatat")
        
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

...
def Timeisit():
    atimess = time.localtime()
    waktu = {"tahun" : atimess[0], "bulan" : atimess[1], "tanggal": atimess[2], "jam" : atimess[3], "menit": atimess[4], "detik": atimess[5]}
    bulan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    bulan_ = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    marah = ""
    merah = ""
    er = "error"
    for i in range(12):
        if waktu["bulan"] == bulan[i]:
            moon = bulan_[i]
            marah = (f"{waktu["tanggal"]} {bulan_[i]} {waktu["tahun"]}")
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


def description(teks, panjang=60):
    chat = []
    for i in range(0, len(teks), panjang):
        chat.append(teks[i:i+panjang])
    for i in range(len(chat)):
        if chat[i][-1] != " ": 
            if chat[i] == chat[-1]:
                continue
            chat[i]= chat[i] + "-"
    return chat

def pay():
    p = pengelolaan.akses()
    hutang = p[2]
    rihu = p[3]
    tampilkan.History_Hutang(hutang)

    print("============  Pembayaran  ============")
    payer = None
    while payer == None:    
        payer = input("Siapa yang membayar: ")
        for i in range(len(hutang)):
            if payer.title() == hutang[i]["nama"]:
                break
        else:
            print(f"{payer.title()} tidak memiliki hutang. Silahkan input ulang pembayar.")
            payer = None

    to = None
    while to == None:    
        to = input("Bayar ke ")
        for i in range(len(hutang)):
            if to.title() == hutang[i]["ke"]:
                break
        else:
            print(f"{payer.title()} tidak memiliki hutang ke {to.title()}. Silahkan input ulang.")
            to = None    

    for i in range(len(hutang)):
        if payer.title() == hutang[i]["nama"] and to.title() == hutang[i]["ke"]:
            jumlah = cek("Jumlah yang dibayarkan: ", "input tidak valid!")
            hutangs = hutang[i]["jumlah"]
            hutang[i]["jumlah"] = hutang[i]["jumlah"] - jumlah
            
            perhitungan.Net_Debt()

            riwayathutang = {"nama": hutang[i]["nama"], "hutang": hutangs, "ke": hutang[i]["ke"], "bayar": jumlah, "sisa": hutang[i]["jumlah"], "status": f"Lunas" if {hutang[i]["jumlah"] == 0} else "Belum lunas", "net": "bayar"}
            rihu.append(riwayathutang)

            if hutang[i]["jumlah"] > 0:
                print(f"hutang {hutang[i]["nama"]} ke {hutang[i]["ke"]} sisa {hutang[i]["jumlah"]}")
            elif hutang[i]["jumlah"] == 0:
                print(f"hutang {hutang[i]["nama"]} ke {hutang[i]["ke"]} lunas!")
            else:
                sisa = hutang[i]["jumlah"]/-1
                cetak = "%g"% sisa
                print(f"{hutang[i]["ke"]} sekarang berhutang {cetak} ke {hutang[i]["nama"]}")

            simpan = {"users": p[0], "riwayat": p[1], "hutang": hutang, "rh": rihu}
            pengelolaan.Save(simpan)

            break