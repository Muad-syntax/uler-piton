# def hitung(a, b):
#     hasil = a + b
#     return hasil * 2

# def proses(x):
#     return hitung(x, x + 1) -x

# nilai = proses(3)
# print(nilai)

# nilai = [70, 85, 60, 90]
# jumlah_lulus = 0

# for n in nilai:
#     if n >= 75:
#         jumlah_lulus += 1

# print(jumlah_lulus)


class A:
    def xxx(self):
        return """A"""

class B(A):
    def xxx(self):
        return """B"""

class C(A):
    def xxx(self):
        return """C"""

def proses(obj):
    return obj.xxx()
data = [A(), B(), C()]

for item in data:
    print(proses(item))