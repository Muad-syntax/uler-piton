def kalkulator():
    while True:
        print('\n=== Program Kalkulator Sederhana ===')
        print('1. Penjumlahan (+)')
        print('2. Pengurangan (-)')
        print('3. Perkalian (x)')
        print('4. Pembagian (/)')
        print('5. Keluar')

        pilihan = input("Pilih Operasi (1/2/3/4/5): ")

        if pilihan == '5':
            print("Terima kasih, program selesai")
            break

        if pilihan in ('1', '2', '3', '4'):
            try:
                angka1 = int(input("Masukan angka pertama: "))
                angka2 = int(input("Masukan angka kedua: "))
            except ValueError:
                print('Error: Harap masukan angka yang valid!')
                continue

            if pilihan == '1':
                hasil = angka1 + angka2
                print(f"Hasil: {angka1} + {angka2} = {hasil}")
            elif pilihan == '2':
                hasil = angka1 - angka2
                print(f"Hasil: {angka1} - {angka2} = {hasil}")
            elif pilihan == '3':
                hasil = angka1 * angka2
                print(f"Hasil: {angka1} x {angka2} = {hasil}")
            elif pilihan == '4':
                if angka2 != 0:
                   hasil = angka1 / angka2
                   print(f"Hasil: {angka1} / {angka2} = {hasil}")
                else:
                    print("Error: Tidak bisa melakukan pembagian dengan nol!")
            else:
                print("Pilihan tidak valid, silahkan cobalagi!")

kalkulator()