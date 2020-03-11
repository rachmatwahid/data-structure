# Deklarasi Stack
books = ["Harry Potter", "Doraemon", "Tempo"]

# Menambah item baru
books.append("Kamus Indonesia-Inggris")

# Menghapus elemen di indeks terakhir
books.pop()

# Menghapus elemen di indeks tertentu
books.pop(1)

# Menghapus elemen tertentu berdasarkan nilai
books.remove("Harry Potter")

# Menghapus seluruh elemen
books.clear()

# Menghitung banyak elemen
print(len(books))
