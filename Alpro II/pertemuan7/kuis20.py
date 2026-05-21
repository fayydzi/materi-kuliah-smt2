# Langkah 1: buatlah sebuat list kosong dengan nama exo
exo = []

# Langkah 2: gunakan method append( ) untuk menambahkan anggota: Suho, Kai, Chanyeol dan Sehun
exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")
print("Langkah 2: ", exo)

# Langkah 3: gunakan for untuk menambahkan anggota: DO, Baekhyun, Kris, Lay, Luhan, Tao, dan Chen
anggota_baru = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for anggota in anggota_baru:
    exo.append(anggota)
print("Langkah 3: ", exo)

# Langkah 4: Hapuslah anggota: Kris, Luhan dan Tao
# Menggunakan remove() karena kita tahu nama spesifik yang ingin dihapus
exo.remove("Kris")
exo.remove("Luhan")
exo.remove("Tao")
print("Langkah 4: ", exo)

# Langkah 5: gunakan method insert() untuk menambahkan anggota Xiumin pada elemen ke tiga dari terakhir
# Indeks -3 berarti urutan ketiga jika dihitung dari belakang
exo.insert(-3, "Xiumin")
print("Langkah 5: ", exo)

# Menampilkan jumlah akhir anggota
print("Jumlah anggota exo: ", len(exo))