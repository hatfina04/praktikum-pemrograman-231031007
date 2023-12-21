import os
os.system('clear')

 
nim = ('2','3','1','0','3','1','0','0','7')
#nim2 = '231031007'
print(nim)
#print(nim2[1:3])

#akses item
print(f'item indeks 0:{nim[0]}')
print(f'item indeks 4:{nim[4]}')
print(f'item indeks terakhir:{nim[len(nim)-1]}')


#akses indeks negatif
print(f'item indeks terakhir:{nim[-1]}')
print(f'item indeks pertama:{nim[-len(nim)]}')
print(f'item indeks 6 [-3]:{nim[-3]}')
print(f'item indeks 4 [-5]:{nim[-5]}')
print(f'item indeks 7 [-2]:{nim[-2]}')

#akses indeks batas
print(f'item indeks 1,2,....: \n{nim[1:]}')
print(f'item indeks 3,4,....: \n{nim[3:]}')
print(f'item indeks 0,1,2: \n{nim[:3]}')
print(f'item indeks 0,1,2,3: \n{nim[:4]}')
print(f'item indeks semua: \n{nim[:]}')
print(f'item indeks [:6]: \n{nim[:-3]}')
print(f'item indeks [:8]: \n{nim[:-1]}')

#pengirisan
print(f'item indeks [1,2]: \n{nim[1:3]}')
print(f'item indeks [2,3,4]: \n{nim[2:5]}')
print(f'item indeks kosong: \n{nim[3:3]}')
print(f'item indeks [8:8] kosong: \n{nim[-1:-1]}')
print(f'item indeks [1:8] kosong: \n{nim[1:-1]}')
print(f'item indeks [2:7] kosong: \n{nim[2:-2]}')



data = ['Hatfina Rustamin',2023,'Aktif'] 
nilai= [87,69,43,97] 
print('Nama: '+ data[0]) 
print('angkatan:', data[1]) 
print('status: '+ data[2])

print(f'{data[0]} status Kuliah: {data[2]}')
print(f'Data terbesar nilai adalah:{max(nilai)}')
print(f'Data terkecil nilai adalah:{min(nilai)}')
print(f'Rata-rata nilai adalah:{sum(nilai)/len(nilai)}')

data = ('mahasiswa1',2023,'Aktif') 
nilai= (90,89,93,97) 
print(data[1]) 
print(data[-1]) 
print(nilai[1:-1])

print(f'Jumlah nilai {data[0][0]} adalah: 4')
print(f'Data terbesar nilai adalah:{max(nilai)}')
print(f'Data terkecil nilai adalah:{min(nilai)}')
print(f'Rata-rata nilai adalah:{sum(nilai)/len(nilai)}')



data = [['Hatfina',2023,'Aktif'], 
[90,89,93,97], 
[20,22], 
['S1-Reguler','Ganjil']] 

matkul = ['Agama', 'Pancasila', 'Bahasa', 'Cinta']
sks  = [2,2,2,2]
# Tambahkan matkul dan sks ke dalam data (di akhir)
matkul.append('Pemrogaraman')
sks.append(3)
# Tambahkan 3 matkul dengan sks nya
matkul_= ['PTI', 'Kalkulus', 'Sains']
matkul.extend(matkul_)
sks_= [3,3,3]
sks.extend(sks_)
# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print('Mata Kuliah 1:',matkul [0],'dengan jumlah sks :',sks [0])
# Mata kuliah 2: Matkul2 dengan jumlah 3 sks
print('Mata Kuliah 2:',matkul [1],'dengan jumlah sks :',sks [1])
# Mata kuliah 3: Matkul3 dengan jumlah 3 sks
print('Mata Kuliah 3:',matkul [2],'dengan jumlah sks :',sks [2])
# Mata kuliah 4: Matkul4 dengan jumlah 2 sks
print('Mata Kuliah 4:',matkul [3],'dengan jumlah sks :',sks [3])
# Mata kuliah 5: Matkul5 dengan jumlah 2 sks
print('Mata Kuliah 5:',matkul [4],'dengan jumlah sks :',sks [4])
# Mata kuliah 6: Matkul6 dengan jumlah .. sks
print('Mata Kuliah 6:',matkul [5],'dengan jumlah sks :',sks [5])
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
print('Mata Kuliah 7:',matkul [6],'dengan jumlah sks :',sks [6])
# Mata kuliah 8: Matkul8 dengan jumlah .. sks
print('Mata Kuliah 8:',matkul [7],'dengan jumlah sks :',sks [7])

# Tambahkan 8 nilai masing-masing


print(data[0][0]) 
print(data[-1][0]) 
print(data[2][0:])
print()

# >> Tugas: Nama Mahasiswa  dengan NIM: 231031007
print(f'Nama Mahasiswa:',data[0][0], 'dengan NIM:',nim[0], nim[1],nim[2],nim[3],nim[4],nim[5],nim[6],nim[7],nim[8])
#>> Program pendidikan Thomas: S1-Reguler
print(f'program pendidikan {data[0][0]}: {data[3][0]}')
#>> Angkatan : 2023-Ganjil
print(f'Angkatan: {data[0][1]}-{data[3][1]}')
#>> Jumlah nilai Thomas adalah: 4
print(f'Jumlah nilai {data[0][0]} adalah: {len(data[1])}')
#>> Data terbesar Thomas adalah: 97
print(f'Data terbesar {data[0][0]} adalah:{max(data[1])}')
#>> Data terkecil Thomas adalah: 89
print(f'Data terkecil {data[0][0]} adalah:{min(data[1])}')
#>> Rata-rata nilai Thomas adalah: 92.25
x_bar = sum(data[1])/len(data[1])
print(f'Rata-rata {data[0][0]} adalah:{x_bar}')











