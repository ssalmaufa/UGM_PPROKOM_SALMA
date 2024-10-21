# Inisialisasi daftar
daftar = [
    [10,15,20],
    [25, 30, 35],
    [40, 45, 50]
]

# Fungsi untuk menghitung jumlah elemen genap dan ganjil
def hitung_genap_ganjil(data):
    jumlah_genap = 0
    jumlah_ganjil = 0
    
    for elemen in data:
        if isinstance(elemen, list):  # Jika elemen adalah list, iterasi melalui elemen di dalamnya
            for sub_elemen in elemen:
                if sub_elemen % 2 == 0:
                    jumlah_genap += 1
                else:
                    jumlah_ganjil += 1
        else:  # Jika elemen adalah angka
            if elemen % 2 == 0:
                jumlah_genap += 1
            else:
                jumlah_ganjil += 1
                
    return jumlah_genap, jumlah_ganjil

# Menghitung jumlah genap dan ganjil
genap, ganjil = hitung_genap_ganjil(daftar)

# Menampilkan hasil
print(f"Jumlah elemen genap: {genap}")
print(f"Jumlah elemen ganjil: {ganjil}")