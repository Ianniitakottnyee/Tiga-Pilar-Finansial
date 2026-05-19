import Pencatatan
import json


def Save(simpan):
    with open("data.json", "w") as f:
        json.dump(simpan, f)


def buka():
    with open("data.json", "r") as f:
        loaded = json.load(f)
    return loaded


def akses():
    data = buka()
    try:
        users = data["users"]
    except KeyError: users = []
    try:
        riwayat = data["riwayat"]
    except KeyError: riwayat = []
    try:
        hutang = data["hutang"]
    except KeyError: hutang = []
    try:
        riwhutang = data["rh"]
    except KeyError: riwhutang = []
    return [users, riwayat, hutang, riwhutang]

def clearrh():
    p = akses()
    if p[3] == []:
        print("Riwayat kosong!")
    else:
        simpan = {"users": p[0], "riwayat": p[1], "hutang": p[2], "rh": []}
        Save(simpan)
        print("Riwayat perhitungan berhasil dihapus!")

def openbackup():
    with open("backup.json", "r") as f:
        loaded = json.load(f)

    with open("data.json", "w") as f:
        json.dump(loaded, f)

def upbackup():
    with open("data.json", "r") as f:
        loaded = json.load(f)

    with open("backup.json", "w") as f:
        json.dump(loaded, f)

    with open("data.json", "w") as f:
        json.dump({}, f)