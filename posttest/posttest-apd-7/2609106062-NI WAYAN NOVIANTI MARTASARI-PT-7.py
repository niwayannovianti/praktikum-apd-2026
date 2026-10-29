import os

username_benar = "kader"
password_benar = "posyandu19"
data_balita = {}

def bersihkan_layar():
    sistem_operasi = os.name
    if sistem_operasi == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def tampilkan_menu_utama():
    print("\n===========================")
    print("   SISTEM POSYANDU BALITA   ")
    print("===========================")
    print("1. Tambah Data Balita")
    print("2. Lihat Data Balita")
    print("3. Ubah Data Balita")
    print("4. Hapus Data Balita")
    print("5. Keluar")
    print("===========================")

def input_pilihan_menu():
    pilihan_str = input("Pilih Menu (1-5): ")
    return pilihan_str

def ambil_data_baru():
    nama_balita = input("Masukkan Nama Balita: ")
    nama_ibu = input("Masukkan Nama Ibu: ")
    umur = input("Masukkan Umur Balita (bulan): ")
    bb = input("Masukkan Berat Badan (kg): ")
    tb = input("Masukkan Tinggi Badan (cm): ")

    return {
        "Nama Balita": nama_balita,
        "Nama Ibu": nama_ibu,
        "Umur": umur,
        "BB": bb,
        "TB": tb
    }

def validasi_angka_menu(teks_pilihan):
    status_valid = False
    if teks_pilihan.isdigit():
        angka = int(teks_pilihan)
        if 1 <= angka <= 5:
            status_valid = True
    return status_valid

def cek_login(username_input, password_input):
    berhasil = False
    if username_input == username_benar and password_input == password_benar:
        berhasil = True
    return berhasil

maksimal_login = 3
terotentikasi = False

while maksimal_login > 0:
    try:
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        if cek_login(username, password):
            print("\nLogin berhasil! Masuk ke sistem...")
            input("Tekan Enter untuk Lanjut ke Sistem...")
            terotentikasi = True
            break
        else:
            maksimal_login -= 1
            print(f"Login gagal! Username atau Password SALAH!")
            if maksimal_login > 0:
                print(f"Sisa percobaan login: {maksimal_login} kali lagi.\n")
            else:
                print("Anda telah salah memasukkan data sebanyak 3 kali.")
                print("Akses ditolak. Program berhenti.")
    except Exception as e:
        print(f"Terjadi kesalahan saat proses login: {e}")

if terotentikasi:
    while True:
        try:
            bersihkan_layar()
            tampilkan_menu_utama()

            pilihan = input_pilihan_menu()
            if not validasi_angka_menu(pilihan):
                print("\nPilihan tidak valid. Silahkan masukkan angka 1-5.")
                input("Tekan Enter untuk Kembali ke Menu...")
                continue

            pilihan_int = int(pilihan)

            if pilihan_int == 1:
                print("\n~~ Data Balita Posyandu ~~")
                balita = ambil_data_baru()

                if len(data_balita) == 0:
                    id_baru = 1
                else:
                    id_terbesar = max(data_balita.keys())
                    id_baru = id_terbesar + 1

                data_balita[id_baru] = balita

                print("\nData balita berhasil ditambahkan!")
                input("Tekan Enter untuk Kembali ke Menu...")

            elif pilihan_int == 2:
                print("\n~~ Daftar Data Balita ~~")
                if len(data_balita) == 0:
                    print("Belum ada data balita yang tersimpan.")
                else:
                    counter_id = 1
                    for key, value in data_balita.items():
                        print(f"{counter_id}. Anak: {value['Nama Balita']} | Ibu: {value['Nama Ibu']} | Umur: {value['Umur']} bulan | BB: {value['BB']} kg | TB: {value['TB']} cm")
                        counter_id += 1
                print()
                input("Tekan Enter untuk Kembali ke Menu...")

            elif pilihan_int == 3:
                print("\n~~ Ubah Data Balita ~~")
                if len(data_balita) == 0:
                    print("Belum ada data balita yang tersimpan.")
                else:
                    counter_id = 1
                    key_list = list(data_balita.keys())
                    for key, value in data_balita.items():
                        print(f"{counter_id}. Anak: {value['Nama Balita']} | Ibu: {value['Nama Ibu']}")
                        counter_id += 1
                    
                    index_str = input("\nPilih nomor data yang akan diubah: ")
                    if index_str.isdigit():
                        index = int(index_str) - 1
                        if 0 <= index < len(key_list):
                            target_key = key_list[index]
                            print("Masukkan data baru:")
                            data_baru = ambil_data_baru()
                            data_balita[target_key] = data_baru
                            print("\nData balita berhasil diubah!")
                        else:
                            print("\nNomor data tidak valid!")
                    else:
                        print("\nInput harus berupa angka!")
                print()
                input("Tekan Enter untuk Kembali ke Menu...")

            elif pilihan_int == 4:
                print("\n~~ Hapus Data Balita ~~")
                if len(data_balita) == 0:
                    print("Belum ada data balita yang tersimpan.")
                else:
                    counter_id = 1
                    key_list = list(data_balita.keys())
                    for key in key_list:
                        value = data_balita[key]
                        print(f"{counter_id}. Anak: {value['Nama Balita']} | Ibu: {value['Nama Ibu']}")
                        counter_id += 1

                    index_str = input("\nPilih nomor data yang akan dihapus: ")
                    if index_str.isdigit():
                        index = int(index_str) - 1
                        if 0 <= index < len(key_list):
                            key_yang_dihapus = key_list[index]
                            data_balita.pop(key_yang_dihapus)
                            print("\nData balita berhasil dihapus!")
                        else:
                            print("\nNomor data tidak valid.")
                    else:
                        print("\nInput harus berupa angka!")
                print()
                input("Tekan Enter untuk Kembali ke Menu...")

            elif pilihan_int == 5:
                print("\nTerimakasih Telah Menggunakan Sistem Posyandu.")
                break

        except ValueError as ve:
            print(f"\nKesalahan format angka: {ve}")
            input("Tekan Enter untuk Lanjutkan...")
        except Exception as e:
            print(f"\nTerjadi kesalahan tak terduga: {e}")
            input("Tekan Enter untuk Lanjutkan...")