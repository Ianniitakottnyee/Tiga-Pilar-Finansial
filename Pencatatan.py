import anggota
import time
import perhitungan
import pengelolaan
import tampilkan


def Transaction():
    print("Pilih mode:\n1. Pembagian Rata\n2. Pencatatan per-item")
    while True:
        mode = input("mode: ").lower()
        if mode == "1" or mode == "pembagian rata":
            mode = 1
            break
        elif mode == "2" or mode == "pencatatan per-item":
            mode = 2
            break
        else: print("mode tidak valid")

    anggota.Show_Users()
    participant = []
    payer = None
    while payer == None:
        payer = Validparticipant("Siapa yang bayar: ", "Pembayar belum terdaftar sebagai anggota. ingin menambahkannya sebagai anggota?(ya/tidak): ", "Silahkan input ulang pembayar!")
    ikut = input("Apakah pembayar ikut membeli? (tekan enter jika ya, ketik apa saja jika tidak)")
    if ikut == "":
        participant.append(payer)
    
    print(f"Siapa saja yang ikut membeli: (ketik \".\" jika selesai menambahkan)")
    i = 1
    while True:
        part = Validparticipant(f"{i}. ", "Anggota belum terdaftar, ingin menambahkannya sebagai anggota?(ya/tidak): ", "Silahkan input ulang anggota.")
        if part == ".": break
        if part in participant:
            print("Anggota sudah ditambahkan")
        else:
            participant.append(part)
            i+=1
    try:
        for i in range(len(participant)):
            if participant[i] == None:
                inx = i
        participant.pop(inx)
    except UnboundLocalError: ...
    
    t = pengelolaan.akses()
    riwayat = t[1]
    try:
        trans = riwayat[-1]["trans"] + 1
    except KeyError, IndexError:
        trans = 0
    deskripsi = input("Tambahkan deskripsi:\n")
    jam = Timeisit()

    if mode == 1:
        f = perhitungan.Flat(participant, payer)
        history = {"part": f[0], "deskripsi": deskripsi, "waktu": jam, "payer": payer,"produk":f[1], "harga": f[2], "tipe": "f", "trans": trans}
        riwayat.append(history)
        simpan = {"users": t[0], "riwayat": riwayat, "hutang": f[3], "rh": t[3], "trans": trans}
    else: 
        p = perhitungan.Per_Item(participant, payer)
        history = {"part": p[0], "deskripsi": deskripsi, "waktu": jam, "payer": payer, "tipe": "p"}
        riwayat.append(history)
        simpan = {"users": t[0], "riwayat": riwayat, "hutang": p[1], "rh": t[3]}
  
    print("Transaksi berhasil dicatat!")
    pengelolaan.Save(simpan)
    

def Check(pesan, eror):
    while True:    
        try:
            x = int(input(pesan))
            break
        except ValueError: print(eror)
    return x


def Validparticipant(pesan, error, re):
    valid = input(pesan)
    try:
        id_ = int(valid)
    except ValueError: id_ = valid
    p = pengelolaan.akses()
    anggota = p[0]
    for x in anggota:
        if valid.lower() == x["nama"].lower() or id_ == x["id"]:
            return x["nama"]
            break
        if valid == ".":
            return "."
    else:
        repeat = input(error)
        if repeat.lower() == "ya":
            anggota.Add_Users()
            print("Berhasil menambahkan anggota baru!")
        else:
            print(re)
            return Validparticipant(pesan, error, re)


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
            jumlah = Check("Jumlah yang dibayarkan: ", "input tidak valid!")
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