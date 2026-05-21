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