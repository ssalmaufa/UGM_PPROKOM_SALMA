matriks = [[0, 0, 0], [0, 0, 0]]


for i in range(2):  # Untuk baris
    for j in range(3):  # Untuk kolom
        nilai = input(f"Masukkan nilai untuk matriks[{i}][{j}]: ")
        matriks[i][j] = nilai


print("\nMatriks yang telah dimasukkan:")
for baris in matriks:
    print(baris)