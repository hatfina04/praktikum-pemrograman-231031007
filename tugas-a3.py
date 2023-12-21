print('Tugas Praktikum 3'.center(40))
nama = 'Hatfina Rustamin'
nim  = '231031007'
prodi= 'Sistem Informasi A'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi} ''')

print('\n')
'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''


str1 = 'duFort Frankel Von Neumann'
#output: NEUMANN DUFORT FRANKEL VON
a= ((str1[-7:])+(str1[6])+(str1[:18])) 
b= a.upper() 
print (b) 

str2 = 'duFort Frankel Von Neumann'
#output: DFV NEUMANN
a2=((str2[0])+(str2[7])+(str2[15])+(str2[18:26])) 
b2= a2.upper() 
print (b2) 

str3 = 'duFort Frankel Von Neumann'
#output: DUFORT FVN
a3 = ((str3[:7])+(str3[7])+(str3[15])+(str3[19]))
b3 = a3.upper()
print(b3)

str4 = 'duFort Frankel Von Neumann'
#output: N duFort FV
a4= ((str4[19])+(str4[6])+(str4[:7])+(str4[7])+(str4[15])) 
print (a4) 

str5 = 'duFort Frankel Von Neumann'
#output: NEUMANN d f v
a5 = ((str5[-7:].upper())+(str5[6])+(str5[0])+(str5[6:8].lower())+(str5[14:16].lower()))
print(a5)

str6 = 'duFort Frankel Von Neumann'
#output: NEUMANN DFV
a6 = ((str6[-7:].upper())+(str6[6])+(str6[0].upper())+(str6[7:8])+(str6[15:16]))
print(a6)

str7 = '@duFort Frankel Von Neumann$'
#output: duFort Frankel Von NEUMANN
a7 = ((str7[:20])+(str7[-8:].upper()))
b7 = a7.strip('@$')
print(b7)

str8 = '#duFort4Frankel4Von4Neumann$'
#output: duFort Frankel Von Neumann
a8 = str8.strip('#$')
b8 = a8.replace('4', ' ')
print(b8)

str9 = '@duFort@-^Frankel*-(Von(-(Neumann$'
#output: duFort Frankel Von Neumann
a9 = str9.strip('@$')
b9 = a9.replace('@-^', ' ')
c9= b9.replace('*-(',' ') 
d9= c9.replace('(-',' ') 
e9= d9.replace('(','') 
print (e9) 

str10 = '@DUFort@1^FraNkel*1(VoN(1(NeuMann^'
#output: duFort Frankel Von Neumann
a10 = str10.strip('@^')
b10 = a10.replace('@1^', ' ')
c10= b10.replace('*1(',' ') 
d10= c10.replace('(1(',' ') 
e10= d10.title() 
f10= (e10[0:2].lower())+(e10[2].upper()+(e10[3:]))
print(f10)
