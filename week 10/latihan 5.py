# Membuat array 2 dimensi 4x2 dengan angka dari 10 hingga 17
array_2d = [
    [10, 11],
    [12, 13],
    [14, 15],
    [16, 17]
]

# Menampilkan seluruh elemen pada kolom pertama
print("Elemen pada kolom pertama:")
for line in array_2d:
    print(line[0],end=" ")
