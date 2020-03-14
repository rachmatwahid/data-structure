# =====
# TUPLE
# =====
# 1 Immutable, elemennya tidak bisa diganti
# 2 Tipe data setiap elemen bisa berbeda-beda
# 3 Tidak bisa menambah elemen

# Membuat tuple kosong
mahasiswa = ()

# Membuat tuple yang HANYA berisi satu elemen
satu_mahasiswa = ("Adi",)
satu_siswa = ("Nina")

print(type(satu_mahasiswa))
print(type(satu_siswa))

# Membuat tuple
mahasiswa = ("Adi", 21, True)
siswa = "Nina", 7, False

# Menghapus tuple
del siswa

# Menghitung banyak elemen tuple
print(len(mahasiswa))

# Menampilkan tuple
print(mahasiswa)

# Menggabungkan tuple
mahasiswa = mahasiswa + ("Ani", 20, False)

# Mengakses elemen tuple
print(mahasiswa[0])

angka = (1, 2, 3, 4, 5)

# Slicing yang menghasilkan satu elemen
print(angka[3:4]) # outputnya dalam bentuk tuple satu elemen

# Slicing yang menghasilkan lebih dari satu elemen
print(angka[2:4])

# Menukar nilai variable
x = 1
y = 2
(x,y) = (y,x)
print(x)
print(y)

# Mengembalikan beberapa nilai dari function
def bagi_sisa(angka1, angka2):
    hasil = angka1 / angka2
    sisa = angka1 % angka2
    return  (hasil, sisa)

bagi_sisa(4,2) # mengakses kedua nilai

# Perulangan di dalam tuple
buah = "apple", "mango", "banana"
for i in buah:
    print(i)

# Perulangan untuk menemukan elemen tuple
if "apple" in buah:
    print("Ada apel")

# Mengubah List menjadi Tuple
motor = ["Yamaha", "Honda", "Vario"]
motor = tuple(motor) # konversi ke tuple
print(type(motor))

# Mengubah string menjadi tuple
nama = "Adinda"
nama = tuple(nama)
print(nama)
