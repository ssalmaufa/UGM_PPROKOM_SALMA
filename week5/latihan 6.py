#deklarasi variabel
var_nilai=0
var_i=1
#perulangan WHILE
while(var_nilai<10):
    print("Perulangan pertama Ke",var_nilai)
    while(var_i<3):
        print("Perulangan ke",var_nilai,",",var_i)
        var_i+=1
    var_i=1
    var_nilai+=1
#diluar_perulangan var_nilai
print("var_nilai=",int(var_nilai),"=10.Bernilai False")
