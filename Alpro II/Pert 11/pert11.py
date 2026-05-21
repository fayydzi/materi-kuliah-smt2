#no 1
def fungsi():
    print("Halo")
    return
    print("Tidak tampil")

fungsi()

#n02
def fungsi(harapan):
    if harapan == False:
        return
    print("Berhasil")

fungsi(False)

#no3
def fungsi():
    return 123

x = fungsi()
print(x)

#no4
def fungsi():
    print("Dipanggil")
    return 123

fungsi()

#no5
def fungsi():
    print("Halo")

x = fungsi()
print(x)

#no6
def tampil(data):
    for i in data:
        print(i)

list_data = [1, 2, 3]
tampil(list_data)

#no7
def tampil(data):
    print(data)

tampil([10, 20, 30])

#no8
def buat_list():
    return [1, 2, 3]

hasil = buat_list()
print(hasil)

#kuis 23
def tahun_kabisat(tahun):
    # tahun kabisat jika:
    # habis dibagi 4 DAN tidak habis dibagi 100
    # ATAU habis dibagi 400
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False


data_uji = [1900, 2000, 2016, 1987]
data_hasil = [False, True, True, False]

for i in range(len(data_uji)):
    th = data_uji[i]
    print(th, "->", end=" ")
    
    hasil = tahun_kabisat(th)
    
    if hasil == data_hasil[i]:
        print("OK")
    else:
        print("Gagal")

#kuis 24
def tahun_kabisat(tahun):
    # Tahun kabisat adalah tahun yang habis dibagi 4, 
    # kecuali tahun abad (akhiran 00) yang harus habis dibagi 400.
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

def hari_didalam_bulan(tahun, bulan):
    # Daftar jumlah hari standar (Index 0 dikosongkan agar bulan 1 = index 1)
    # [Jan, Feb, Mar, Apr, Mei, Jun, Jul, Ags, Sep, Okt, Nov, Des]
    hari_per_bulan = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Jika bulan adalah Februari (2) dan tahunnya kabisat, maka ada 29 hari
    if bulan == 2 and tahun_kabisat(tahun):
        return 29
    else:
        return hari_per_bulan[bulan]

# Bagian Pengujian 
data_uji = [1900, 2000, 2016, 1987]
data_bulan = [2, 2, 1, 11]
data_hasil = [28, 29, 31, 30]

for i in range(len(data_uji)):
    thn = data_uji[i]
    bln = data_bulan[i]
    print(f"{thn}, {bln} -> ", end="")
    
    hasil = hari_didalam_bulan(thn, bln)
    
    if hasil == data_hasil[i]:
        print(f"{hasil} (Ok)")
    else:
        print(f"{hasil} (Gagal)")

#kuis 25
def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    return False

def hari_didalam_bulan(tahun, bulan):
    if bulan < 1 or bulan > 12:
        return None
    hari_per_bulan = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if bulan == 2 and tahun_kabisat(tahun):
        return 29
    return hari_per_bulan[bulan]

def hari_pada_tahun(tahun, bulan, hari):
    # 1. Validasi input dasar
    if bulan < 1 or bulan > 12 or hari < 1:
        return None
    
    # 2. Validasi apakah jumlah hari melebihi batas bulan tersebut
    batas_hari = hari_didalam_bulan(tahun, bulan)
    if hari > batas_hari:
        return None
        
    # 3. Hitung total hari dari bulan-bulan sebelumnya
    total_hari = 0
    for m in range(1, bulan):
        total_hari += hari_didalam_bulan(tahun, m)
    
    # 4. Tambahkan hari di bulan berjalan
    total_hari += hari
    return total_hari

# Test sesuai permintaan di gambar
print(hari_pada_tahun(2000, 12, 31))

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

#kuis 27
def cek_prima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False
    return True

# Bagian pengujian
for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")
print()

def Liter100km_ke_mpg(liter):
    # 100 km dalam mil = 100000 meter / 1609.344 meter
    mil = 100 / 1.609344
    # Liter ke galon
    galon = liter / 3.785411784
    return mil / galon

def mpg_ke_Liter100km(mpg):
    # 1 galon dalam liter
    liter = 3.785411784
    # mpg (mil per galon) dikonversi ke km per galon
    km100 = (mpg * 1.609344) / 100
    return liter / km100


print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.0))
print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))


