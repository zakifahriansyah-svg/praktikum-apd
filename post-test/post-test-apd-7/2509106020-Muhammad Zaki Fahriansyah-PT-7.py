import os

akun = {
    "admin" : {"password" : "123", "role" : "admin"}
}
jadwal = {
    "admin" : []
}

ulang = True

def menu_login():
    user = input("Masukkan Username: ")
    pw = input("Masukkan Password: ")

    if user in akun and akun[user]["password"] == pw:
        print("Login Berhasil!")
        return user
    else:
        print("Login Gagal! Username atau Password Salah!")
        return None

def menu_register():
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

    if tanya_lanjut():
        menu_register()
    else:
        print("Silakan login kembali.")
        input("Tekan Enter untuk melanjutkan...")

def tambah_jadwal(user, kegiatan, tanggal, waktu):
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
    
    if tanya_lanjut():
        kegiatan = input("Nama Kegiatan: ")
        tanggal = input("Tanggal (YYYY/MM/DD): ")
        waktu = input("Waktu (HH:MM): ")
        tambah_jadwal(user, kegiatan, tanggal, waktu)

def ubah_kegiatan_jadwal(user):
    lihat_jadwal(user)
    try:
        nomor = int(input("Pilih nomor jadwal: "))
        print("1. Ubah Jadwal")
        print("2. Ubah Status")
        ubah = input("Pilih: ")

        if ubah == "1":
            kegiatan = input("Masukkan kegiatan baru: ")
            tanggal = input("Masukkan tanggal baru (YYYY/MM/DD): ")
            waktu = input("Masukkan waktu baru (HH:MM): ")
            jadwal[user][nomor-1].update({
                "kegiatan": kegiatan,
                "tanggal": tanggal,
                "waktu": waktu
            })
            print("Jadwal berhasil diubah!")

        elif ubah == "2":
            ubah_status(jadwal[user], nomor-1)
    except (ValueError, IndexError):
        print("Input tidak valid!")
    if tanya_lanjut():
        ubah_kegiatan_jadwal(user)

def ubah_status(jadwal_user, index):
    try:
        jadwal_user[index]["status"] = "selesai"
        print("Status berhasil diubah menjadi 'selesai'!")
    except IndexError:
        print("Nomor tidak valid!")

def lihat_jadwal(user):
    print("=== JADWAL KAMU ===")
    if len(jadwal[user]) == 0:
        print("Belum ada jadwal.")
    else:
        no = 1
        for j in jadwal[user]:
            print(f"{no}. {j['kegiatan']} | {j['tanggal']} | {j['waktu']} | Status: {j['status']}")
            no += 1

def hapus_jadwal(user):
    lihat_jadwal(user)
    try:
        hapus = int(input("Pilih nomor jadwal yang ingin dihapus: "))
        if 1 <= hapus <= len(jadwal[user]):
            del jadwal[user][hapus-1]
            print("Jadwal berhasil dihapus!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")
    if tanya_lanjut():
        hapus_jadwal(user)

def lihat_semuaJadwal(user):
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

def menu_1_login(user, role):
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
            lihat_jadwal(user)
                
        elif pilih == "2":
            os.system('cls||clear')
            kegiatan = input("Nama Kegiatan: ")
            tanggal = input("Tanggal (YYYY/MM/DD): ")
            waktu = input("Waktu (HH:MM): ")               
            tambah_jadwal(user, kegiatan, tanggal, waktu)

        elif pilih == "3":
            os.system('cls||clear')
            ubah_kegiatan_jadwal(user)

        elif pilih == "4":
            os.system('cls||clear')
            hapus_jadwal(user)

        elif pilih == "5" and role == "admin":
            os.system('cls||clear')
            lihat_semuaJadwal(user)

        elif (pilih == "5" and role != "admin") or (pilih == "6" and role == "admin"):
            print("Logout berhasil.")
            lanjut = False

        else:
            print("Pilihan tidak valid!")
        input("\nTekan Enter untuk melanjutkan...")

def tanya_lanjut():
    pilih = input("\nApakah ingin melakukan lagi? (y/n)? ").lower()
    if pilih == 'y':
        return True
    elif pilih == 'n':
        return False
    else:
        print("Input tidak valid, coba lagi.")
        return tanya_lanjut()

while ulang:
    os.system('cls||clear')
    print("=== JADWAL AKTIVITAS DIGITAL ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        user = menu_login()
        if user is None:
            input("Tekan Enter untuk lanjut...")
            continue

        role = akun[user]["role"]            
        menu_1_login(user, role)

    elif menu == "2":
        menu_register()

    elif menu == "3":
        ulang = False
        print("Terima kasih telah menggunakan program!")
    else:
        print("Pilihan tidak ada!")
        input("Enter...")