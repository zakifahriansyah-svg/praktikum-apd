







# def perkalian():
#     x = 5 * 3
#     print(x)

# perkalian()

# def perkenalan(nama):
#     print(f'Halo {nama} Selamat Berbelanja!')
# perkenalan('Yoga')

# def luasPersegiPanjang(panjang, lebar):
#     luas = panjang * lebar
#     print('luas dari persegi panjang adalah ', luas)

# luasPersegiPanjang(5,3)

# def luasPersegi(sisi):
#     luas = sisi*sisi
#     return luas

# def volume_persegi(sisi):
#     volume = luasPersegi(sisi) * sisi
#     print('Volume Persegi = ', volume)

# luasPersegi(4)
# volume_persegi(8)

# def faktorial(n):
# # Basis (Base Case): Kondisi berhenti
#     if n == 1 or n == 0:
#         return 1
# # Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
#     else:
#         return n * faktorial(n - 1)
# # Memanggil fungsi
# hasil = faktorial(7)
# print(f"Hasil dari 7! adalah: {hasil}")

# fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")
#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print ("Salah pilih!")

# # Fungsi untuk menampilkan semua data
# film = []
# def show_data():
#     if len(film) <= 0:
#         print("Belum Ada data")
#     else:
#         print("ID | Judul Film")
#     for indeks in range(len(film)):
#         print(indeks, "|", film[indeks])

# # Fungsi untuk menambah data
# def insert_data():
#     film_baru = input("Judul Film: ")
#     film.append(film_baru)
#     print("Film berhasil ditambahkan!")

# # Fungsi untuk mengedit data
# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")

#     else:
#         judul_baru = input("Judul baru: ")
#         film[indeks] = judul_baru
#         print("Film berhasil diupdate!")

# # Fungsi untuk menghapus data
# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         film.remove(film[indeks])
#         print("Film berhasil dihapus!")

# # fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")

#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     else:
#         print('Tidak ada di menu')


# while True:
#     show_menu()


# try:
#     angka = int(input('masukkan harga\t: '))
# except ValueError:
#     print('Inputan bukan berupa angka')
# else:
#     print(angka)
# finally:
#     print('terima kasih telah berbelanja')

# try:
#     usn = input('Username yang diinginkan : ')
#     if len(usn) < 5:
#         raise ValueError('Nama Minimal Memiliki 5 karakter')
# except ValueError as e:
#     print(e)
# else:
#     print(usn)

try:
    usn = input('Username yang diinginkan : ')
    if len(usn) < 8:
        raise ValueError('Minimal 8 karakter')
    if not usn.isdigit():
        raise ValueError('Username harus berupa angka saja')
except ValueError as e:
    print(e)
else:
    print(usn)
