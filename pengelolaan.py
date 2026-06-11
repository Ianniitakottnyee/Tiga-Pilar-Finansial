import pencatatan
import json

#==============================================================================================================================================
def unggah(simpan):                                                                 #File Handler [2]
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
    except KeyError: pembayaran = ()
    return [anggota, transaksi, pembayaran]

def simpan(anggota= None, transaksi= None, pembayaran= None):
    data = akses()
    if anggota is None:
        anggota = data[0]
    if transaksi is None:
        transaksi = data[1]
    if pembayaran is None:
        pembayaran = data[2]
    simpan = {"anggota": anggota, "transaksi": transaksi, "pembayaran": pembayaran}
    unggah(simpan)

#==============================================================================================================================================
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