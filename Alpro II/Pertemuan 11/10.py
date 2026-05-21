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

# --- Bagian Pengujian 
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