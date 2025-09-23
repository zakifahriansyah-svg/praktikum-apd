def main():
    print('-'* 31)
    print("=== Program Cek Berat Badan ===")
    print('-'*31)

    nama   = input('Masukkan Nama Pasien      : ')
    tinggi = float(input('Masukkan Tnggi Badan (cm) : '))
    berat  = float(input('Masukkan Berat Badan (kg) : '))

    berat_ideal  = tinggi - 100
    is_kelebihan = berat > berat_ideal

    status_list = ['Tidak Kelebihan Berat Badan', 'Kelebihan Berat Badan']
    status = status_list[int(is_kelebihan)]

    tinggi_str = f"{int(tinggi)} cm"
    berat_str  = f"{int(berat)} kg"
    ideal_str  = f"{int(berat_ideal)} kg"

    print('\n')

    print('-' * 47)
    print(f'| {'HASIL CEK BERAT BADAN' :^44}|')
    print('-' * 47)
    print(f'| Nama Pasien   : {nama:<28}|')
    print(f'| Tinggi Badan  : {tinggi_str:<28}|')
    print(f'| Berat Badan   : {berat_str:<28}|')
    print(f'| Berat Ideal   : {ideal_str:<28}|')
    print(f'| Status        : {status:<28}|')
    print('-' * 47)
main()

print('\nTerimakasih Telah Menggunakan Program Cek Berat Badan')