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