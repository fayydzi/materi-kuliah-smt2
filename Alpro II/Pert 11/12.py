#kuis 26
def cek_prima(bilangan):
    # Bilangan prima harus lebih besar dari 1
    if bilangan <= 1:
        return False
    
    # Cek pembagi dari 2 hingga akar dari bilangan (atau bilangan - 1)
    # Jika ada yang bisa membagi habis, maka bukan prima
    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False
            
    # Jika tidak ada pembagi yang ditemukan, maka prima
    return True

# Bagian kode dari gambar untuk menguji fungsi
for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")
print()