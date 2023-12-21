# a = True

# while a:
#     pilih = input('Pilihan: ')
#     if pilih == 'ya':
#         print('Selamat Datang')
#     elif pilih == 'tidak':
#         print('Sampai Jumpa')

#============PENJELASAN=============
#program diatas adalah program menggunakan loop while yang terus berjalan selaam nilai a adalah True
#pengguna diminta memasukkan pilihan ya atau tidak
#namun, pilihan diluar ya atau tidak, program akan terus berjalan


a = True

while a:
    pilih = input('Pilihan: ')
    if pilih == 'ya':
        print('Selamat Datang')
        break #untuk menghentikan loop
    elif pilih == 'tidak':
        print('Sampai Jumpa')
        break #untuk menghentikan loop



