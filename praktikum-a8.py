def login():
    max_attempts = 3
    max_pages = 3
    password = ['sistem informasi', 'praktikum', 'si23a']

    for page in range(1, max_pages + 1):
        for attempt in range(1, max_attempts + 1):
            user_input = input(f'Masukkan password Pada Halaman {page}: ')

            if user_input == password[page - 1]:
                print(f'Password Yang Anda Masukkan Benar, Selamat Datang di Halaman {page}')
                break
            else:
                print(f'Password Yang Anda Masukkan salah, Anda Gagal Pada Halaman {page}, Percobaan Anda Sisa-{attempt}')

        else:
            print(f'Sisa Percobaan Anda Telah Habis Pada Halaman {page}. Anda Tidak Berhasil Login.')
            break
    else:
        print("Selamat, Anda Berhasil Login!!")

if __name__ == "__main__":
    login()
