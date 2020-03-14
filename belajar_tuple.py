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

# Slicing pada tuple
print(mahasiswa[1:3])

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
