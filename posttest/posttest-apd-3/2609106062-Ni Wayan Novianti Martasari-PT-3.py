Username = "Novi"
Password = "62"

print ("Masukkan Username & Password anda dengan benar!")

print ("Username:")
if input ("Username: ") == Username:
        print ("Password:")
        if input ("Password: ") == Password:
            print ("Masukkan total point anda!")
            total_point = int(input("Masukkan total point anda!"))

            if total_point < 0:
              print ("EROR: total point yang diinputkan tidak boleh kurang dari 0")
            else : 
             if total_point >= 5000:
                Rank = "Legend"
                total_point -= 5000
                print ("Selamat, anda telah mencapai rank tertinggi")
             elif total_point >= 1000:
                Rank = "Grand Master"
                total_point -= 1000
             elif total_point >=300:
                Rank = "Master"
                total_point -= 300
             elif total_point >= 100:
                Rank = "Warrior"
                total_point -= 100
             else:
                Rank = "Rokie"
          
            print("Rank anda saat ini: " + Rank)
            print("Sisa Point Yang Dibutuhkan untuk naik ke rank selanjutnya: " + str(total_point))

        else:
            print("Login Gagal, Password yang anda masukkan salah!")

else:
    print("Username yang anda masukkan salah!")
