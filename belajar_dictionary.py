# ==========
# DICTIONARY
# ==========

# Membuat sebuah dictionary
kamus = {
    'eat' : 'makan',
    'sleep' : 'tidur',
    'time' : 'waktu'
}
# Mengakses salah satu elemen (gunakan print untuk menampilkannya)
kamus['eat']

# Menambahkan sebuah elemen baru
kamus['drink'] = 'minum'

# Menghapus salah satu elemen menggunakan key-nya
del kamus['sleep']

# Menampilkan seluruh elemen dalam dictionary
print(kamus)

# Membuat sebuah List berisi seluruh key dari Dictionary
inggris = kamus.keys()

# Membuat sebuah List berisi seluruh value dari Dictionary
indo = kamus.values()

print(indo)