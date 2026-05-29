import pencatatan
import pengelolaan
import tampilkan

def pembagianRata(peserta, pembayar):
    item = input("Nama Produk: ")
    while True:
        harga = input("Harga Satuan/Harga Total(s/t): ").lower()
        if harga == "s":
            harga = pencatatan.cek("Harga: ", f"\033[91mHarga Harus Berupa Angka! \033[0m")
            break
        elif harga == "t":
            total = pencatatan.cek("Harga: ", f"\033[91mHarga Harus Berupa Angka! \033[0m")
            harga = total/len(peserta)
            if harga % 10 != 0:
                if harga % 1000 < 500:
                    harga = harga - (harga % 1000)
                else:
                    harga = harga - (harga % 1000) + 1000
            break
        else:
            print(f"\033[91mPembagian Harus Berupa Satuan/Total \033[0m")
            continue
    print(harga)
 
    
def Flat(participant, payer):
    historyr = []
    item = input("nama produk: ")
    ptan = input("Harga satuan/Harga total?(s/t): ")
    if ptan.title() == "Harga satuan" or ptan.lower() == "s":
        harga = pencatatan.Check(pesan="Harga satuan: ", eror="input yang bener la")
    else:
        harga = pencatatan.Check(pesan="Harga total: ", eror="input yang bener la")
        harga = harga/len(participant)
        if harga % 10 != 0:
            if harga % 1000 < 500:
                harga = harga - (harga % 1000)
            else:
                harga = harga - (harga % 1000) + 1000

    p = pengelolaan.akses()
    debt = p[2]
    for i in range(len(participant)):
        riwayatr = {"nama" : participant[i]}
        historyr.append(riwayatr)
        if participant[i] == payer:
            continue
        else:
            hutang = {}
            hutang = {"nama" : participant[i], "jumlah" : harga, "ke" : payer}
            debt.append(hutang)

    return [historyr, item, harga, debt]


def Per_Item(participant, payer):
    historyp = []
    list_peritem = []
    print("catat masing-masing membeli apa:")
    for i in range(len(participant)):
        pemilik = {}
        produk = []
        print(f"{i+1}. {participant[i]}: ")
        while True:
            item = {}
            x = input(f"item: ")
            if x == ".": break
            y = pencatatan.Check(pesan="harga: ", eror="harga tidak valid!")
            item = {"item": x, "harga": y }
            produk.append(item)
        jum = 0
        for j in range(len(produk)):
            jum += produk[j]["harga"]
    
        pemilik = {"punya": participant[i], "produk": produk, "total": jum}
        list_peritem.append(pemilik)
        
        p = pengelolaan.akses()
        debt = p[2]    
    for i in range(len(list_peritem)):
        hutang = {}
        riwayat = {"nama" : list_peritem[i]["punya"], "produk": list_peritem[i]["produk"]}
        historyp.append(riwayat)
        if list_peritem[i]["punya"] == payer:
            continue
        else:
            hutang = {"nama" : list_peritem[i]["punya"], "jumlah" : list_peritem[i]["total"], "ke" : payer}
            debt.append(hutang)
    return [historyp, debt]
    

