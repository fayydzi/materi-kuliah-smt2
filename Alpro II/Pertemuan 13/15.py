try:
    x = int("10a")
    y = 5 / 0
except ValueError:
    print("Terjadi kesalahan konversi")
except ZeroDivisionError:
    print("Tidak bisa dibagi nol")