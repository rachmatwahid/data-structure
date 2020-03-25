# ====
# LIST
# ====

# Deklarasi List
books = ["Harry Potter", "Doraemon", "Tempo"]

# Memutar balikan urutan seluruh elemen
books.reverse()

# Menambah item baru di indeks tertentu
books.insert(1, "Koran Kompas")

# Menghapus elemen di indeks tertentu
books.pop(1)

# Menghapus elemen tertentu berdasarkan nilai
books.remove("Harry Potter")

# Menggabungkan List
paper = ['white paper', 'blank paper', 'white paper']
books.extend(paper)

# Menghitung jumlah kemunculan elemen tertentu
print(books.count("white paper"))

# Menghitung banyak elemen
print(len(books))

# Menemukan indeks elemen tertentu (jika elemen kembar, indeks terkecil yang dipilih)
print(books.index("white paper"))

# Menampilkan List
print(books)

# Menghapus seluruh elemen
books.clear()

# =====
# STACK
# =====

# Menambah elemen baru di atas Stack
books.append("Kamus Indonesia-Inggris")

# Menghapus elemen paling atas Stack
books.pop()

# =====
# QUEUE
# =====

from collections import deque

# Membuat Queue baru
antrian = deque(["Adi", "Nina", "Budi"])

# Menambah elemen baru di Queue (indeks terbesar)
antrian.append("Sandy")

# Menghapus elemen di Queue (indeks terkecil)
antrian.popleft()

print(antrian)