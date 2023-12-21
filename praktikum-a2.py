print('praktikum-a2\n')

print('NAMA     : HATFINA RUSTAMIN')
print('NIM      : 231031007')
print('Prodi    : Sistem Informasi A\n')

#INI OPERATOR ASSIGNMENT
a = 19
print('Nilai a adalah', a)
a += 3
print('Nilai a+= adalah', a)

a = 19
print('Nilai a adalah', a)
a -= 3
print('Nilai a-= adalah', a)

a = 19
print('Nilai a adalah', a)
a *= 2
print('Nilai a*= adalah', a)

a = 19
print('Nilai a adalah', a)
a /= 2
print('Nilai a/= adalah', a)

a = 3
print('Nilai a adalah', a)
a **= 2
print('Nilai a**= adalah', a)

a = 19
print('Nilai a adalah', a)
a %= 4
print('Nilai a%= adalah', a)

a = 35
print('Nilai a adalah', a)
a %= 32
print('Nilai a%= adalah', a)

a = 35
print('Nilai a adalah', a)
a //= 32
print('Nilai a//= adalah', a, '\n')

#Tugas melanjutkan untuk operator selanjutnya line 25-line 59
#OR
b = True
print('Nilai b =', b)
b|= False
print('Nilai b|= False akan menjadi', b)
b = False
print('Nilai b =', b)
b|= False
print('Nilai b|= False akan menjadi', b)

#AND
b = True
print('Nilai b =', b)
b&= False
print('Nilai b&= False akan menjadi', b)
b = False
print('Nilai b=', b)
b&= False
print('Nilai b&=False akan menjadi', b)

#XOR
b = True
print('Nilai b =',b)
b^= False
print('Nilai b^=False akan menjadi',b)
b = False
print('Nilai b =',b)
b^= False
print('Nilai b^= False akan menjadi',b)

#Shifting
c = 0b0100
print('Nilai c =', format(c, '04b'))
c>>=1
print('Nilai c>>=1 akan menjadi', format(c, '04b'))
c=0b0100
c<<=1
print('Nilai c<<=1 akan menjadi', format(c, '04b'))

#OPERATOR PERBANDINGAN
a = 9
b = 13
print('\n--------- Besar dari 7')
hasil = a > 7
print(a, '> 13 adalah', hasil)
hasil = b > 7
print(b, '> 13 adalah', hasil)

print('\n--------- Kecil dari 7')
hasil = a < 7
print(a, '< 13 adalah', hasil)
hasil = b < 7
print(b, '< 13 adalah', hasil)

print('\n--------- Besar atau Sama dari dari 7')
# hasil = a >= 7
# hasil = b >= 7
hasil = a >= 7
print(a, '>= 13 adalah', hasil)
hasil = b >= 7
print(b, '>= 13 adalah', hasil)

print('\n--------- Kecil atau Sama dari dari 7')
# hasil = a <= 7
# hasil = b <= 7
hasil = a <= 7
print(a, '<= 13 adalah', hasil)
hasil = b <= 7
print(b, '<= 13 adalah', hasil)

print('\n--------- Sama dari dari 7')
# hasil = a == 7
# hasil = b == 7
hasil = a == 7
print(a, '== 13 adalah', hasil)
hasil = b == 7
print(b, '== 13 adalah', hasil)

print('\n--------- Tidak Sama dari dari 7')
# hasil = a != 7
# hasil = b != 7
hasil = a != 7
print(a, '!= 13 adalah', hasil)
hasil = b != 7
print(b, '!= 13 adalah', hasil)

#OPERATOR LOGIKA
a = True
b = False
print('\n========AND========')

hasil = a and a
print(a,'and', a, 'hasilnya=', hasil)

hasil = a and b
print(a,'and', b, 'hasilnya=', hasil)

hasil = b and a
print(b,'and', a, 'hasilnya=', hasil)

hasil = b and b
print(b,'and', b, 'hasilnya=', hasil)

print('\n========OR========')
# Tugas hasil = a or a
# Tugas hasil = a or b
# Tugas hasil = b or a
# Tugas hasil = b or b
hasil = a or a
print(a,'or', a, 'hasilnya=', hasil)

hasil = a or b
print(a,'or', b, 'hasilnya=', hasil)

hasil = b or a
print(b,'or', a, 'hasilnya=', hasil)

hasil = b or b
print(b,'or', b, 'hasilnya=', hasil)

print('\n========XOR========')
hasil = a ^ a
print(a,'xor', a, 'hasilnya=', hasil)

hasil = a ^ b
print(a,'xor', b, 'hasilnya=', hasil)

hasil = b ^ a
print(b,'xor', a, 'hasilnya=', hasil)

hasil = b ^ b
print(b,'xor', b, 'hasilnya=', hasil)

print('\n========NOT========')

hasil = not a
print('not', a, 'hasilnya =', hasil)

#OPERATOR MEMBERSHIP
print('\n=========IN=========')
nama = 'Hatfina'
test = 'fi'
cek = test in nama
print(test,'terdapat di', nama, 'adalah', cek)

test = 'if'
cek = test in nama
print(test,'terdapat di', nama, 'adalah', cek)

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 in nama
print(test1, 'terdapat di', nama, 'adalah', cek)
cek = test2 in nama
print(test2, 'terdapat di', nama, 'adalah', cek)
cek = test3 in nama
print(test3, 'terdapat di', nama, 'adalah', cek)
cek = test4 in nama
print(test4, 'terdapat di', nama, 'adalah', cek)
cek = test5 in nama
print(test5, 'terdapat di', nama, 'adalah', cek)

print('\n============NOT IN============')
#Tugas lanjutkan untuk NOT IN dengan cara yang sama
nama = 'Hatfina Rustamin'
test = 'an'
cek = test not in nama
print(test,'tidak terdapat di', nama, 'adalah', cek)

test = 'tam'
cek = test not in nama
print(test,'tidak terdapat di', nama, 'adalah', cek)

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 not in nama
print(test1, 'tidak terdapat di', nama, 'adalah', cek)
cek = test2 not in nama
print(test2, 'tidak terdapat di', nama, 'adalah', cek)
cek = test3 not in nama
print(test3, 'tidak terdapat di', nama, 'adalah', cek)
cek = test4 not in nama
print(test4, 'tidak terdapat di', nama, 'adalah', cek)
cek = test5 not in nama
print(test5, 'tidak terdapat di', nama, 'adalah', cek)