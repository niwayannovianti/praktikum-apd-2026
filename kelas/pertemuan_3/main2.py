kendaraan = input("masukkan jenis kendaraan:").lower().strip()

if kendaraan == "mobil":
    tarif_parkir = 10_000 #10000
elif kendaraan == "motor":
    tarif_parkir = 5_000 
elif kendaraan == "sepeda":
    tarif_parkir = 6_7000
else:
    tarif_parkir = 15_000

print("tarif parkir yang harus dibayar:", tarif_parkir)