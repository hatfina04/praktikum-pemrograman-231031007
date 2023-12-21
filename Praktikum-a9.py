def judul():
    print('PROGRAM MENGHITUNG LUAS DAN KELILING'.center(45))
    print('BANGUN DATAR PERSEGI'.center(45))
    print()

def inputan():
    panjang = float(input('Masukkan Panjang: '))
    lebar = float(input('Masukkan Lebar: '))
    return panjang, lebar

def hitung(panjang,lebar):
    luas = panjang * lebar
    kel = (panjang+lebar)*2
    return luas, kel

def tampil(pesan,nilai):
    print(f'Hasil Perhitungan nilai {pesan}: {nilai}')

def pilihan():
    pilih = input('Apakah Ingin Melanjutkan? [y/n]')
    if pilih == 'y':
        a = True
    else:
        a = False
        print('Sampai Jumpa')
    return a


a = True
while a: 
    #judul
    judul()
    #inputan panjang dan lebar
    panjang, lebar = inputan()
    #hitung luas dan keliling
    luas,kel = hitung(panjang,lebar)
    #cetak atau display
    tampil('luas', luas)
    tampil('keliling', kel)
    #pilihan
    a = pilihan()