# ==============
# LEARN FUNCTION
# ==============

# Membuat function
def salam():
    print("Selamat pagi!") # perhatikan tabnya!

# Menggunakan/memanggil function
salam()

# Membuat function dilengkapi argumen/parameter
def perkenalan(nama):
    print("Perkenalkan, nama saya " + nama)
perkenalan("Adi")
perkenalan("Nina")

# Membuat function dilangkapi dengan beberapa parameter
def biografi(nama, kota):
    print("Nama saya " + nama + " saya berasal dari " + kota)
biografi("Dian", "Bandung")

# Memanggil function dengan argumen yang memiliki keyword
biografi(kota="Jakarta", nama="Dian")

# Membuat function dengan parameter yang nilainya default
def identitas(nama = "Fulan"):
    print("Hai, nama saya " + nama)
identitas() # argumen tidak ada, Fulan menjadi argumennya
identitas("Dian")

# Membuat function yang bisa mengembalikan nilai
def hitung_pangkat(angka):
    angka = angka ** angka
    return angka
print(hitung_pangkat(2))

# ================
# Cakupan Variabel
# ================

# 1. Jika variabel berada di luar function, disebut variabel global
# 2. Jika berada di dalam function, disebut variabel lokal
# 3. Walaupun identifier-nya sama, tapi nilainya berbeda

hasil = 0 # ini variabel global

def penjumlahan(angka1,angka2):
    hasil = angka1 + angka2
    return hasil # ini variabel lokal

print("Local variable " + str(penjumlahan(1,2))) # nilainya 3
print("Global variable " + str(hasil)) # nilainya nol
