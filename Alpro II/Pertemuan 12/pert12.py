# no 1
def contoh():
    x = 10
    print(x)

contoh()

# no 2
x = 5

def contoh():
    print("Nilai x:", x)

contoh()
#no 3
x = 5

def contoh():
    x = 10
    print(x)

contoh()
print(x)

#no 4
x = 5

def ubah():
    global x
    x = 10

ubah()
print(x)

#NO 5
#kuis IMT
def hitung_imt(berat, tinggi):
    # menghitung nilai imt
    imt = berat / (tinggi ** 2)
    return imt

# user memasukkan berat (kg) dan tinggi (m)
# menggunakan float agar bisa menerima angka desimal (contoh: 1.7)
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

index_massa_tubuh = hitung_imt(berat, tinggi)
kategori = ["Normal", "Gemuk", "Obesitas"]

# kategorikan nilai imt yang sudah di dapat
if index_massa_tubuh <= 25.0:
    print("Index massa tubuh anda adalah ", index_massa_tubuh, ", termasuk kategori ", kategori[0])
elif 25.0 < index_massa_tubuh <= 27.0:
    print("Index massa tubuh anda adalah ", index_massa_tubuh, ", termasuk kategori ", kategori[1])
else:
    print("Index massa tubuh anda adalah ", index_massa_tubuh, ", termasuk kategori ", kategori[2], ", Anda harus diet!")

#NO 6
def segitiga(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

print(segitiga(3, 4, 5))

#NO 7
def segitiga(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(segitiga(3, 4, 5))

#No 8
print((3+4>5) and (3+5>4) and (4+5>3))

#NO 9
#kuis faktorial
def faktorial(n):
    # bilangan yang akan difaktorial harus lebih besar dari 0
    if n < 0:
        return None
    
    # 0! dan 1! nilainya sama (1)
    if n < 2:
        return 1
    
    hasil = 1
    # kita mulai perkalian dari 2 sampai n
    for i in range(2, n + 1):
        hasil = hasil * i
    
    return hasil

n = int(input("Masukkan nilai yang ingin di faktorial: "))
print(n, "! = ", faktorial(n))

#No 10
#kuis fibonacci
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    
    elem_1 = elem_2 = 1
    hasil_jumlah = 0 # untuk menampung hasil dari penjumlahan 2 elemen
    
    # Kita mulai perulangan dari indeks ke-3 sampai n
    for i in range(3, n + 1):
        # Proses jumlah
        hasil_jumlah = elem_1 + elem_2
        
        # Tukar elemen (geser nilai untuk iterasi berikutnya)
        elem_1 = elem_2
        elem_2 = hasil_jumlah
        
    return hasil_jumlah

# Test
for i in range(1, 10):
    print(i, "->", fibonacci(i))

#No 11
def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n-1)

print(faktorial(5))

#No 12
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))