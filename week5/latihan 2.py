awal=int(input("Masukkan saldo awal\t:"))
sisa=awal   #bila tidak ada pengeluaran
while(True):
    pengeluaran=int(input("Masukkan pengeluaran hari ini (0 untuk keluar):"))
    if pengeluaran==0:
        print("sisa saldo=",sisa)
    sisa=sisa-pengeluaran
    if sisa <0:
        print("saldo tidak mencukupi")
        print("sisa saldo",sisa+pengeluaran)
        break
