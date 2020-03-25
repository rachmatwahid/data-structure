# ========
# REKURSIF
# ========

# Contoh Perulangan

def perkalian_perulangan(angka1, angka2):
    hasil = 0
    while angka2 > 0:
        hasil += angka1
        angka2 -= 1
    return hasil


print(perkalian_perulangan(3,4)) # coba perkalian lainnya

# Contoh Rekursi

def perkalian_rekursi(angka1, angka2):
    if angka2 == 1:
        return angka1
    else:
        return angka1 + perkalian_rekursi(angka1, angka2 - 1) # function ini memanggil dirinya sendiri
    # tidak ada perulangan apapun di function ini


print(perkalian_rekursi(3,4)) # coba perkalian lainnya


# Contoh Faktorial dengan Perulangan


def faktorial_perulangan(angka):
    hasil = 1
    for i in range(1, angka + 1):
        hasil *= i
    return hasil


print(faktorial_perulangan(3)) # coba faktorial bilangan lainnya
