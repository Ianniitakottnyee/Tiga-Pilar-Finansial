import perhitungan
import pengelolaan
import pencatatan
import anggota

x = perhitungan.graph()
x.transaksiKeHutang(pengelolaan.akses()[1])

print("Hutang Awal:")
x.tampilkanHutang()
input("Tekan Enter untuk Melanjutkan...")
print("Hutang Awal:")
x.tampilkanHutang()

input("Tekan Enter untuk Melanjutkan...")
print("Riwayat Perhitungan:")
x.tampilkanRiwayatPerhitungan()

input("Tekan Enter untuk Melanjutkan...")
print("Riwayat Pembayaran:")
x.tampilkanRiwayatPembayaran()

input("Tekan Enter untuk Melanjutkan...")
print("Pembayaran:")
x.pembayaran()

input("Tekan Enter untuk Melanjutkan...")
print("Riwayat Pembayaran kedua:")
x.tampilkanRiwayatPembayaran()

input("Tekan Enter untuk Melanjutkan...")
print("Hutang Final:")
x.tampilkanHutang()