import streamlit as st
import sys

# Judul Aplikasi
st.title("🚀 Prototype Manajemen Sequence Data")
st.subheader("Konteks Riset: BERT-LSTM")

# 1. Input kalimat panjang
kalimat = st.text_area("Masukkan kalimat atau paragraf panjang:", 
                       placeholder="Contoh: Belajar Struktur Data untuk implementasi model BERT-LSTM sangat menyenangkan.")

if kalimat:
    # 2. Tokenization (Pecah menjadi list kata)
    tokens = kalimat.split()
    
    # 3. List Comprehension: Filter kata dengan panjang > 3 karakter
    filtered_tokens = [kata for kata in tokens if len(kata) > 3]
    
    # 4. Hitung penggunaan memori
    ukuran_memori = sys.getsizeof(filtered_tokens)
    
    # 5. Output: Tampilkan hasil dalam Dashboard yang rapi
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Kata (Awal)", len(tokens))
    with col2:
        st.metric("Total Kata (Setelah Filter)", len(filtered_tokens))
    
    st.write("### Hasil Tokenisasi (> 3 Karakter):")
    st.info(f"{filtered_tokens}")
    
    st.write("### Analisis Memori:")
    st.warning(f"Total penggunaan memori list tersebut adalah **{ukuran_memori} bytes**.")
    
    # Progress bar sebagai pemanis visual
    st.progress(min(ukuran_memori / 1000, 1.0)) 
else:
    st.write("Silakan masukkan teks pada kolom di atas untuk memulai analisis.")
