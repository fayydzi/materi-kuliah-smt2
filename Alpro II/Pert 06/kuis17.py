# meminta user memasukkan kata
user_word = input("Masukkan sebuah kata: ")

# mengubah kata menjadi huruf kapital
user_word = user_word.upper()

# perulangan untuk membaca setiap huruf
for huruf in user_word:
    if huruf == "A":
        continue
    elif huruf == "I":
        continue
    elif huruf == "U":
        continue
    elif huruf == "E":
        continue
    elif huruf == "O":
        continue
    else:
        print(huruf)