from prettytable import PrettyTable

data_balita = {}

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

def tambah_data():
    print("\n~~ Data Balita Posyandu ~~")
    balita = ambil_data_baru()

    if len(data_balita) == 0:
        id_baru = 1
    else:
        id_terbesar = max(data_balita.keys())
        id_baru = id_terbesar + 1

    data_balita[id_baru] = balita
    print("\nData balita berhasil ditambahkan!")

def lihat_data():
    print("\n~~ Daftar Data Balita ~~")
    if len(data_balita) == 0:
        print("Belum ada data balita yang tersimpan.")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama Balita", "Nama Ibu", "Umur (bulan)", "BB (kg)", "TB (cm)"]

        counter_id = 1
        for key, value in data_balita.items():
            table.add_row([
                counter_id,
                value['Nama Balita'],
                value['Nama Ibu'],
                value['Umur'],
                value['BB'],
                value['TB']
            ])
            counter_id += 1
        print(table)

def ubah_data():
    print("\n~~ Ubah Data Balita ~~")
    if len(data_balita) == 0:
        print("Belum ada data balita yang tersimpan.")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama Balita", "Nama Ibu"]

        counter_id = 1
        key_list = list(data_balita.keys())
        for key, value in data_balita.items():
            table.add_row([counter_id, value ['Nama Balita'], value ['Nama Ibu']])
            counter_id += 1
        print(table)

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

def hapus_data():
    print("\n~~ Hapus Data Balita ~~")
    if len(data_balita) == 0:
        print("Belum ada data balita yang tersimpan.")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama Balita", "Nama Ibu"]

        counter_id = 1
        key_list = list(data_balita.keys())
        for key in key_list:
            value = data_balita[key]
            table.add_row([counter_id, value['Nama Balita'], value['Nama Ibu']])
            counter_id += 1
        print(table)

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