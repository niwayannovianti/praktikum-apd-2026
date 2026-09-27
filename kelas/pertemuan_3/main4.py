#if kondisi :
   #if kondisi2:

username = input("masukkan username:").lower().strip()
password = input("masukkan password:").lower().strip()

if username == "novi":
    if password == "062":
        print("login berhasil")
    else:
        print("password salah")
else:
    print("username salah")
