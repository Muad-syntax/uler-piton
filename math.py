from operasi import tambah,kurang,kali,bagi

while True:
    print("\n--- APLIKASI MATEMATIKA ---")
    print("--- pilih Operasi ---")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Exit")

    pilihan = input("Masukan Pilihan Operasi: ")

    if pilihan == '5':
        print("Program Selesai! ")
        break

    if pilihan in ['1', '2', '3', '4']:
        angka1 = int(input("Masukan nilai 1: "))
        angka2 = int(input("Masukan nilai 2: "))


        match pilihan:
            case '1':
                tambah(angka1, angka2)
            case '2':
                kurang(angka1, angka2)
            case '3':
                kali(angka1, angka2)
            case '4':
                bagi(angka1, angka2)
      
    else:
        print("Pilihan tidak tersedia")