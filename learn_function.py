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
identitas() # argumen tidak ada

# Membuat function yang bisa mengembalikan nilai
def hitung_pangkat(angka):
    angka = angka ** angka
    return angka
print(hitung_pangkat(2))

# ================
# Cakupan Variabel
# ================

hasil = 0 # ini variabel global

def penjumlahan(angka1,angka2):
    hasil = angka1 + angka2
    return hasil # ini variabel lokal

print("Local variable " + str(penjumlahan(1,2)))
print("Global variable " + str(hasil))
