import os

username_benar = "kader"
password_benar = "posyandu19"
maksimal_login = 3
terotentikasi = False

while maksimal_login > 0:
    username = input("Masukkan Username: ")
    if username != username_benar:
        maksimal_login -= 1
        print("Login gagal! Username yang anda masukkan SALAH!")
        if maksimal_login > 0:
            print(f"Sisa percobaan login: {maksimal_login} kali lagi.\n")
        else:
            print("Anda telah salah memasukkan password sebanyak 3 kali.")
            print("Akses ditolak. Program berhenti.")
        continue

    password = input("Masukkan Password: ")
    if password == password_benar:
        print("\nLogin berhasil! Masuk ke sistem...")
        input("Tekan Enter untuk Lanjut ke Sistem...")
        terotentikasi = True
        break
    else:
        maksimal_login -= 1
        print(f"Login gagal! Password SALAH!")
        if maksimal_login > 0:
            print(f"Sisa percobaan login: {maksimal_login} kali lagi.\n")
        else:
            print("Anda telah salah memasukkan password sebanyak 3 kali.")
            print("Akses ditolak. Program berhenti.")

if terotentikasi:
    data_balita = {}
    counter_id = 1

    while True:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        print("\n===========================")
        print("   SISTEM POSYANDU BALITA   ")
        print("===========================")
        print("1. Tambah Data Balita")
        print("2. Lihat Data Balita")
        print("3. Ubah Data Balita")
        print("4. Hapus Data Balita")
        print("5. Keluar")
        print("===========================")

        pilihan = input("Pilih Menu (1-5): ")

        if pilihan == "1":
            print("\n~~~ Data Balita Posyandu ~~~")
            nama_balita = input("Masukkan Nama Balita: ")
            nama_ibu = input("Masukkan Nama Ibu: ")
            umur = input("Masukkan Umur Balita (bulan): ")
            bb = input("Masukkan Berat Badan (kg): ")
            tb = input("Masukkan Tinggi Badan (cm): ")

            balita = {
                "Nama Balita": nama_balita,
                "Nama Ibu": nama_ibu,
                "Umur": umur,
                "BB": bb,
                "TB": tb
            }

            if len(data_balita) == 0:
                id_baru = 1
            else:
                id_terbesar = 0
                for key in data_balita.keys():
                    if key > id_terbesar:
                        id_terbesar = key
                id_baru = id_terbesar + 1

            data_balita[id_baru] = balita

            print("\nData balita berhasil ditambahkan!")
            input("Tekan Enter untuk Kembali ke Menu...")

        elif pilihan == "2":
            print("\n~~~ Daftar Data Balita ~~~")
            if len(data_balita) == 0:
                print("Belum ada data balita yang tersimpan.")
            else:
                counter_id = 1
                for key, value in data_balita.items():
                    print(f"{counter_id}. Anak: {value["Nama Balita"]} | Ibu: {value["Nama Ibu"]} | Umur: {value["Umur"]} bulan | BB: {value["BB"]} kg | TB: {value["TB"]} cm")
                    counter_id += 1
                print()
                input("Tekan Enter untuk Kembali ke Menu...")

        elif pilihan == "3":
            print("\n~~~ Ubah Data Balita ~~~")
            if len(data_balita) == 0:
                print("Belum ada data balita yang tersimpan.")
            else:
                counter_id = 1
                for key, value in data_balita.items():
                    print(f"{counter_id}. Anak: {value["Nama Balita"]} | Ibu: {value["Nama Ibu"]}")
                    counter_id += 1
                print()
                index_str = input("\nPilih nomor data yang akan diubah: ")
                if index_str.isdigit():
                    index = int(index_str) - 1
                    key_list = list(data_balita.keys())

                    if 0 <= index < len(key_list):

                        target_key = key_list[index]

                        nama_balita_baru = input("Masukkan Nama Balita Baru: ")
                        nama_ibu_baru = input("Masukkan Nama Ibu Baru: ")
                        umur_baru = input("Masukkan Umur Baru (bulan): ")
                        bb_baru = input("Masukkan Berat Badan Baru (kg): ")
                        tb_baru = input("Masukkan Tinggi Badan Baru (cm): ")

                        data_balita[target_key] = {
                            "Nama Balita": nama_balita_baru,
                            "Nama Ibu": nama_ibu_baru,
                            "Umur": umur_baru,
                            "BB": bb_baru,
                            "TB": tb_baru
                         }
                        print("\nData balita berhasil diubah!")
                    else:
                        print("\nNomor data tidak valid!")
                else:
                    print("/nInput harus berupa angka!")
            print()
            input("Tekan Enter untuk Kembali ke Menu...")

        elif pilihan == "4":
            print("\n~~~ Hapus Data Balita ~~~")
            if len(data_balita) == 0:
                print("Belum ada data balita yang tersimpan.")
            else:
                counter_id = 1
                key_list = list(data_balita.keys())

                for key in key_list:
                    value = data_balita[key]
                    print(f"{counter_id}. Anak: {value["Nama Balita"]} | Ibu: {value["Nama Ibu"]}")
                    counter_id += 1

                index_str = input("\nPilih nomor data yang akan dihapus: ")
                if index_str.isdigit():
                    index = int(index_str)

                    if 1 <= index <= len(key_list):
                        key_yang_dihapus = key_list[index-1]
                        data_balita.pop(key_yang_dihapus)
                        print("\nData balita berhasil dihapus!")
                    else:
                        print("\nNomor data tidak valid.")
                else:
                    print("/nInput harus berupa angka!")
            print()
            input("Tekan Enter untuk Kembali ke Menu...")

        elif pilihan == "5":
            print("\nTerimakasih Telah Menggunakan Sistem Posyandu.")
            break

        else:
            print("\nPilihan tidak valid. Silahkan masukkan angka 1-5.")
            print()
            input("Tekan Enter untuk Kembali ke Menu...")   