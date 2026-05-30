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
        hutang = data["hutang"]
    except KeyError: hutang = []
    try:
        perhitungan = data["perhitungan"]
    except KeyError: perhitungan = []
    return [anggota, transaksi, hutang, perhitungan]

def simpan(anggota= None, transaksi= None, hutang= None, perhitungan= None):
    data = akses()
    if anggota is None:
        anggota = data[0]
    if transaksi is None:
        transaksi = data[1]
    if hutang is None:
        hutang = data[2]
    if perhitungan is None:
        perhitungan = data[3]
    simpan = {"anggota": anggota, "transaksi": transaksi, "hutang": hutang, "perhitungan": perhitungan}
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