# nomor 1
i = 1
while i <= 5:
    print(i)
    i += 1

#nomor2
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#nomor3
i = 1

while i <= 10:
    if i % 2 == 0:
        print(i, "adalah bilangan genap")
    else:
        print(i, "adalah bilangan ganjil")
    i += 1

#Kuis 15
secret_number = 777

print("""
+================================+
| Selamat datang di game saya, muggle! |
| masukkan suatu angka dan tebak |
| angka berapa yang saya pilih   |
| untuk kamu.                    |
| Jadi, berapa angka rahasianya? |
+================================+
""")

while True:
    angka = int(input("Masukkan angka: "))

    if angka == secret_number:
        print("Selamat, Muggle! kamu bebas sekarang")
        break
    else:
        print("hahaha! kamu nyangkut deh di Loop saya")
#nomor4
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
c = int(input("Masukkan nilai c: "))
d = int(input("Masukkan nilai d: "))
e = int(input("Masukkan nilai e: "))

nilai = [a, b, c, d, e]
terbesar = nilai[0]

for i in nilai:
    if i > terbesar:
        terbesar = i

print("Nilai terbesar adalah:", terbesar)

#Nommor5
n = int(input("Masukkan nilai pangkat: "))
hasil = 1

for i in range(n):
    hasil = hasil * 2

print("Hasil eksponensial 2^", n, "=", hasil)

#nomor6
for i in range(1, 11):
    if i == 5:
        continue
    if i == 9:
        break
    print(i)


#kuis16
secret_number = 777

while True:
    angka = int(input("Masukkan angka tebakan: "))

    if angka == secret_number:
        print("Selamat! Tebakan kamu benar.")
        break
    else:
        print("Tebakan salah, coba lagi!")

#kuis17
# meminta user memasukkan kata
user_word = input("Masukkan sebuah kata: ")

# mengubah kata menjadi huruf kapital
user_word = user_word.upper()

# perulangan untuk membaca setiap huruf
for huruf in user_word:
    if huruf == "A":
        continue
    elif huruf == "I":
        continue
    elif huruf == "U":
        continue
    elif huruf == "E":
        continue
    elif huruf == "O":
        continue
    else:
        print(huruf)


#Nomor7
i = 1

while i <= 5:
    print("Angka:", i)
    i += 1
else:
    print("Perulangan selesai")

#nomor8
for i in range(1, 6):
    print("Angka:", i)
else:
    print("Perulangan for selesai")

#nomor9
a = 10
b = 5

print("a > b :", a > b)
print("a < b :", a < b)
print("a == b :", a == b)
print("a != b :", a != b)

#nomor 10
a = True
b = False

print("Logical AND:", a and b)
print("Logical OR:", a or b)
print("Logical NOT:", not a)

x = 5
y = 3

print("Bitwise AND:", x & y)
print("Bitwise OR:", x | y)
print("Bitwise XOR:", x ^ y)

#nomor11
a = 5

print("Nilai a:", a)
print("Shift kiri (a << 1):", a << 1)
print("Shift kanan (a >> 1):", a >> 1)

#kuis18
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)