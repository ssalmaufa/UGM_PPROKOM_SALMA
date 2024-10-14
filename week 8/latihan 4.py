jumlah_elemen = int(input("Masukkan jumlah elemen dalam array: "))

array = list(range(1, jumlah_elemen + 1))

print("Array yang dihasilkan:")
print(array)

bilangan = int(input("Masukkan bilangan bulat untuk mencari kelipatan: "))

kelipatan = [num for num in array if num % bilangan == 0]

if kelipatan:
    print("Elemen-elemen yang merupakan kelipatan dari", bilangan, "adalah:")
    print(kelipatan)
else:
    print("Tidak ada elemen yang merupakan kelipatan dari", bilangan)