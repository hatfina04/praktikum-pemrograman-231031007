# Tugas 1 : Buat program
# a. Input bilangan X
# b. Cek : jika ganjil maka cetak (“X adalah bilangan Ganjil ”)
# c. Jika tidak Maka cetak (“X adalah bilangan Bukan Ganjil”)
# d. Selesai

x = int(input('Masukkan nilai x: '))
print('x adalah bilangan', 'Ganjil' if(x % 2 != 0) else 'Bukan Ganjil')

bilangan = input('Masukan bilangan: ')
if bilangan % 2 != 0:
    print (f'{bilangan} adalah bilangan Ganjil')
else:
    print (f'{bilangan} adalah bilangan Bukan Ganjil')














