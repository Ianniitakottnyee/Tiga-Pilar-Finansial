import pengelolaan

users = []

class anggata:
    def __init__(self, nama, id):
        self.nama = nama
        self.id = id

    def tambahAnggota(self, nama, id):
        return {
            "nama": self.nama,
            "id": self.id
        }
    
    def inputAnggata(self):
        angka = 0
        angka += 1
        anggota = "nama" + str(angka)

        [{"nama": "A", "id": 1}, {"nama": "b", "id": 2}]

a = anggata.tambahAnggota("angga", 2)


def Add_Users():
    user = {}
    Show_Users()

    p = pengelolaan.akses()
    users = p[0]
    if users == []:
        id = 0
    else: id = users[-1]["id"]
    print("Tambahkan Anggota Baru:")
    print("Tekan (.) jika selesai menambahkan.")
    i = 1
    while True:
        new = input(f"{i}. ")
        tambah = True
        if new == ".":
            break
        for x in users:
            if x["nama"] == new.title():
                print("Anggota sudah ditambahkan")
                tambah = False
                break
        if new == "":
            print("input tidak valid.")
        else:
            if tambah == True:
                id += 1
                user = {"nama" : new.title(), "id" : id}
                users.append(user)
                i+=1

    simpan = {"users": users, "riwayat": p[1], "hutang": p[2], "rh": p[3]}
    pengelolaan.Save(simpan)


def Show_Users():
    p = pengelolaan.akses()
    users = p[0]
    print("+----+--------------+------------------+")
    print(f"|No  |      {"ID".ljust(7)} |       {"Nama".ljust(8)}   | ")
    print("+----+--------------+------------------+")
    for i in range(len(users)):
        if users[i]["id"] < 10:
            print(f"| {str(i+1).ljust(2)} |  00{str(users[i]["id"]).ljust(9)} | {users[i]["nama"].ljust(16)} | ")
        elif users[i]["id"] < 100:
            print(f"| {str(i+1).ljust(2)} |  0{str(users[i]["id"]).ljust(10)} | {users[i]["nama"].ljust(16)} | ")
        else:
            print(f"| {str(i+1).ljust(2)} |  {str(users[i]["id"]).ljust(11)} | {users[i]["nama"].ljust(16)} | ")
    print("+----+--------------+------------------+")


def Delete_User():
    Show_Users()
    p = pengelolaan.akses()
    users = p[0]
    if users[0] == None:
        print("Belum ada anggota yang terdaftar!")
    else:
        try:
            x = int(input(f"Pilih User yang ingin dihapus berdasarkan IDnya: "))
            ditemukan = False
            for i in range(len(users)):
                if users[i]["id"] == x:
                    users.pop(i)
                    print("Users berhasil dihapus!")
                    simpan = {"users": users, "riwayat": p[1], "hutang": p[2], "rh": p[3]}
                    pengelolaan.Save(simpan)
                    Show_Users()
                    ditemukan = True
                    break
            if not ditemukan:
                print(f"User dengan ID {x} tidak ditemukan.")
        except ValueError: print("ID tidak valid"), Repeat_Delete()


def Repeat_Delete():
    ulangi = input(f"Tekan tombol apasaja untuk melakukan penghapusan ulang\nKetik (.) untuk keluar menu")
    if ulangi != ".":
        Delete_User()

