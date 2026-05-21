# List awal yang berisi angka berulang
list_awal = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# List baru sebagai temporary work area
list_unik = []

# Proses penyaringan
for angka in list_awal:
    # Cek apakah angka sudah ada di list_unik atau belum
    if angka not in list_unik:
        # Jika belum ada, masukkan ke dalam list_unik
        list_unik.append(angka)

# Menampilkan hasil
print(f"List awal : {list_awal}")
print(f"List unik : {list_unik}")