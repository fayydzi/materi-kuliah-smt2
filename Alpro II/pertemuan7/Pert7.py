#nomor 1 
my_list = [10, 20, 30, 40, 50]
print(my_list[0])
print(my_list[2])
print(my_list[4])

#nomor2
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i)

#nomor3
my_list = [10, 20, 30, 40]
print(len(my_list))

#nomor4
my_list = [10, 20, 30, 40]
print(len(my_list))

#nomor5
my_list = [10, 20, 30, 40]
print(my_list[-1])
print(my_list[-2])

#kuis19
topi_list = [1, 2, 3, 4, 5] # Angka yang tersembunyi di dalam topi pesulap

# Langkah 1: Tulis satu baris kode yang meminta user memasukkan angka integer
# untuk di-replace ke nilai tengah dari list (indeks 2)
topi_list[2] = int(input("Masukkan angka pengganti untuk nilai tengah: "))

# Langkah 2: Tulis satu baris kode untuk menghapus elemen terakhir pada list
topi_list.pop()

# Langkah 3: Tulis satu baris kode untuk menampilkan panjang dari list
print("Panjang list saat ini adalah:", len(topi_list))

print(topi_list)

#nomor6
my_list = [1, 2, 3]
my_list.append(4)
my_list.insert(1, 10)
print(my_list)

#nomor7
angka = [111, 7, 2, 1]
print(len(angka))
print(angka)

###

angka.append(4)
print(len(angka))
print(angka)

###

angka. insert(0, 222) 
print(len(angka)) 
print(angka)

angka.insert(1, 333)
print(len(angka))
print(angka)

#nomor8

#kode2
my_list = []  # membuat list kosong

for i in range(5):
    my_list.insert(0, i + 1)

print("Hasil insert:", my_list)

#nomor9
#kode1
my_list = []  # membuat list kosong

for i in range(5):
    my_list.append(i + 1)

print("Hasil append:", my_list)


#nomor10
#kode2
my_list = [10, 1, 8, 3, 5] 
total=0

for i in my_list: 
    total += i

print(total)

#nomor11
my_list = [10, 1, 8, 3, 5]

length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

#kuis20
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
