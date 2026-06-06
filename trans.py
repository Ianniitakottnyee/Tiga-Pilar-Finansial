import pengelolaan


class Node():
    def __init__(self, transaksi):
        self.transaksi = transaksi
        self.selanjutnya = None
        self.sebelumnya = None


def ambilAngga():
    data = pengelolaan.akses()[1]
    if len(data) == 0:
        return None
    
    kelapaKepala = Node(data[0])
    noobSekarang = kelapaKepala
    
    for i in range(1, len(data)):
        proNanti = Node(data[i])
        noobSekarang.selanjutnya = proNanti
        proNanti.sebelumnya = noobSekarang
        noobSekarang = noobSekarang.selanjutnya
    
    noobSekarang.selanjutnya = kelapaKepala
    kelapaKepala.sebelumnya = noobSekarang
    
    return kelapaKepala


def tampilkanTransaksi(kelapa):
    current_node = kelapa
    nomor = 1
    
    while True:
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        
        transaksi = current_node.transaksi
        
        if transaksi["kode"] == "r":
            print(f"======================================================================================")
            print(f"                                 transaksi ke-{nomor} dari {len(pengelolaan.akses()[1])}")
            print(f"======================================================================================")
            print(f"+----+--------------------+---------------------+-----------------+-----------------+")
            print(f"| No |       Peserta      |        Produk       |      Harga      |     Pembayar    |")
            print(f"+----+--------------------+---------------------+-----------------+-----------------+")
            no = 0
            kosong = ""
            for peserta in transaksi["peserta"]:
                if no == 0:
                    print(f"| {no+1}. | {peserta.ljust(18)} | {transaksi["item"].ljust(19)} | Rp {str(transaksi["harga"]).ljust(12)} | {transaksi["pembayar"].ljust(15)} |")
                    no += 1
                else:
                    print(f"| {no+1}. | {peserta.ljust(18)} | {kosong.ljust(19)} | {kosong.ljust(15)} | {kosong.ljust(15)} |")
                    no += 1
            print(f"+----+--------------------+---------------------+-----------------+-----------------+")

        else:
            print(f"======================================================================================")
            print(f"                                 transaksi ke-{nomor} dari {len(pengelolaan.akses()[1])}")
            print(f"======================================================================================")
            print(f"+----+--------------------+---------------------+-----------------+-----------------+")
            print(f"| No |       Peserta      |        Produk       |      Harga      |     Pembayar    |")
            print(f"+----+--------------------+---------------------+-----------------+-----------------+")
            no = 0
            kosong = ""
            for peserta in transaksi["peserta"]:
                awal = True
                nama = list(peserta.keys())[0]
                listItem = peserta[nama]
        
                for item in listItem:
                    for produk, harga in item.items():
                        if awal is True:
                            print(f"| {no+1}. | {nama.ljust(18)} | {produk.ljust(19)} | Rp {str(harga).ljust(12)} | {transaksi["pembayar"].ljust(15)} |")
                            awal = False
                        else:
                            print(f"| {kosong.ljust(2)} | {kosong.ljust(18)} | {produk.ljust(19)} | Rp {str(harga).ljust(12)} | {kosong.ljust(15)} |")
                no += 1
                print(f"+----+--------------------+---------------------+-----------------+-----------------+")



        print("\nNavigasi:")
        print("  [n] Next (Data berikutnya)")
        print("  [p] Previous (Data sebelumnya)")
        print("  [q] Quit (Keluar)")
        
        user_input = input("\nPilihan (n/p/q): ").lower().strip()
        
        if user_input == 'n':
            current_node = current_node.selanjutnya
            if nomor < len(pengelolaan.akses()[1]):
                nomor += 1
            else:
                nomor = 1
        elif user_input == 'p':
            current_node = current_node.sebelumnya
            if nomor > 1:   
                nomor -= 1
            else:
                nomor = len(pengelolaan.akses()[1])
        elif user_input == 'q':
            print("Keluar dari tampilan transaksi.")
            break
        else:
            print("Input tidak valid. Silakan gunakan n, p, atau q.")
            input("Tekan Enter untuk lanjut...")


if __name__ == "__main__":
    tampilkanTransaksi(ambilAngga())