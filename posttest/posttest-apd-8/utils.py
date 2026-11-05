import os

def bersihkan_layar():
    sistem_operasi = os.name
    if sistem_operasi == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def tampilkan_menu_utama():
    print("\n============================")
    print("   SISTEM POSYANDU BALITA   ")
    print("===========================")
    print("1. Tambah Data Balita")
    print("2. Lihat Data Balita")
    print("3. Ubah Data Balita")
    print("4. Hapus Data Balita")
    print("5. Keluar")
    print("===========================")

def input_pilihan_menu():
    return input("Pilih Menu (1-5): ")

def validasi_angka_menu(teks_pilihan):
    if teks_pilihan.isdigit():
        angka = int(teks_pilihan)
        if 1 <= angka <= 5:
            return True
    return False