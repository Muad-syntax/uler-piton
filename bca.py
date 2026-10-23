'''
    Kelompok 7
    - Muad
    - Afif
    - Aurel
'''
def atm():
    # input user
    username = str(input("Masukan Username: "))
    password = str(input("Masukan Password: "))

    # saldo
    saldo = 2000000
    sisaSaldo = saldo
    
    #validasi user 
    if(username == "Aurel" and password == "admin123"):
        print("Selamat Datang " + str(username) +" BCA BANK akan membantu anda")
        print(f"Saldo Anda saat ini: {saldo}")

        # pengulangan program
        while True:
            print('\n=== Tarik Tunai di BCA ===')
            print('1. Cek Saldo')
            print('2. Tarik Tunai')
            print('3. Transfer')
            print('4. Stor Tunai')
            print('5. Keluar')

            pilihan = input("Pilih Operasi (1/2/3/4/5): ")

            # cek saldo
            if pilihan == '1':
                print('\n=== Cek Saldo ===')
                print(f"Saldo Anda Sekarang: {sisaSaldo}")

            # tarik tunai
            elif pilihan == '2':
                print('\n=== Tarik Tunai ===')
                tarik = int(input("Jumlah yang ingin di tarik: "))
                if tarik > sisaSaldo:
                    print("Saldo anda tidak mencukupi")
                else:
                    sisaSaldo -= tarik
                    print(f"Penarikan {tarik} berhasil. Sisa saldo: {sisaSaldo}")

            # transfer
            elif pilihan == '3':
                print('\n=== Transfer ===')
                rekening = str(input("Masukan No Rekening Tujuan: "))
                transfer = int(input("Masukan Jumlah Transfer: "))
                if transfer > sisaSaldo:
                    print("Saldo anda tidak mencukupi")
                else:
                    sisaSaldo -= transfer
                    print(f"Transfer ke No Rekening {rekening} Berhasil, Sisa saldo: {sisaSaldo}")

            # stor tunai
            elif pilihan == '4':
                print('\n=== Stor Tunai ===')
                stor = int(input("Masukan Tunai: "))
                sisaSaldo += stor
                print(f"Saldo Rp. {stor} masuk, Saldo anda: {sisaSaldo}")

            # keluar
            elif pilihan == '5':
                print("Terima kasih, program selesai")
                break
            else:
                print("Pilihan Tidak Valid")
    else:
        print(f"Username {username} tidak ditemukan/Password Salah!!")

atm()