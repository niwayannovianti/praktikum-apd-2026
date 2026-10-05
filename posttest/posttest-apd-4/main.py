nama_benar = "novi"
password_benar = "2609106062"

percobaan = 0
batas_percobaan = 3
login_berhasil = False

print("~~~ Login Program Sosial MBG ~~~")
while True:
    if percobaan < batas_percobaan:
        username = input("Masukkan Nama (username) Anda:").lower()
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
else:
    total_porsi = 0
    penerima_manfaat = 0
    jumlah_reguler = 0
    jumlah_anak = 0
    jumlah_keluarga = 0
    
    while True:
         print("\n~~~Menu Distribusi Paket~~~")
         print("Opsi 1 -> Paket Reguler, 1 Porsi Makanan")
         print("Opsi 2 -> Paket Anak, 1 Porsi Makanan")
         print("Opsi 3 -> Paket Keluarga, 4 Porsi Makanan")
         print("Opsi 4 -> Keluar dari Program")
         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

         pilihan_menu = input ("Silahkan Masukan Pilihan Menu: ")

         if pilihan_menu == "" or not pilihan_menu.isdigit():
            print("\nOpsi Tidak Valid! Silahkan Masukkan Opsi yang Tersedia")
            continue

         pilihan_menu = int(pilihan_menu)

         if pilihan_menu == 4:
            print("Anda Telah Keluar Dari Program.")
            break
         elif pilihan_menu < 1 or pilihan_menu > 4:
            print("\nOpsi Tidak Valid! Silahkan Masukkan Opsi yang Tersedia")
            continue

         while True:
            jumlah_paket = input("Masukkan Jumlah Paket yang Akan dibagikan: ")

            if jumlah_paket == "" or not jumlah_paket.isdigit():
                print("n\Jumlah Paket Tidak Valid. Silahkan Masukkan Jumlah")
                continue

            porsi = int(jumlah_paket)

            if porsi <= 0:
                print("\nJumlah Paket Minimal 1!")
                continue
            break
    
         if pilihan_menu == 3:
             porsi = 4
         else:
             porsi = 1

         for i in range(porsi):
              total_porsi += porsi

         if pilihan_menu == 1:
             penerima_manfaat += porsi * 1
             print(f"\nMenambahkan {jumlah_paket} Paket Reguler")
         elif pilihan_menu == 2:
             penerima_manfaat += porsi * 1
             print(f"\nMenambahkan {jumlah_paket} Paket Anak")
         elif pilihan_menu == 3:
             penerima_manfaat += porsi * 4
             print(f"\nMenambahkan {jumlah_paket} Paket Keluarga")

    if total_porsi >= 20:
        bonus = "5 paket buah"
    elif total_porsi >= 10:
        bonus = "3 botol susu"
    elif total_porsi >= 5:
        bonus = "1 paket vitamin"
    else:
        bonus = "tidak mendapat bonus"

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Paket Reguler : {jumlah_reguler} paket")
    print(f"Paket Anak : {jumlah_anak} paket")
    print(f"Paket Keluarga : {jumlah_keluarga} paket")
    print(f"Total Porsi : {total_porsi} porsi")
    print(f"Penerima Manfaat : {penerima_manfaat} orang")
    print(f"Bonus : {bonus}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Makanan Dibagikan Secara Gratis Sehingga Tidak Ada Harga dan Pembayaran") 