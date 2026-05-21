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