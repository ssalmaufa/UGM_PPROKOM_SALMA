# Array input
array_input = [1, 5, 4, 6, 7, 12, 45, 9, 99, 55, 100, 88, 75, 60]

# Membuat array untuk menyimpan angka ganjil dan genap
angka_ganjil = []
angka_genap = []

# Memisahkan angka ganjil dan genap
for num in array_input:
    if num % 2 == 0:
        angka_genap.append(num)
    else:
        angka_ganjil.append(num)

# Menghitung total angka ganjil dan genap
total_ganjil = len(angka_ganjil)
total_genap = len(angka_genap)

# Menampilkan hasil
print("ini adalah angka genap:", angka_genap)
print("Total angka genap:", total_genap)
print("ini adalah Angka ganjil:", angka_ganjil)
print("Total angka ganjil", total_ganjil)