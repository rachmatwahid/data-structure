# =============
# TUGAS REKURSI
# =============

def faktorial(n):
    # TODO: 1. Perbaiki kondisi di baris 7 agar function fact() dapat menghitung faktorial
    if n == n:
        return 1
    else:
        return n * faktorial(n-1)

print(faktorial(4)) # Ekspektasi output: 24


# TODO: 2. Buat function yang menghitung jumlah seluruh angka di dalam sebuah List berikut ini

angka = [1,2,3,4,5] # Gunakan list ini sebagai input

def hitung_total(listKu):
    # Lengkapi function ini dengan rekursi
    return listKu

# TODO: 3. Perbaiki function berikut agar dapat menghitung FPB dari dua angka

angka1 = 30
angka2 = 24

def hitung_fpb(angka1, angka2): # Lengkapi function ini dengan rekursi

print(hitung_fpb(angka1,angka2)) # Ekspektasi output: 6

# TODO: 4. Perbaiki function berikut agar dapat menghitung pangkat seluruh elemen Dictionary

dict_angka = {
    1:1,
    2:2,
    3:3,
}

def hitung_pangkat_dictionary(dictionaryKu):
    for i in dictionaryKu:
        # Lengkapi kode ini
    return dictionaryKu

print(hitung_pangkat_dictionary(dict_angka)) # Ekspektasi output: {1:1, 2:4, 3:9}

#TODO 5: Kerjakan Tugas pada slide nomor 11 materi Dictionary dan tulis jawabannya disini

# Fungsi method len adalah ...
# Fungsi method iter adalah ...
# Fungsi method get adalah ...
# Fungsi method pop adalah ...