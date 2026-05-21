# nomor 1 (Comparison Operator)
a = 10
b = 5
print(a > b)
print(a < b)
print(a == b)
print(a != b)

# Kuis 11 
n = int(input("Masukkan nilai n: "))

if n > 100:
    print(True)
else:
    print(False)

# Nomor 3 (Conditional statement: Rangkaian if)
nilai = int(input("Masukkan nilai : "))

if nilai >= 90:
    print("Nilai A")

if nilai >= 75:
    print("Nilai B")

if nilai >= 70:
    print("Nilai C")

# Nomor 4 (Conditional statement: if-else)
nilai = int(input(" Masukkan Nilai : "))

if nilai >= 90:
    print("Nilai A")
elif nilai >= 75:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai C")
else:
    print("Nilai D")

# Nomor 5  (Conditional statement: if-elif-else)
nilai = int(input( "Masukkan Nilai : "))

if nilai >= 80:
    print("Lulus")
else:
    print("Tidak Lulus")

# Nomor 6 (Membandingkan 2 angka input)
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

if a > b:
    print("angka pertama lebih besar")
elif a < b:
    print("angka kedua lebih besar")
else:
    print("kedua angka sama")

# Kuis 12
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

if a > b and a > c:
    print("Angka terbesar adalah:", a)
elif b > a and b > c:
    print("Angka terbesar adalah:", b)
else:
    print("Angka terbesar adalah:", c)

# Kuis 13
pendapatan = float(input("Masukkan pendapatan bulanan Anda: "))
pajak = 0

if pendapatan <= 60000000:
    pajak = pendapatan * 0.05
elif pendapatan <= 250000000:
    pajak = pendapatan * 0.15
elif pendapatan <= 500000000:
    pajak = pendapatan * 0.25
else:
    pajak = pendapatan * 0.30

print("Pajak penghasilan yang harus anda bayar adalah", pajak, "rupiah")
