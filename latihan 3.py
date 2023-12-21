nama = str(input('Masukkan Nama Karyawan: '))
pendapatan = int(input('Pendapatan: '))

if pendapatan > 1000:
    print('Status: Berhak')
else:
    print('Status: Tidak Berhak')