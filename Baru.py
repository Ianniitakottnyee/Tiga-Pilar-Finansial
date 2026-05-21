Anggota = []
id = 0

class Anggata:
    def __init__(self, nama, id):
        self.nama = nama
        self.id = id

    def dict(self):
        anggotaBaru = {
            "nama": self.nama,
            "id": self.id
        }
        return anggotaBaru

def inpuy():
    global id
    global Anggota
    nama = input("Masukkan Nama: ")
    id += 1
    x = Anggata(nama, id)
    y = x.dict()
    Anggota.append(y)

while True:
    inpuy()
    fal = input("Enter untuk berhenti...")
    if fal == "":
        break

for x in Anggota:
    print(x)
