# PERTEMUAN 1 & 2 - REPRESENTASI DATA DALAM PYTHON
# LAPORAN PRAKTIKUM PENGENALAN POLA

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# ==========================================
# 1. OPERASI DASAR LIST
# ==========================================
print("=== 1. OPERASI DASAR LIST ===")
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]

# a. Menggabungkan list
list_gabung = list1 + list2
print(f"a. Hasil Penggabungan: {list_gabung}")

# b. Mengambil nilai (indexing & slicing)
nilai_ambil = list1[1]
print(f"b. Mengambil Nilai indeks ke-1: {nilai_ambil}")

# c. Menyisipkan nilai
list1.insert(1, "orange")
print(f"c. Setelah Menyisipkan 'orange': {list1}")

# d. Menghapus nilai
list1.remove("apple")
print(f"d. Setelah Menghapus 'apple': {list1}")

# e. Mengurutkan isi
list2.sort()
print(f"e. Setelah Mengurutkan list2: {list2}\n")


# ==========================================
# 2. LATIHAN DATA FRAME & MANIPULASI DATA PATIENT (CSV)
# ==========================================
print("=== 2. LATIHAN DATA FRAME & MANIPULASI DATA ===")

# Representasi Data Pasien dari Modul LPK
data_pasien = {
    'Nama Pasien': ['Anto', 'Budi', 'Adi', 'Delima', 'Dodi', 'Tukiyem', 'Rama', 'Santi', 'Mery', 'Yanti', 'Parto', 'Dea'],
    'Umur': [24, 35, 55, 32, 21, 19, 23, 35, 44, 27, 43, 24],
    'Gender': ['L', 'L', 'L', 'P', 'L', 'P', 'L', 'P', 'P', 'P', 'L', 'P'],
    'Diagnosa Sakit': ['Tidak', 'Ya', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Ya', 'Tidak', 'Ya', 'Tidak']
}

df = pd.DataFrame(data_pasien)
print("Dataframe Awal Pasien:")
print(df)
print("-" * 40)

# Latihan Soal dari Modul:
# 1. Berapa rata-rata umur dari data tersebut?
rata_umur = df['Umur'].mean()
print(f"1. Rata-rata umur pasien: {rata_umur:.2f} tahun")

# 2. Tampilkan pasien yang sakit!
pasien_sakit = df[df['Diagnosa Sakit'] == 'Ya']
print("\n2. Daftar Pasien yang Sakit:")
print(pasien_sakit[['Nama Pasien', 'Diagnosa Sakit']])

# 3. Tampilkan pasien yang umurnya > 40
pasien_tua = df[df['Umur'] > 40]
print("\n3. Daftar Pasien dengan Umur > 40:")
print(pasien_tua[['Nama Pasien', 'Umur']])

# 4. Ubahlah diagnosa sakit menjadi angka! (Ya=1, Tidak=0)
df['Diagnosa Sakit'] = df['Diagnosa Sakit'].map({'Ya': 1, 'Tidak': 0})
print("\n4. Dataframe Setelah Mengubah Diagnosa Sakit Menjadi Angka (Ya=1, Tidak=0):")
print(df)
print("\n")


# ==========================================
# 3. MANIPULASI CITRA (OPENCV & MATPLOTLIB)
# ==========================================
print("=== 3. OPERASI CITRA (DUMMY CODE UNTUK GENERASI MATRIX) ===")
# Membuat matriks visual dummy menyerupai logo grayscale berukuran 100x100
dummy_img = np.zeros((100, 100), dtype=np.uint8)
cv2.circle(dummy_img, (50, 50), 30, 255, -1) # Membuat lingkaran putih di tengah

print(f"Shape citra dummy: {dummy_img.shape}")
print(f"Total ukuran pixel: {dummy_img.size}")
print("Akses nilai pixel di koordinat (50,50):", dummy_img[50, 50])
print("Proses manipulasi citra berhasil disimulasikan.")
