def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print(f"Hasil dari {angka1} + {angka2} = {hasil}")

def kurang(angka1, angka2):
    hasil = angka1 - angka2
    print(f"Hasil dari {angka1} - {angka2} = {hasil}")

def kali(angka1, angka2):
    hasil = angka1 * angka2
    print(f"Hasil dari {angka1} x {angka2} = {hasil}")

def bagi(angka1, angka2):
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil dari {angka1} / {angka2} = {hasil}")
    else:
        print("Tidak bisa dibagikan dengan nol!")

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