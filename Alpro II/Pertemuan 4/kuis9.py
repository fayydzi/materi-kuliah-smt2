jam = int(input("Waktu mulai jam: "))
menit = int(input("Waktu mulai menit: "))
durasi = int(input("Durasi Acara menit: "))

menit += durasi
jam += menit // 60
menit = menit % 60
jam = jam % 24

print(f"Acara berakhir pukul {jam}:{menit} ")