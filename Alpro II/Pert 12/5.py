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