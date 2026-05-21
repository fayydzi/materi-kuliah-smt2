# Nomor 1 (Membuat fungsi input kemudian tampilkan ke konsol)
print("Siapa nama kamu?")
nama = input()
print("Haii", nama, " Salam kenal yaa")

# Nomor 2 (Membuat fungsi input dengan argumen)
Nilai1 = float(input( " Nilai pertama  : "))
Nilai2 = float(input(" Nilai kedua  : "))
Rata_rata = (Nilai1 + Nilai2) / 2
print(" Nilai Rata rata adalah : ", Rata_rata)

# Nomor 3 (Memahami hasil dari fungsi input)
anything = input("Enter a number: ")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# Nomor 4 (Mengkonversi tipe data 1: Membuat konversi tipe data float pada fungsi input)
print("Luas Lingkaran")
jari = float(input("Jari jari lingkaran : "))
Luas = 3.14 * jari*jari
print ("Luas Lingkaran: ", Luas)

# Nomor 5 (Mengkonversi tipe data 2: Membuat program untuk menghitung sisi miring segitiga dengan variable hypo untuk menampung hasil rumus pitagoras)
a=float(input("sisi a: "))
b=float(input("sisi b: "))

hypo (a*2 + b2) * 0.5
print ("sisi miring = ", hypo)

# Nomor 6 (Mengkonversi tipe data 2: Membuat program untuk menghitung sisi miring segitiga tanpa membuat variable untuk menampung hasil operasi)
a=float(input("sisi a : "))
b=float(input("sisi b : "))
print ("sisi miring = ", (a**2 + b**2) **0.5)

# Nomor 7 (Operator Konkatenasi)
Nama_depan = input( " Nama depan : ")
Nama_belakang = input(" Nama belakang : ")
print (" Nama Lengkap : " + Nama_depan + " " + Nama_belakang)

# Nomor 8 (Operator Replikasi)
jumlah = int(input(" jumlah bintang : "))
print("*" * jumlah)

# Nomor 9 (Mengkonversi Tipe data 3: konversi ke string )
Umur = int(input(" Umur : " ))
Tahun_depan = Umur + 1
print (" Tahun depan umur saya : " + str(Tahun_depan))

# Nomor 10 (Melihat tipe data dari suatu variable)
x = 3.5
print(type(x))
x = "halo"
print(type(x))
x = 16
print(type(x))

# Kuis 7
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

print("Hasil penjumlahan:", a + b)
print("Hasil pengurangan:", a - b)
print("Hasil pembagian:", a / b)
print("Hasil perkalian:", a * b)

print("Selamat kamu sudah pintar matematika")

# Kuis 8
x = float(input(" Nilai x: "))
y = 1.0 / (x + 1.0 / (x + 1.0 / (x + 1.0 / x)))
print(" Nilai y =", round(y, 3))

# Kuis 9
jam = int(input("Waktu mulai jam: "))
menit = int(input("Waktu mulai menit: "))
durasi = int(input("Durasi Acara menit: "))

menit += durasi
jam += menit // 60 
menit = menit % 60
jam = jam % 24

print(f"Acara berakhir pukul {jam}:{menit} ")