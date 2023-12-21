# a = True
# while a:
#     print('Menjalankan Program')

#===========PENJELASAN============#
#tidak menggunakan count yang berguna untuk menghitung berapa kali program akan dijalankan sehingga program akan terus berjalan

a = True

counter = 0

while a:
    print('Menjalankan Program')
    counter += 1
    if counter == 5:
        break   #break digunakan untuk menghentikan perulangan


 