angka = []

for i in range(5):
    input_angka = float(input("Masukkan angka ke-{}: ".format(i+1)))
    angka.append(input_angka)
    print("Angka yang telah dimasukkan sejauh ini: ", angka)

jumlah_total = sum(angka)

print("\nPilih menu:")
print("1. Lihat jumlah dari semua angka yang dimasukkan")
print("2. Lihat rata-rata dari angka-angka tersebut")

pilihan = int(input("Masukkan pilihan Anda: "))

if pilihan == 1:
    print("Jumlah dari semua angka yang dimasukkan: ", jumlah_total)
elif pilihan == 2:
    rata_rata = jumlah_total / len(angka)
    print("Rata-rata dari angka-angka tersebut: ", rata_rata)
else:
    print("Pilihan tidak valid") 