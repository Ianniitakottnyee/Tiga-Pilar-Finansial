import pencatatan
import json


def unggah(simpan):
    with open("data.json", "w") as f:
        json.dump(simpan, f, indent= 4)


def buka():
    with open("data.json", "r") as f:
        loaded = json.load(f)
    return loaded


def akses():
    data = buka()
    try:
        anggota = data["anggota"]
    except KeyError: anggota = []
    try:
        transaksi = data["transaksi"]
    except KeyError: transaksi = []
    try:
        pembayaran = data["pembayaran"]
    except KeyError: pembayaran = []
    try:
        perhitungan = data["perhitungan"]
    except KeyError:
        perhitungan = []
    return [anggota, transaksi, pembayaran, perhitungan]

def simpan(anggota= None, transaksi= None, pembayaran= None, perhitungan= None):
    data = akses()
    if anggota is None:
        anggota = data[0]
    if transaksi is None:
        transaksi = data[1]
    if pembayaran is None:
        pembayaran = data[2]
    if perhitungan is None:
        # data[3] may not exist in older files
        try:
            perhitungan = data[3]
        except Exception:
            perhitungan = []
    simpan = {"anggota": anggota, "transaksi": transaksi, "pembayaran": pembayaran, "perhitungan": perhitungan}
    unggah(simpan)


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