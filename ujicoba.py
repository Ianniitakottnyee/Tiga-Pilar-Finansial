import perhitungan
import pengelolaan
import pencatatan



kumpulanTransaksi = pengelolaan.akses()[1]

graph = perhitungan.graph()
graph.transaksiKeHutang(kumpulanTransaksi)

print("Hutang setelah transaksi ke hutang:")
graph.tampilkanHutang()