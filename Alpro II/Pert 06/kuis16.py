secret_number = 777

while True:
    angka = int(input("Masukkan angka tebakan: "))

    if angka == secret_number:
        print("Selamat! Tebakan kamu benar.")
        break
    else:
        print("Tebakan salah, coba lagi!")