import os

akun = {
    "admin" : {"password" : "123", "role" : "admin"}
}
jadwal = {
    "admin" : []
}
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

        if user in akun and akun[user]["password"] == pw:
            print("Login Berhasil!")
            role = akun[user]["role"]
            input("Tekan Enter untuk lanjut...")

        else:
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

            if user not in jadwal:
                jadwal[user] = []
            if pilih == "1":
                os.system('cls||clear')
                print("=== JADWAL KAMU ===")
                if len(jadwal[user]) == 0:
                    print("Belum ada jadwal.")
                else:
                    no = 1
                    for j in jadwal[user]:
                        print(f"{no}. {j['kegiatan']} | {j['tanggal']} | {j['waktu']} | Status: {j['status']}")
                        no += 1

            elif pilih == "2":
                kegiatan = input("Nama Kegiatan: ")
                tanggal = input("Tanggal (YYYY/MM/DD): ")
                waktu = input("Waktu (HH:MM): ")

                if kegiatan == "" or tanggal == "" or waktu == "":
                    print("Data tidak boleh kosong!")
                else:
                    jadwal[user].append({
                        "kegiatan": kegiatan,
                        "tanggal": tanggal,
                        "waktu": waktu,
                        "status": "belum"
                    })
                    print("Jadwal berhasil ditambahkan!")

            elif pilih == "3":
                if len(jadwal[user]) == 0:
                    print("Tidak ada jadwal untuk diubah.")
                else:
                    no = 1
                    for j in jadwal[user]:
                        print(f"{no}. {j['kegiatan']} | {j['tanggal']} | {j['waktu']} | Status: {j['status']}")
                        no += 1

                    pilih = input("Pilih nomor jadwal: ")

                    if pilih.isdigit() and 1 <= int(pilih) <= len(jadwal[user]):
                        print("1. Ubah Jadwal")
                        print("2. Ubah Status")
                        ubah = input("Pilih: ")

                        if ubah == "1":
                            kegiatan = input("Masukkan kegiatan baru: ")
                            tanggal = input("Masukkan tanggal baru (YYYY/MM/DD): ")
                            waktu = input("Masukkan waktu baru (HH:MM): ")
                            jadwal[user][int(pilih)-1]['kegiatan'] = kegiatan
                            jadwal[user][int(pilih)-1]['tanggal'] = tanggal
                            jadwal[user][int(pilih)-1]['waktu'] = waktu
                            print("Jadwal berhasil diubah!")

                        elif ubah == "2":
                            jadwal[user][int(pilih)-1]['status'] = "selesai"
                            print("Status berhasil diubah menjadi 'selesai'!")

                        else:
                            print("Pilihan tidak valid.")
                    else:
                        print("Nomor jadwal tidak valid!")


            elif pilih == "4":
                if len(jadwal[user]) == 0:
                    print("Tidak ada jadwal untuk dihapus.")
                else:
                    no = 1
                    for j in jadwal[user]:
                        print(f"{no}. {j['kegiatan']} | {j['tanggal']} | {j['waktu']} | Status: {j['status']}")
                        no += 1
                    hapus = input("Pilih nomor jadwal yang ingin dihapus: ")
                    if hapus.isdigit() and 1 <= int(hapus) <= len(jadwal[user]):
                        del jadwal[user][int(hapus)-1]
                        print("Jadwal berhasil dihapus!")
                    else:
                        print("Nomor tidak valid!")

            elif pilih == "5" and role == "admin":
                print("=== SEMUA JADWAL PENGGUNA ===")
                for username, data in jadwal.items():
                    print(f"\nUser: {username}")
                    if not data:
                        print("  (Belum ada jadwal)")
                    else:
                        no = 1
                        for j in data:
                            print(f"{no}. {j['kegiatan']} | {j['tanggal']} | {j['waktu']} | Status: {j['status']}")
                            no += 1

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

        if user == '' or pw == '':
            print("Username dan Password tidak boleh kosong!")
        elif user in akun:
            print("Username sudah dipakai!")
        else:
            akun[user] = {"password": pw, "role": "user"}
            jadwal[user] = []
            print("Akun berhasil dibuat! Silahkan Login Kembali.")
        input("Tekan Enter untuk melanjutkan...")

    elif menu == "3":
        ulang = False
        print("Terima kasih telah menggunakan program!")
    else:
        print("Pilihan tidak ada!")
        input("Enter...")