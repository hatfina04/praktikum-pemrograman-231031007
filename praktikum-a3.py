nama = 'hatfina rustamin'
nim = '231031007'
meet = 'praktikum 3'
prodi = 'sistem informasi A'
email = 'hatfinafina04@gmail.com'

nama = 'Hatfina Rustamin'
nim = '231031007'
prodi = 'Sistem Informasi A'
ttl = '04-01-2005'
alamat = 'Jl Andi Sinta'
asal = 'Parepare'
hobi = 'Menari'
tinggi = '150'

sp = 40
print ('-'*sp)
print(nama.center(40).upper())
print(nim.center(40))
print('\n'*2)
print(meet.capitalize(). rjust(40))
print(prodi.title(). rjust(40))
print(email.rjust(40))
print('-'*sp)

print(f'''Halo, nama saya {nama.title()} dengan NIM 
      {nim} dari prodi {prodi.title()}, 
      ini adalah file {meet.capitalize()}. Terima kasih.
      ''')


print(f''' Biodata Saya:
Nama\t: {nama.title()}
NIM\t: {nim}
Prodi\t: {prodi.title()}
TTL\t: {ttl}
Alamat\t: {alamat}
Asal\t: {asal}
Hobi\t: {hobi}
Tinggi\t: {tinggi} cm
      ''')
 

stat = 'sir issac newton'
up = stat.upper()
print(up)
up = up.split() #up menjadi list 3 item
print(up)
print(up[2][0], up[0], up[1]) #N SIR ISSAC
#item ke 2 (newton), 0=n

print(up[2], up[0][0], up[1][0]) #NEWTON S I


print()


stat2 = '&sir$ @issac# *newton.'
up2 = stat2.upper()
print(up2)
up2 = stat2.split()
print(up2[0][1:-1], up2[1][1:-1], up2[2][1:-1])
print(up2[0].strip('&$'), up2[1].strip('@#'), up2[2].strip('*.'))
















