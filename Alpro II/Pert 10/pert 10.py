#Nomor 1
nilai = [60, 70, 80, 90]
lulus = [n for n in nilai if n >= 75]
print(lulus)

#Nomor2
data = [
    [10, 20, 30],
    [40, 50, 60]
]

print(data[0][2])

#nomor3
barang = [
    [["Pulpen", "Pensil"], ["Penghapus", "Penggaris"]],
    [["Buku", "Map"], ["Spidol", "Tipe-X"]]
]

print(barang[1][0][1])

#nomor4
def hitung_total(harga, jumlah):
    return harga * jumlah

print(hitung_total(5000, 3))

# Kuis1
hasil = [x * 3 for x in range(1, 11) if x % 2 == 0]
print(hasil)

# kuis 2
array = [[j + i*3 for j in range(1, 4)] for i in range(3)]

for baris in array:
    print(baris)

# kuis 3
data = [[2, 4], [6, 8], [10, 12]]

hasil = [angka for sublist in data for angka in sublist]

print(hasil)

#nomor8
def hitung_luas(p, l):
    return p * l

print(hitung_luas(8, 5))

