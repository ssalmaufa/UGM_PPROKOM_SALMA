#Program Persyaratan SIM
umur=int(input("Masukan Umur Anda="))
nilai=int(input("Masukkan Nilai tes anda="))
lulus="Selamat Anda Berhak Mendapatkan Sim Anda"
gagal="Maaf, Anda tidak berhak mendaopatkan sim anda\nSilahkan coba lagi bulan atau tahun depan"
if(umur>17):
    if(nilai<60):
        print()
        print(gagal)
    else:
        print()
        print(lulus)
else:
    print()
    print(gagal)
