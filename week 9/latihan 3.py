# Fungsi untuk mengecek apakah sebuah angka adalah bilangan prima
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Array input
array_input = [4, 5, 11, 12, 14, 16, 16, 19]

# Mencari bilangan prima dalam array
bilangan_prima = [num for num in array_input if is_prime(num)]

# Menghitung jumlah bilangan prima
jumlah_bilangan_prima = len(bilangan_prima)

# Menampilkan hasil
print("Bilangan prima dalam array:", bilangan_prima)
print("Jumlah bilangan prima:", jumlah_bilangan_prima)