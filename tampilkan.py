import pencatatan
import pengelolaan

space = ""

def History(riwayat):
    for i in range(len(riwayat)):
        if (riwayat[i]["tipe"]) == "p":
            print("==================================================================================") 
            print(f"{space.ljust(23)}Transaksi {riwayat[i]["waktu"]} {space.ljust(23)}")
            print("+---+--------------+----------------------+---------------+----------------------+")
            print(f"|No |     {"Nama".ljust(6)}   |        {"Produk".ljust(10)}    |     {"Harga".ljust(6)}    |       {"Pembayar".ljust(12)}   |")
            History_Peritem(mambo=i,riwayat=riwayat)       
        else:
            print("==================================================================================") 
            print(f"{space.ljust(23)}Transaksi {riwayat[i]["waktu"]} {space.ljust(23)}")
            print("+---+--------------+----------------------+---------------+----------------------+")
            print(f"|No |     {"Nama".ljust(6)}   |        {"Produk".ljust(10)}    |     {"Harga".ljust(6)}    |       {"Pembayar".ljust(12)}   |")
            History_Flat(mambo=i,riwayat=riwayat)       


def History_Flat(mambo,riwayat):
    desc = pencatatan.description(teks=riwayat[mambo]["deskripsi"])
    print("+---+--------------+----------------------+---------------+----------------------+")
    historyr = riwayat[mambo]
    k = 0
    harga = f"{historyr["harga"]:g}"
    try:
        for i in range(len(historyr["part"])):
            print(f"| {i+1} | {historyr["part"][i]["nama"].ljust(12)} |", end="")
            for j in range(len(historyr["part"])):
                if j == 0 and k == 0: 
                    print(f" {historyr["produk"].ljust(20)} | {str(harga).ljust(13)} | {historyr["payer"].ljust(20)} |")
                    k = 1
                elif j == 0:
                    print(f" {historyr["produk"].ljust(20)} | {str(harga).ljust(13)} | {space.ljust(20)} |")
            if i == len(historyr["part"])-1:
                print("+---+--------------+----------------------+---------------+----------------------+")
            else:
                print(f"+---+--------------+----------------------+---------------+ {space.ljust(21)}|")
    except IndexError: pass

    print("Catatan:")
    for i in range(len(desc)):
        if i == 0:
            print(f"     {desc[i]}")
        else:
            print(f"  {desc[i]}")


def History_Peritem(mambo,riwayat):
    desc = pencatatan.description(teks=riwayat[mambo]["deskripsi"])
    print("+---+--------------+----------------------+---------------+----------------------+")
    no = 1
    k = 0
    historyp = riwayat[mambo]
    try:
        for i in range(len(historyp["part"])):
            print(f"| {no} | {historyp["part"][i]["nama"].ljust(12)} |", end="")
            for j in range(len(historyp["part"][i]["produk"])):
                harga = historyp["part"][i]["produk"][j]["harga"]
                item = historyp["part"][i]["produk"][j]["item"]
                if j == 0 and k == 0: 
                    print(f" {item.ljust(20)} | {str(harga).ljust(13)} | {historyp["payer"].ljust(20)} |")
                    k = 1
                elif j == 0:
                    print(f" {item.ljust(20)} | {str(harga).ljust(13)} | {space.ljust(20)} |")
                else:
                    print(f"|   |              | {item.ljust(20)} | {str(harga).ljust(13)} | {space.ljust(20)} |")
            no += 1
            if i == len(historyp["part"])-1:
                print("+---+--------------+----------------------+---------------+----------------------+")
            else:
                print(f"+---+--------------+----------------------+---------------+ {space.ljust(21)}|")
    except IndexError: pass

    print("Catatan:")
    for i in range(len(desc)):
        if i == 0:
            print(f"     {desc[i]}")
        else:
            print(f"  {desc[i]}") 


def History_Hutang(hutang):
    print("===================================================") 
    print(f"{space.ljust(17)}Riwayat Hutang {space.ljust(17)}")
    print("+---+--------------+--------------+---------------+")
    print(f"|No |     {"Nama".ljust(6)}   |    {"Jumlah".ljust(6)}    |    {"Bayar ke".ljust(6)}   |")
    print("+---+--------------+--------------+---------------+")
    for i in range(len(hutang)):
        cetak = "%g"% hutang[i]["jumlah"]
        print( f"|{i+1}. | {hutang[i]["nama"].ljust(12)} | {str(cetak).ljust(12)} | {hutang[i]["ke"].ljust(13)} |")
        print("+---+--------------+--------------+---------------+")
        i += 1

def History_Perhitungan():
    p = pengelolaan.akses()
    pembayaran = p[3]
    if pembayaran == []:
        print("Riwayat perhitungan kosong!!")
    else:    
        print("===================================================") 
        print(f"{space.ljust(16)}Riwayat Pembayaran {space.ljust(16)}")
        print("===================================================")
        for i in range(len(pembayaran)):
            if pembayaran[i]["net"] == "swap":
                print(f"[Ditukar otomatis] {pembayaran[i]["nama"]} sekarang berhutang {pembayaran[i]["hutang"]} ke {pembayaran[i]["ke"]}")
            elif pembayaran[i]["net"] == "tambah":
                print(f"[Ditambahkan otomatis] {pembayaran[i]["nama"]} berhutang sebanyak {pembayaran[i]["jumlah"]} ke {pembayaran[i]["ke"]}")
            elif pembayaran[i]["net"] == "gabung":
                try:    
                    if pembayaran[i]["status"]:
                        print(f"[Digabungkan otomatis] {pembayaran[i]["nama"]} berhutang sebanyak {pembayaran[i]["jumlah"]} ke {pembayaran[i]["ke"]} [Status Lunas!]")
                    else:          
                        print(f"[Digabungkan otomatis] {pembayaran[i]["nama"]} berhutang sebanyak {pembayaran[i]["jumlah"]} ke {pembayaran[i]["ke"]} [Status belum Lunas!]")
                except KeyError: continue
            elif pembayaran[i]["net"] == "bayar":
                print(f"[Pembayaran] {pembayaran[i]["nama"]} membayar sebanyak {pembayaran[i]["bayar"]} ke {pembayaran[i]["ke"]}, sisa hutang = {pembayaran[i]["sisa"]} {"Status lunas" if pembayaran[i]["sisa"] <= 0.0 else "Belum lunas"}")
            elif pembayaran[i]["net"] == "simpel":
                print(f"[Simplikasi] Hutang {pembayaran[i]["nama2"]} ke {pembayaran[i]["nama3"]} jadi {pembayaran[i]["nama1"]} ke {pembayaran[i]["nama3"]}, sisa {pembayaran[i]["nama1"]} ke {pembayaran[i]["nama2"]} = {pembayaran[i]["jumlah"]}")
            elif pembayaran[i]["net"] == "waktu":
                print(pembayaran[i]["waktu"])       
            else:
                print(f"[{i}] [Error]")
            
 
 
