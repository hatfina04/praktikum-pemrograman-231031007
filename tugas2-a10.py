# 1. Program penjumlahan waktu
def tambah_waktu(waktu1, waktu2):
    total_detik = waktu1 + waktu2
    jam = total_detik // 3600
    sisa_detik = total_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60
    return jam, menit

jam1 = int(input('Masukkan jam pertama: '))
menit1 = int(input('Masukkan menit pertama: '))

jam2 = int(input('Masukkan jam kedua: '))
menit2 = int(input('Masukkan menit kedua: '))

total_jam, total_menit= tambah_waktu((jam1 * 3600 + menit1 * 60),
                                     (jam2 * 3600 + menit2 * 60))

print(f'Waktu sekarang menunjukkan Pukul {total_jam}:{total_menit}')

# 2. Program selisih waktu 
def selisih_waktu(waktu1, waktu2):
    selisih_detik = abs(waktu1 - waktu2)
    jam = selisih_detik // 3600
    sisa_detik = selisih_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60
    return jam, menit

jam1 = int(input("Masukkan jam pertama: "))
menit1 = int(input("Masukkan menit pertama: "))

jam2 = int(input("Masukkan jam kedua: "))
menit2 = int(input("Masukkan menit kedua: "))

selisih_jam, selisih_menit= selisih_waktu((jam1 * 3600 + menit1 * 60 ),
                                                          (jam2 * 3600 + menit2 * 60 ))

print(f'Waktu sekarang menunjukkan Pukul {selisih_jam}:{selisih_menit}')
















