import os
os.system('cls')

username = 'zaki'
password = '020'

ulang_transaksi = 'y'
while ulang_transaksi == 'y':
    print("="*40)
    print('Selamat Datang di Toko Murmer'.center(40))
    print("="*40)

    status = input('Apakah Anda member? (y/n): ')
    login_berhasil = False

    if status == 'y':
        kesempatan = 3
        while kesempatan > 0:
            user = input('Masukkan username: ')
            pw = input('Masukkan password: ')

            if user == '' or pw == '':
                print('Username atau password tidak boleh kosong!\n')
                continue
            if user == username and pw == password:
                print('Login berhasil! Silahkan berbelanja.')
                login_berhasil = True
                break
            else:
                kesempatan -= 1
                print(f'Login gagal, Anda salah memasukkan username password! Sisa percobaan: {kesempatan}\n')
        if not login_berhasil:
            print('Anda gagal login 3 kali, Anda dianggap sebagai non-member.\n')
            status = 'n'
    elif status == 'n':
        print('Silahkan berbelanja sebagai non-member\n')
    else:
        print('Input tidak valid! Anda dianggap non-member.\n')
        status = 'n'
    
    total_belanja = 0
    keranjang = ""
    while True:
        print("="*40)
        print('Menu Belanja'.center(40))
        print("="*40)
        print(f"{'1. Buku tulis':25} - Rp.{18000:>8}")
        print(f"{'2. Pulpen kokoro':25} - Rp.{7500:>8}")
        print(f"{'3. Penghapus':25} - Rp.{2500:>8}")
        print(f"{'4. Penggaris':25} - Rp.{5000:>8}")
        print(f"{'5. Pensil':25} - Rp.{3000:>8}")
        print('-'*40)
        print("6. Checkout\n")

        pilihan = input("Pilih barang (1-5) atau 'checkout': ")
        if pilihan == "1":
            total_belanja += 18000
            keranjang += f"{'Buku tulis':25} Rp{18000:>8,}\n"
            os.system('cls')
            print(f"Buku tulis ditambahkan ke keranjang!")
        elif pilihan == "2":
            total_belanja += 7500
            keranjang += f"{'Pulpen kokoro':25} Rp{7500:>8,}\n"
            os.system('cls')
            print(f"Pulpen kokoro ditambahkan ke keranjang!")
        elif pilihan == "3":
            total_belanja += 2500
            keranjang += f"{'Penghapus':25} Rp{2500:>8,}\n"
            os.system('cls')
            print(f"Penghapus ditambahkan ke keranjang!")
        elif pilihan == "4":
            total_belanja += 5000
            keranjang += f"{'Penggaris':25} Rp{5000:>8,}\n"
            os.system('cls')
            print(f"Penggaris ditambahkan ke keranjang!")
        elif pilihan == "5":
            total_belanja += 3000
            keranjang += f"{'Pensil':25} Rp{3000:>8,}\n"
            os.system('cls')
            print(f"Pensil ditambahkan ke keranjang!")
        elif pilihan == "6":
            if total_belanja == 0:
                print("Keranjang kosong! Silakan belanja dulu.\n")
                continue
            else:
                break
        else:
            print("Pilihan tidak valid!")
            continue
        print(f"Total sementara belanjaan: Rp{total_belanja:,}\n")

    print('\n')
    print('='*40)
    print(f'Struk Belanja Toko Murmer'.center(40))
    print('='*40)
    print(f"{'Nama Barang':25}{'Harga':>10}")
    print('-'*40)
    print(keranjang)
    print('-'*40)
    

    if status == 'y' and login_berhasil == True:
        diskon = 0.15 * total_belanja
        total_bayar = total_belanja - diskon
        print(f"{'Total sebelum diskon':25} Rp {total_belanja:>8,}")
        print(f"{'Potongan diskon (15%)':25} Rp {diskon:>8,}")
    else:
        diskon = 0
        total_bayar = total_belanja

    print(f"{'Total yang harus dibayar':25} Rp {total_bayar:>8}")
    print('='*40)
    print('Terimakasih telah berbelanja!'.center(40))
    print('='*40)

    ulang = input('\nApakah Anda ingin melakukan transaksi lagi? (y/n): ')
    if ulang != 'y':
        print('Program selesai. Terimakasih!'.center(40))
        break
    else:
        os.system('cls')
        ulangi_transaksi = 'y'