#Fungsi Rekursif factorial dengan perulangan
def faktorial(nilai):
 if nilai<=1:
     return 1
 else:
     return nilai*faktorial(nilai-1)
#Program Utama
for i in range(11):
 print('%2d ! = %d' % (i,faktorial(i)))

print('\n')

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input nilai untuk menghasilkan deret 
nilai_input = int(input("Masukkan nilai untuk deret Fibonacci: "))

# Output deret hingga nilai_input
for i in range(nilai_input):
    print(f"fibonacci({i}) = {fibonacci(i)}")