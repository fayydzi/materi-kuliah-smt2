#kuis faktorial
def faktorial(n):
    # bilangan yang akan difaktorial harus lebih besar dari 0
    if n < 0:
        return None
    
    # 0! dan 1! nilainya sama (1)
    if n < 2:
        return 1
    
    hasil = 1
    # kita mulai perkalian dari 2 sampai n
    for i in range(2, n + 1):
        hasil = hasil * i
    
    return hasil

n = int(input("Masukkan nilai yang ingin di faktorial: "))
print(n, "! = ", faktorial(n))