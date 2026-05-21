#no1
list_data = [8, 10, 6, 2, 4]

for i in range(len(list_data)):
    for j in range(0, len(list_data) - i - 1):
        if list_data[j] > list_data[j + 1]:
            list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]

print(list_data)

#no2
my_list = []
swapped = True
num = int(input("Masukkan panjang elemen list yang akan diurutkan: "))

for i in range(num):
    val = float(input("Masukkan elemen list: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

#no3
data = [8, 10, 6, 2, 4]
data.sort()
print(data)

#no4
data = [1, 2, 3, 4]
data.reverse()
print(data)

#no5
list_1 = [1]
list_2 = list_1
list_1[0] = 2

print(list_2)

#no6
my_list = [10, 20, 30, 40, 50]
print(my
_list[1:4])

#no7
my_list = [10,8,4,6,2]
new_list = my_list[1:-2]
print(new_list)

#no8
my_list = [10,8,4,6,2]
new_list = my_list[-3:4]
print(new_list)

#no9
my_list = [10,8,4,6,2]
new_list = my_list[3:-4]
print(new_list)

#no10
data = [1, 2, 3, 4]
print(data[2:])

#no11
my_list = [10, 20, 30]
print(my_list[-6:])

#no12
my_list = [10, 20, 30, 40, 50]
del my_list[:2]
print(my_list)

#n013
my_list = [10, 20, 30, 40]
my_list.clear()
print(my_list)

#no14
my_list = [10, 20, 30]
del my_list

#no15
data = [1, 2, 3]
print(2 in data)

#no16
data = [1, 2, 3, 4, 5]
print(5 not in data)

#no17
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13] 
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest: 
        largest = my_list[i]

print(largest)

#no18
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]

largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)

#n019
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemen ditemukan pada index ke-", i)
else:
    print("Tidak ada di dalam list")

#no20
def cek_lotre():
    # Angka hasil undian yang sudah ditentukan
    undian = {5, 9, 11, 42, 3, 49}
    
    print("- Program Tebakan Lotre -")
    print(f"Angka undian hari ini: {undian}")
    
    try:
        # menginput 6 angka sekaligus dipisahkan spasi
        user_input = input("\nMasukkan 6 angka tebakan Anda (pisahkan dengan spasi): ")
        
        # Mengubah string input menjadi set angka integer
        tebakan = set(map(int, user_input.split()))
        
        # Validasi jumlah angka
        if len(tebakan) != 6:
            print("Peringatan: Masukkan tepat 6 angka yang berbeda.")
            return

        # Mencari kecocokan
        cocok = tebakan.intersection(undian)
        jumlah_benar = len(cocok)

        # Menampilkan hasil
        print("\n--- Hasil ---")
        print(f"Tebakan Anda : {tebakan}")
        print(f"Angka Cocok  : {list(cocok) if cocok else 'Tidak ada'}")
        print(f"Total Benar  : {jumlah_benar} kali")

    except ValueError:
        print("Kesalahan: Pastikan Anda hanya memasukkan angka.")

cek_lotre()

#no21
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