def Net_Debt():
    p = pengelolaan.akses()
    debt = p[2]
    rihu = p[3]
    panjang = len(debt)
    waktu = pencatatan.Timeisit()
    srh = {"net": "waktu", "waktu": waktu}
    rihu.append(srh)
    try:    
        for i in range(panjang):
            for j in range(panjang):
                srh = {}
                jmlh = 0
                if i == j:
                    continue
                if debt[i]["jumlah"] < 0:
                    nama = debt[i]["nama"]
                    debt[i]["nama"] = debt[i]["ke"]
                    debt[i]["ke"] = nama
                    debt[i]["jumlah"] = debt[i]["jumlah"] / -1
                    srh = {"nama": debt[i]["ke"], "hutang": debt[i]["jumlah"], "ke": debt[i]["nama"], "net": "swap"}
                    rihu.append(srh)                 
                if debt[i]["nama"] == debt[j]["nama"] and debt[i]["ke"] == debt[j]["ke"]:
                    jmlh = debt[i]["jumlah"] + debt[j]["jumlah"]
                    srh = {"nama": debt[i]["nama"], "jumlah": f"{debt[i]["jumlah"]} + {debt[j]["jumlah"]} = {jmlh}", "ke": debt[j]["ke"], "net": "tambah"}
                    debt[i]["jumlah"] = jmlh
                    rihu.append(srh)
                    debt[j]["ke"] = ""
                elif debt[i]["nama"] == debt[j]["ke"] and debt[i]["ke"] == debt[j]["nama"]:
                    if debt[i]["jumlah"] > debt[j]["jumlah"]:
                        jmlh = debt[i]["jumlah"] - debt[j]["jumlah"]
                        srh = {"nama": debt[i]["nama"], "jumlah": f"{debt[i]["jumlah"]} - {debt[j]["jumlah"]} = {jmlh}", "ke": debt[i]["ke"], "net": "gabung"}
                        debt[i]["jumlah"] = jmlh
                        rihu.append(srh)
                        debt[j]["ke"] = ""
                    elif debt[i]["jumlah"] < debt[j]["jumlah"]:
                        jmlh = debt[j]["jumlah"] - debt[i]["jumlah"]
                        srh = {"nama": debt[j]["nama"], "jumlah": f"{debt[j]["jumlah"]} - {debt[i]["jumlah"]} = {jmlh}", "ke": debt[j]["ke"], "net": "gabung"}
                        debt[j]["jumlah"] = jmlh
                        rihu.append(srh)                        
                        debt[i]["ke"] = ""
                    else:
                        srh = {"nama": debt[i]["nama"], "jumlah": f"{debt[i]["jumlah"]} - {debt[j]["jumlah"]} = 0", "ke": debt[i]["ke"], "status": "Lunas", "net": "gabung"}
                        rihu.append(srh)                        
                        debt[i]["ke"] = ""
                        debt[j]["ke"] = ""
    except IndexError: pass

    for i in range(panjang, -1, -1):
        try:
            if debt[i]["ke"] == "" or debt[i]["jumlah"] == 0.0:
                debt.pop(i)
        except IndexError: pass
    simpan = {"users": p[0], "riwayat": p[1], "hutang": debt, "rh": rihu}
    pengelolaan.Save(simpan)

    p = pengelolaan.akses()
    tampilkan.History_Hutang(p[2])
    return [debt, rihu]

def elimination():
    p = pengelolaan.akses()
    hutang = p[2]
    rihu = p[3]
    waktu = pencatatan.Timeisit()
    srh = {"net": "waktu", "waktu": waktu}
    rihu.append(srh)
    print("===================  Simplikasi  ==================")
    for x in hutang:
        for y in hutang:
            if x["ke"] == y["nama"]:
                if x["jumlah"] == y["jumlah"]:
                    x["ke"] = y["ke"]
                    srh = {"nama1": x["nama"], "nama2": y["ke"], "nama3": x["ke"], "jumlah": x["jumlah"], "net": "simpel"}
                    rihu.append(srh)
                    y["ke"] = ""
                elif x["jumlah"] > y["jumlah"]:
                    y["nama"] = x["nama"]
                    x["jumlah"] = x["jumlah"] - y["jumlah"]
                    srh = {"nama1": x["nama"], "nama2": x["ke"], "nama3": y["ke"], "jumlah": x["jumlah"], "net": "simpel"}
                    rihu.append(srh)
                elif x["jumlah"] < y["jumlah"]:
                    x["ke"] = y["ke"]
                    y["jumlah"] = y["jumlah"] - x["jumlah"]
                    srh = {"nama1": x["nama"], "nama2": y["nama"], "nama3": x["ke"], "jumlah": y["jumlah"], "net": "simpel"}
                    rihu.append(srh)
                else:
                    print("error")
    for i in range(len(hutang), -1, -1):
        try:
            if hutang[i]["ke"] == "":
                hutang.pop(i)
        except IndexError: pass
    simpan = {"users": p[0], "riwayat": p[1], "hutang": hutang, "rh": rihu}
    pengelolaan.Save(simpan)

    p = pengelolaan.akses()
    tampilkan.History_Hutang(p[2])