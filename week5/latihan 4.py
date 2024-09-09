jumlah_data=int(input("masukkan jumlah data yang ingin dihitung rata-ratanya:"))
data=[]
for i in range (jumlah_data):
    angka=float(input(f"Masukkan angka ke-{i+1}:"))
    data.append(angka)
rata_rata= sum(data)/jumlah_data

print(f"rata-rata dari {data} adalah {rata_rata}")
