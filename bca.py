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
        print("Saldo Anda saat ini: ", saldo)

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
                if tarik < 0:
                    print("Masukan nilai lebih dari 0")
                elif tarik > sisaSaldo:
                    print("Saldo anda tidak mencukupi")
                else:
                    sisaSaldo -= tarik
                    print(f"Penarikan {tarik} berhasil. Sisa saldo: {sisaSaldo}")

            # transfer
            elif pilihan == '3':
                print('\n=== Transfer ===')
                print("1. BCA")
                print("2. DANA")
                print("3. OVO")
                print("4. GOPAY")
                pilihan = input("Tranfer Ke (1-4): ")

                if pilihan == '1':
                    rekening = str(input("Masukan No Rekening: "))
                    transfer = int(input("Masukan Jumlah Transfer: "))    
                    if transfer < 0:
                        print("Masukan nilai lebih dari 0")
                    elif transfer > sisaSaldo:
                        print("Saldo anda tidak mencukupi")
                    else:
                        sisaSaldo -= transfer
                        print(f"Transfer ke No Rekening {rekening} Berhasil, Sisa saldo: {sisaSaldo}")
                elif pilihan == '2':
                    rekening = str(input("Masukan No DANA: "))
                    transfer = int(input("Masukan Jumlah Transfer: ")) 
                    if transfer < 0:
                        print("Masukan nilai lebih dari 0")
                    elif transfer > sisaSaldo:
                        print("Saldo anda tidak mencukupi")
                    else:
                        sisaSaldo -= transfer
                        print(f"Transfer ke No Rekening {rekening} Berhasil, Sisa saldo: {sisaSaldo}")
                elif pilihan == '3':
                    rekening = str(input("Masukan No OVO: "))
                    transfer = int(input("Masukan Jumlah Transfer: ")) 
                    if transfer < 0:
                        print("Masukan nilai lebih dari 0")
                    elif transfer > sisaSaldo:
                        print("Saldo anda tidak mencukupi")
                    else:
                        sisaSaldo -= transfer
                        print(f"Transfer ke No Rekening {rekening} Berhasil, Sisa saldo: {sisaSaldo}")
                elif pilihan == '4':
                    rekening = str(input("Masukan No GOPAY: "))
                    transfer = int(input("Masukan Jumlah Transfer: ")) 
                    if transfer < 0:
                        print("Masukan nilai lebih dari 0")
                    elif transfer > sisaSaldo:
                        print("Saldo anda tidak mencukupi")
                    else:
                        sisaSaldo -= transfer
                        print(f"Transfer ke No Rekening {rekening} Berhasil, Sisa saldo: {sisaSaldo}")
                else:
                    print('Pilihan tidak ditemukan')

            # stor tunai
            elif pilihan == '4':
                print('\n=== Stor Tunai ===')
                stor = int(input("Masukan Tunai: "))
                if stor < 0:
                    print("Masukan tunai lebih dari 0")
                else:
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