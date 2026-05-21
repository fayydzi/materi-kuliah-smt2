def cek_lotre():
    # Angka hasil undian yang sudah ditentukan
    undian = {5, 9, 11, 42, 3, 49}
    
    print("- Program Tebakan Lotre -")
    print(f"Angka undian hari ini: {undian}")
    
    try:
        # menginput 6 angka sekaligus dipisahkan spasi
        user_input = input("\nMasukkan 6 angka tebakan Anda (pisahkan dengan spasi): ")
        
        # Mengubah string input menjadi set angka integer
        tebakan = set(map(int, user_input.split()))
        
        # Validasi jumlah angka
        if len(tebakan) != 6:
            print("Peringatan: Masukkan tepat 6 angka yang berbeda.")
            return

        # Mencari kecocokan
        cocok = tebakan.intersection(undian)
        jumlah_benar = len(cocok)

        # Menampilkan hasil
        print("\n--- Hasil ---")
        print(f"Tebakan Anda : {tebakan}")
        print(f"Angka Cocok  : {list(cocok) if cocok else 'Tidak ada'}")
        print(f"Total Benar  : {jumlah_benar} kali")

    except ValueError:
        print("Kesalahan: Pastikan Anda hanya memasukkan angka.")

cek_lotre()