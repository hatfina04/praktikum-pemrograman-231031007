max_attempts = 3
password = "si23a"

for attempt in range(max_attempts):
    user_input = input("Masukkan password: ")

    if user_input == password:
        print("Selamat Anda Login!")
        break
    else:
        remaining_attempts = max_attempts - (attempt + 1)
        print(f"Password salah. Kesempatan anda tersisa: {remaining_attempts} kali")

        if remaining_attempts == 0:
            print("Password Salah! Anda kehabisan kesempatan")
            break
