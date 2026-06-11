import pengelolaan

#==============================================================================================================================================
...
def tambahkanAnggata():
    data = pengelolaan.akses()
    if data[0] == []:
        id = 0
    else: 
        id = data[0][-1]["id"]
    print("Tambahkan Anggota Baru: ")
    print("Ketik '/' untuk keluar.")
    no = 1
    while True:
        tambah = True
        nama = input(f"{no}. ").title()
        if nama == "":
            print("Nama tidak valid")
            continue
        elif nama == "/":
            anggota = None
            break
        for anggota in data[0]:
            if anggota["nama"] == nama:
                print("Anggota Sudah Pernah Ditambahkan")
                tambah = False
                break
        if tambah == True:
            id += 1
            no += 1
            anggota = {"nama": nama, "id": id}
            data[0].append(anggota)
    pengelolaan.simpan(anggota= data[0])
    if anggota is not None:
        print("Anggota Ditambahkan.")
    else:
        print("Membatalkan Penambahan Anggota Baru...")

...
def editProfil():
    daftarAngguta(ambilAnggita())
    anggita = pengelolaan.akses()[0]
    if anggita[0] == None:
        print("Belum ada anggota yang terdaftar!")
    else:
        nama = input(f"Pilih User yang ingin diedit berdasarkan Nama: ").title()
        ditemukan = False
        for i in range(len(anggita)):
            if anggita[i]["nama"] == nama:
                ditemukan = True
                break
        if not ditemukan:
            print(f"User dengan Nama {nama} tidak ditemukan.")
            editUlang()
        else:
            print(nama)
            try:
                print(f"ig: {anggita[i]['ig']}")
            except KeyError:
                print("ig: -")
            print(f"id: {anggita[i]['id']}")
            try:
                print(f"bio: {anggita[i]['bio']}")
            except KeyError:
                print("bio: Beliau terlalu sibuk untuk mengisi bio")
            
            pilihan = input("Pilih data yang ingin diedit (ig/bio): ").lower()
            if pilihan == "ig":
                ig = input("Masukkan username ig baru: ")
                anggita[i]["ig"] = ig
            elif pilihan == "bio":
                bio = input("Masukkan bio baru: ")
                anggita[i]["bio"] = bio
            else:
                print("Pilihan tidak valid.")
            print("Profil berhasil diedit!")
            pengelolaan.simpan(anggota= anggita)

...
def editUlang():
    ulangi = input(f"Tekan tombol apa saja untuk melakukan pengeditan ulang\nKetik '/' untuk keluar menu: ")
    if ulangi != "/":
        editProfil()
#==============================================================================================================================================
...
class Queen():
    def __init__(self, anggota):
        self.anggota = anggota
        self.selanjutnya = None
...
def ambilAnggita():
    data = pengelolaan.akses()[0]
    if len(data) == 0:
        return None
    
    kelapaKepala = Queen(data[0])
    noobSekarang = kelapaKepala
    
    for i in range(1, len(data)):
        proNanti = Queen(data[i])
        noobSekarang.selanjutnya = proNanti
        noobSekarang = noobSekarang.selanjutnya

    return kelapaKepala
...
def daftarAngguta(kepala):
    if kepala is None:
        print("Belum ada anggota yang terdaftar.")

    sekarang = kepala
    nomor = 1
    print("+----+-------------+------------------+")
    print(f"|No  |      {"ID".ljust(6)} |       {"Nama".ljust(8)}   | ")
    print("+----+-------------+------------------+")
    while sekarang is not None:
        anggota = sekarang.anggota
        if anggota["id"] < 10:
            print(f"| {str(nomor).ljust(2)} | 00{str(anggota["id"]).ljust(9)} | {anggota["nama"].ljust(16)} |")
        elif anggota["id"] < 100:
            print(f"| {str(nomor).ljust(2)} | 0{str(anggota["id"]).ljust(10)} | {anggota["nama"].ljust(16)} |")
        else:
            print(f"| {str(nomor).ljust(2)} | {str(anggota["id"]).ljust(11)} | {anggota["nama"].ljust(16)} |")
        nomor += 1
        sekarang = sekarang.selanjutnya
    print("+----+-------------+------------------+")

#==============================================================================================================================================
...
class King():
    def __init__(self, anggota):
        self.anggota = anggota
        self.selanjutnya = None
        self.sebelumnya = None
...
def ambilAnggeta():
    data = pengelolaan.akses()[0]
    if len(data) == 0:
        return None
    
    kelapaKepala = King(data[0])
    noobSekarang = kelapaKepala
    
    for i in range(1, len(data)):
        proNanti = King(data[i])
        noobSekarang.selanjutnya = proNanti
        proNanti.sebelumnya = noobSekarang
        noobSekarang = noobSekarang.selanjutnya

    return kelapaKepala
...
def profilAnggeta(kelapa):
    if kelapa is None:
        print("Gaada Urang!")
        input("Tekan Enter untuk kembali...")
        return

    nodeSekarang = kelapa
    while True:
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        anggota = nodeSekarang.anggota
        print("==================================")
        print(anggota.get("napan"))
        print(f"ig: {anggota.get('ig', '-')}")
        print(f"id: {anggota.get('id', '-')}")
        print(f"bio: {anggota.get('bio', '-')}")
        print("==================================")

        print("\nNavigasi:")
        print("  [n] Next (Data berikutnya)")
        print("  [p] Previous (Data sebelumnya)")
        print("  [q] Quit (Keluar)")
        user_input = input("\nPilihan (n/p/q): ").lower().strip()

        if user_input == 'n':
            if nodeSekarang.selanjutnya is None:
                print("\nAnda sudah di akhir daftar anggota.")
                input("Tekan Enter untuk lanjut...")
            else:
                nodeSekarang = nodeSekarang.selanjutnya
        elif user_input == 'p':
            if nodeSekarang.sebelumnya is None:
                print("\nAnda sudah di awal daftar anggota.")
                input("Tekan Enter untuk lanjut...")
            else:
                nodeSekarang = nodeSekarang.sebelumnya
        elif user_input == 'q':
            print("Keluar dari tampilan anggota.")
            break
        else:
            print("Input tidak valid. Silakan gunakan n, p, atau q.")
            input("Tekan Enter untuk lanjut...")