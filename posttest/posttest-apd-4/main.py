nama_benar = "novi"
password_benar = "2609106062"

percobaan = 0
batas_percobaan = 3
login_berhasil = False

print("~~~ Login Program Sosial MBG ~~~")
while percobaan < batas_percobaan:
    username = input("Masukkan Nama (username) Anda:")
    password = input("Masukkan NIM (password) Anda: ")

    if username == nama_benar and password == password_benar:
        print("Login Berhasil! Selamat Datang di Program Sosial MBG")
        login_berhasil = True
        break
    else:
        percobaan += 1
        sisa = batas_percobaan - percobaan
        print(f"Login Gagal! Nama atau Password yang Anda Masukkan Salah (Sisa Percobaan Login: {sisa})\n")

if not login_berhasil:
        print("Batas Login Anda Telah Habis, Program ditutup.")

while login_berhasil:
    print("\n~~~Menu Distribusi Paket~~~")
    print("Opsi 1 -> Paket Reguler, 1 Porsi Makanan")
    print("Opsi 2 -> Paket Anak, 1 Porsi Makanan")
    print("Opsi 3 -> Paket Keluarga, 4 Porsi Makanan")
    print("Opsi 4 -> Keluar dari Program")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    pilihan_menu = input ("Silahkan Masukan Pilihan Menu: ")

    if pilihan_menu == "4":
     print("Anda Telah Keluar Dari Program.")
     break

    if pilihan_menu != "1" and pilihan_menu != "2" and pilihan_menu != "3":
        print("\nOpsi Tidak Valid! Silahkan Masukkan Opsi yang Tersedia")
        continue

    jumlah_paket = int(input("Masukkan Jumlah Paket yang Akan dibagikan: "))

    if pilihan_menu == "1":
        nama_paket = "Paket Reguler"
        porsi = 1
    elif pilihan_menu == "2":
        nama_paket = "Paket Anak"
        porsi = 1
    elif pilihan_menu == "3":
        nama_paket = "Paket Keluarga"
        porsi = 4

    total_porsi = 0
    for i in range(jumlah_paket):
        total_porsi += porsi

    if total_porsi >= 20:
        bonus = "5 paket buah"
    elif total_porsi >= 10:
        bonus = "3 botol susu"
    elif total_porsi >= 5:
        bonus = "1 paket vitamin"
    else:
        bonus = "tidak mendapat bonus"

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Jenis Paket : {nama_paket}")
    print(f"Jumlah Paket : {jumlah_paket} paket")
    print(f"Total Porsi : {total_porsi} porsi")
    print(f"Penerima Manfaat : {jumlah_paket} orang")
    print(f"Bonus : {bonus}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
