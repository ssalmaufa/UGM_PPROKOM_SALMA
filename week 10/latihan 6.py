# Mendefinisikan dua array multidimensi
Array1 = [
    [4, 6],
    [1, 7]
]

Array2 = [
    [2, 3],
    [5, 6]
]

# Menghitung penjumlahan kedua array
penjumlahan = [[Array1[i][j] + Array2[i][j] for j in range(len(Array1[0]))] for i in range(len(Array1))]

# Menghitung pengurangan kedua array
pengurangan = [[Array1[i][j] - Array2[i][j] for j in range(len(Array1[0]))] for i in range(len(Array1))]

# Menampilkan hasil
print("Hasil Penjumlahan:")
for row in penjumlahan:
    print(row)

print("\nHasil Pengurangan:")
for row in pengurangan:
    print(row)