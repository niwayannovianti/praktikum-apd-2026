from auth import cek_login
from utils import bersihkan_layar, tampilkan_menu_utama, input_pilihan_menu, validasi_angka_menu
from posyandu import tambah_data, lihat_data, ubah_data, hapus_data

def main ():
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
                    tambah_data()
                    input("Tekan Enter untuk Kembali ke Menu...")
                elif pilihan_int == 2:
                    lihat_data()
                    input("Tekan Enter untuk Kembali ke Menu...")
                elif pilihan_int == 3:
                    ubah_data()
                    input("Tekan Enter untuk Kembali ke Menu...")
                elif pilihan_int == 4:
                    hapus_data()
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

if __name__ == "__main__":
    main()