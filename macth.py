nilai = input(str("Masukan Predikat: "))
match nilai:
    case "A" | "a":
        print(f"Nilai {nilai}: Sangat baik")
    case "B" | "b":
        print(f"Nilai {nilai}: Baik")
    case "C" | "c":
        print(f"Nilai {nilai}: Cukup")
    case "D" | "d":
        print(f"Nilai {nilai}: Kurang")
    case "E" | "e":
        print(f"Nilai {nilai}: Sangat Kurang")
    
    case _:
        print(f"tidak nilai {nilai}")