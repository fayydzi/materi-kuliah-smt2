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