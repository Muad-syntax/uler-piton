username = str(input("Masukan Username: "))
password = str(input("Masukan Password: "))


if(username == 'Ahmad' and password == '123'):
    saldo = 2000000
    hutang = 500000
    sisaSaldo = saldo
    sisaHutang = hutang
    print("Login Berhasil")
    print(f"Selamat datang {username}")
    while True:
        saldo = sisaSaldo
        hutang = sisaHutang
        print("\n----Transaksi---")
        print(f"saldo anda: {saldo}")
        print("1. Tarik Tunai")
        print("2. Kredit")
        print("3. Prabayar")
        print("4. Keluar")
        transaksi = str(input("Pilih Transaksi:"))
        match transaksi:
            case "1":
                print("\n----Tarik Tunai---")
                print("1. Tarik Saldo")
                print("2. Tarik Semua saldo")
                print("3. Lihat saldo")
                print("4. Isi saldo")
                aksi = str(input("pilih: "))
                match aksi:
                    case "1":
                        tarik = int(input("Masukan jumlah saldo: "))
                        sisaSaldo = saldo - tarik
                        print(f"saldo {tarik} ditarik, sisa saldo anda : {sisaSaldo}")
                    case "2":
                        sisaSaldo = saldo - saldo
                        print(f"saldo {sisaSaldo} ditarik")
                    case "3":
                        print(f"Saldo Anda {saldo}")
                    case "4":
                        isi = int(input("Masukan Nominal"))
                        sisaSaldo = saldo + isi
                        print(f"Saldo Anda Berhasil Ditambahkan, saldo anda sekarang {sisaSaldo}")
                print()

            case "2":
                print("\n----Kredit---")
                print(f"Kredit Anda {hutang}")
                print("1. Kredit")
                print("2. Lihat Kredit")
                aksi = str(input("Pilih: "))
                match aksi:
                    case "1":
                        pinjam = int(input("Masukan Jumlah Kredit: "))
                        sisaHutang = hutang + pinjam
                        print(f"Anda meminjam sebesar {pinjam}")
                        print(f"Kredit Anda: {sisaHutang}")
                    case "2":
                        print(f"Kredit Anda: {sisaHutang}")
                print()
            case "3":
                print("\n----Prabayar---")
                print(f"Hutang Anda: {sisaHutang}")
                print("1. Bayar")
                print("2. Lihat Hutang")
                aksi = str(input("pilih: "))
                match aksi:
                    case "1":
                        bayar = int(input("Bayar Berapa: "))
                        sisaHutang = hutang - bayar
                        print(f"Anda membayar sebesar {bayar}, hutang anda: {sisaHutang}")
                    case "2":
                        print(f"hutang anda: {sisaHutang}")
                print()
            case "4":
                print("Terima Kasih")
                break

else:
    print("404 Not Found")