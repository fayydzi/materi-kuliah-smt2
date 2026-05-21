topi_list = [1, 2, 3, 4, 5] # Angka yang tersembunyi di dalam topi pesulap

# Langkah 1: Tulis satu baris kode yang meminta user memasukkan angka integer
# untuk di-replace ke nilai tengah dari list (indeks 2)
topi_list[2] = int(input("Masukkan angka pengganti untuk nilai tengah: "))

# Langkah 2: Tulis satu baris kode untuk menghapus elemen terakhir pada list
topi_list.pop()

# Langkah 3: Tulis satu baris kode untuk menampilkan panjang dari list
print("Panjang list saat ini adalah:", len(topi_list))

print(topi_list)