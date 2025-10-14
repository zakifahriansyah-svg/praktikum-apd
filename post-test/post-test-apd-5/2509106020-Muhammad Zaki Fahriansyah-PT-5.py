import os

akun = [["admin", "123", "admin"]]
jadwal = [["admin", []]]
ulang = True

while ulang:
    os.system('cls||clear')
    print("=== JADWAL AKTIVITAS DIGITAL ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        user = input("Masukkan Username: ")
        pw = input("Masukkan Password: ")
        login = False
        role = ""

        for i in range(len(akun)):
            if akun [i][0] == user and akun[i][1] == pw:
                print("Login Berhasil!")
                login = True
                role = akun[i][2]
                break

        if not login:
            print("Login Gagal! Username atau Password Salah!")
            input("Tekan Enter untuk lanjut...")
            continue

        lanjut = True
        while lanjut:
            os.system('cls||clear')
            print (f"\n=== MENU {user.upper()} ===")
            print("1. Lihat Jadwal")
            print("2. Tambah Jadwal")
            print("3. Ubah Kegiatan Jadwal Atau Status")
            print("4. Hapus Jadwal")
            if role == "admin":
                print("5. Lihat Semua Jadwal")
                print("6. Logout")
            else:
                print("5. Logout")
            pilih = input("Pilih menu: ")

            for data in jadwal:
                if data[0] == user:
                    break
            if pilih == "1":
                os.system('cls||clear')
                print("=== JADWAL KAMU ===")
                if len(data[1]) == 0:
                    print("Belum ada jadwal.")
                else:
                    for i in range(len(data[1])):
                        j = data[1][i]
                        print(f"{i+1}. {j[0]} | {j[1]} | {j[2]} | Status: {j[3]}")

            elif pilih == "2":
                kegiatan = input("Nama Kegiatan: ")
                tanggal = input("Tanggal (YYYY/MM/DD): ")
                waktu = input("Waktu (HH:MM): ")
                status = "belum"
                data[1].append([kegiatan, tanggal, waktu, status])
                print("Jadwal berhasil ditambahkan!")

            elif pilih == "3":
                if len(data[1]) == 0:
                    print("Tidak ada jadwal untuk diubah.")
                else:
                    for i in range(len(data[1])):
                        j = data[1][i]
                        print(f"{i+1}. {j[0]} | {j[1]} | {j[2]} | Status: {j[3]}")

                    pilih = input("Pilih nomor jadwal: ")

                    if pilih.isdigit() and 1 <= int(pilih) <= len(data[1]):
                        print("1. Ubah Jadwal")
                        print("2. Ubah Status")
                        ubah = input("Pilih: ")

                        if ubah == "1":
                            kegiatan = input("Masukkan kegiatan baru: ")
                            anggal = input("Masukkan tanggal baru (YYYY/MM/DD): ")
                            waktu = input("Masukkan waktu baru (HH:MM): ")
                            data[1][int(pilih)-1][0] = kegiatan
                            data[1][int(pilih)-1][1] = tanggal
                            data[1][int(pilih)-1][2] = waktu
                            print("Jadwal berhasil diubah!")

                        elif ubah == "2":
                            data[1][int(pilih)-1][3] = "selesai"
                            print("Status berhasil diubah menjadi 'selesai'!")

                        else:
                            print("Pilihan tidak valid.")
                    else:
                        print("Nomor jadwal tidak valid!")


            elif pilih == "4":
                if len(data[1]) == 0:
                    print("Tidak ada jadwal untuk dihapus.")
                else:
                    for i in range(len(data[1])):
                        j = data[1][i]
                        print(f"{i+1}. {j[0]} | {j[1]} | {j[2]} | Status: {j[3]}")
                    hapus = input("Pilih nomor jadwal yang ingin dihapus: ")
                    if hapus.isdigit() and 1 <= int(hapus) <= len(data[1]):
                        del data[1][int(hapus)-1]
                        print("Jadwal berhasil dihapus!")
                    else:
                        print("Nomor tidak valid!")

            elif pilih == "5" and role == "admin":
                print("=== SEMUA JADWAL PENGGUNA ===")
                for data in jadwal:
                    print(f"\nUser: {data[0]}")
                    if len(data[1]) == 0:
                        print("  (Belum ada jadwal)")
                    else:
                        for i in range(len(data[1])):
                            j = data[1][i]
                            print(f"   {i+1}. {j[0]} | {j[1]} | {j[2]} | Status: {j[3]}")

            elif (pilih == "5" and role != "admin") or (pilih == "6" and role == "admin"):
                print("Logout berhasil.")
                lanjut = False

            else:
                print("Pilihan tidak valid!")

            input("\nTekan Enter untuk melanjutkan...")

    elif menu == "2":
        print("=== REGISTER ===")
        user = input("Buat username: ")
        pw = input("Buat password: ")

        duplikat = False
        for data in akun:
            if data[0] == user:
                duplikat = True
                break

        if duplikat:
            print("Username sudah dipakai!")
        else:
            akun.append([user, pw, "user"])
            jadwal.append([user, []])
            print("Akun berhasil dibuat! Silahkan Login Kembali.")
        input("Tekan Enter untuk melanjutkan...")

    elif menu == "3":
        ulang = False
        print("Terima kasih telah menggunakan program!")
    else:
        print("Pilihan tidak ada!")
        input("Enter...")