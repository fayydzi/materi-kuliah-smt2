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