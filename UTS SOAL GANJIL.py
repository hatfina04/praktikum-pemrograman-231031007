''' UTS
1. Buat variabel jenis list berikut.
    
    Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu hasil studi mahasiswa',
            'Nama Lengkap',
            'NIM',
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil',
            'aktif',
            'Tanggal-Bulan-Tahun Lahir']
#(NOTED: sesuaikan dengan data anda)


2. Buat variabel nested list berikut.

MK =   [['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [3,2,3,2,3,3,3,2],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, dan Nilai)

3. Buat Kode dengan hasil runing seperti berikut.


            INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                           JURUSAN SAINS
                    KARTU HASIL STUDI MAHASISWA
                          GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : NIM
Program/Prodi   : S1/Sistem Informasi A
Tahun Masuk     : 2023-Ganjil
Status          : Aktif
|--|--   12   --|--             31            --|-- 7 --|--    13   --|
-----------------------------------------------------------------------
No. Kode        |           Mata Kuliah         |  SKS  | Nilai (0-4) |
-----------------------------------------------------------------------
1   22A1209     | Matkul1                       |   3   |         3.50|
2   22A1210     | Matkul2                       |   2   |         3.00|
3   22A1211     | Matkul3                       |   3   |         3.75|
4   22A1212     | Matkul4                       |   2   |         4.00|
5   22A1213     | Matkul5                       |   3   |         3.75|
6   22A1214     | Matkul6                       |   3   |         3.50|
7   22A1215     | Matkul7                       |   3   |         3.75|
8   22A1216     | Matkul8                       |   2   |         3.00|
-----------------------------------------------------------------------
                                       TOTAL SKS:   21
-----------------------------------------------------------------------
|---------------------------------71-----------------------------------|
Summary:
Jumlah Mata Kuliah : 8 Mata Kuliah
Nilai Tertinggi    : 4.00  (22A1212 - Matkul4)
Nilai Terendah     : 3.00  (22A1211 - Matkul2)
IP Kumulatif       : 3.00
                                   
                                               Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''



# Tulis Kode Jawaban di bawah!
Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu hasil studi mahasiswa',
            'Hatfina Rustamin',
             231031007,
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil',
            'aktif',
             '4 Januari 2005']
MK =   [['Pemrograman','Kaldas','Sainster','Bahasa','PTI','Cinta','Pancasila','Agama'],
        [3,3,3,2,3,2,2,2],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.45,3.65,3.35,4.00,3.85,3.00,3.85,3.85]]

sp=71
print(Bio[0].upper().center(sp))
print(Bio[2].upper().center(sp))
print(Bio[3].upper().center(sp))
strr = Bio[-3]+' '+Bio[-4].replace('-','/')
print(strr.upper().center(sp))
print()

print(f'''
Nama Lengkap    : {Bio[4].upper()}
NIM             : {Bio[5]}
Program/prodi   : {Bio[6]}/{Bio[7]}
Tahun Masuk     : {Bio[8][:4]}-{Bio[9].title()}
Status          : {Bio[-2].title()}''')
print()

print('-'*71)
print('No. Kode'.ljust(16)+'|'+'Mata Kuliah'.center(31)+'|'+'SKS'.center(7)+'|'+'Nilai (0-4)'.center(13)+'|')
print('-'*71)
print(f'1   {MK[2][0]}'.ljust(16)+'|'+f'{MK[0][0]}'.center(31)+'|'+f'{MK[1][0]}'.center(7)+'|'+f'{MK[3][0]}'.rjust(13)+'|')
print(f'2   {MK[2][1]}'.ljust(16)+'|'+f'{MK[0][1]}'.center(31)+'|'+f'{MK[1][1]}'.center(7)+'|'+f'{MK[3][1]}'.rjust(13)+'|')
print(f'3   {MK[2][2]}'.ljust(16)+'|'+f'{MK[0][2]}'.center(31)+'|'+f'{MK[1][2]}'.center(7)+'|'+f'{MK[3][2]}'.rjust(13)+'|')
print(f'4   {MK[2][3]}'.ljust(16)+'|'+f'{MK[0][3]}'.center(31)+'|'+f'{MK[1][3]}'.center(7)+'|'+f'{MK[3][3]}'.rjust(13)+'|')
print(f'5   {MK[2][4]}'.ljust(16)+'|'+f'{MK[0][4]}'.center(31)+'|'+f'{MK[1][4]}'.center(7)+'|'+f'{MK[3][4]}'.rjust(13)+'|')
print(f'6   {MK[2][5]}'.ljust(16)+'|'+f'{MK[0][5]}'.center(31)+'|'+f'{MK[1][5]}'.center(7)+'|'+f'{MK[3][5]}'.rjust(13)+'|')
print(f'7   {MK[2][6]}'.ljust(16)+'|'+f'{MK[0][6]}'.center(31)+'|'+f'{MK[1][6]}'.center(7)+'|'+f'{MK[3][6]}'.rjust(13)+'|')
print(f'8   {MK[2][7]}'.ljust(16)+'|'+f'{MK[0][7]}'.center(31)+'|'+f'{MK[1][7]}'.center(7)+'|'+f'{MK[3][7]}'.rjust(13)+'|')
print('-'*71)
print(f'                                       TOTAL SKS:  {sum(MK[1])}')
print('-'*71)
str1= '71'
a = str1.center(71,'-')
print(a)
rata_rata= sum(MK[3]) / len(MK[1])
nilai = [MK[1][0] * MK[3][0],
         MK[1][1] * MK[3][1],
         MK[1][2] * MK[3][2],
         MK[1][3] * MK[3][3],
         MK[1][4] * MK[3][4],
         MK[1][5] * MK[3][5],
         MK[1][6] * MK[3][6],
         MK[1][7] * MK[3][7]]
rataan = sum(nilai)/sum(MK[1])

print(f''' 
Summary:
Jumlah Mata Kuliah : {len(MK[1])} Mata Kuliah
Nilai Tertinggi    : {max(MK[3])}  ({MK[2][3]}-{MK[0][3]})
Nilai Terendah     : {min(MK[3])}  ({MK[2][3]}-{MK[0][3]})
IP Kumulatif       : {rataan}
''')

nama_kota = Bio[1]
tanggal = Bio[-1]
gabung = (nama_kota+", "+tanggal).rjust(73)
print(gabung)
print("\n"*4)
nama = Bio[4]
strip_akhir = "-"*12
print(nama.rjust(69))
print(strip_akhir.rjust(67))

