skincare_1 = 35000
skincare_2 = 42000
skincare_3 = 50000
skincare_4 = 55000
skincare_5 = 68000
skincare_6 = 70000
ongkos_kirim = 12000
total_pengeluaran = skincare_1 + skincare_2 + skincare_3 + skincare_4 + skincare_5 + skincare_6 + ongkos_kirim

print (total_pengeluaran)

banyak_data_skincare = 6

kurs_yen = 113

rata_rata = total_pengeluaran/banyak_data_skincare

print (rata_rata)

nim = 62

print (nim)

total_kurs_yen = total_pengeluaran/kurs_yen

print (total_kurs_yen)

bolean = nim < rata_rata
if nim < rata_rata:
    print("iya")
else:
    print("tidak")

