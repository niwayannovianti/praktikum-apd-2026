import os

data_balita = []

while True:

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print("\n==========================")
    print("   SISTEM POSYANDU BALITA   ")
    print("==========================")
    print("1. Tambah Data Balita")
    print("2. Lihat Data Balita")
    print("3. Ubah Data Balita")
    print("4. Hapus Data Balita")
    print("5. Keluar")
    print("==========================")

    pilihan = input("Pilih Menu (1-5): ")

    if pilihan == "1":
        print("\n~~~ Data Balita Posyandu ~~~")
        nama_balita = input("Masukkan Nama Balita: ")
        nama_ibu = input("Masukkan Nama Ibu: ")
        umur = input("Masukkan Umur Balita (bulan): ")
        bb = input("Masukkan Berat Badan (kg): ")
        tb = input("Masukkan Tinggi Badan (cm): ")

        balita = [nama_balita, nama_ibu, umur, bb, tb]
        data_balita.append(balita)
        print("\nData balita berhasil ditambahkan!")
        ("Tekan Enter untuk Kembali ke Menu...")

    elif pilihan == "2":
        print("\n~~~ Daftar Data Balita ~~~")
        if len(data_balita) == 0:
            print("Belum ada data balita yang tersimpan.")
        else:
            for i in range(len(data_balita)):
                print(f"{i+1}. Anak: {data_balita[i][0]} | Ibu: {data_balita[i][1]} | Umur: {data_balita[i][2]} bulan | BB: {data_balita[i][3]} kg | TB: {data_balita[i][4]} cm")
        print()
        input("Tekan Enter untuk Kembali ke Menu...")

    elif pilihan == "3":
        print("\n~~~ Ubah Data Balita ~~~")
        if len(data_balita) == 0:
            print("Belum ada data balita yang tersimpan.")
            print()
        else:
            for i in range(len(data_balita)):
                print(f"{i+1}.{data_balita[i][0]} (Ibu:{data_balita[i][1]})")

            index_str = input("\nPilih nomor data yang akan diubah: ")
            if index_str.isdigit():
                index = int(index_str) - 1
                if 0 <= index < len(data_balita):
                    nama_balita_baru = input("Masukkan Nama Balita Baru: ")
                    nama_ibu_baru = input("Masukkan Nama Ibu Baru: ")
                    umur_baru = input("Masukkan Umur Baru (bulan): ")
                    bb_baru = input("Masukkan Berat Badan Baru (kg): ")
                    tb_baru = input("Masukkan Tinggi Badan Baru (cm): ")

                    data_balita[index][0] = nama_balita_baru
                    data_balita[index][1] = nama_ibu_baru
                    data_balita[index][2] = umur_baru
                    data_balita[index][3] = bb_baru
                    data_balita[index][4] = tb_baru
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
            print()
        else:
            for i in range(len(data_balita)):
                print(f"{i+1}. {data_balita[i][0]}(Ibu:{data_balita[i][1]})")

            index_str = input("\nPilih nomor data yang akan dihapus: ")
            if index_str.isdigit():
                index = int(index_str) - 1
                if 0 <= index < len(data_balita):
                    data_balita.pop(index)
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