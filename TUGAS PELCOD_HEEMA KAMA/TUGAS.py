a = float(input("masukkan nilai 1 :"))
tanda = input("masukkan operasi matematika(+,-,*,/):")
b = float(input("masukkan nilai 2 :"))

if tanda == "+":
    print(f"{a} + {b} =", a + b)
elif tanda == "-":
    print(f"{a} - P{b} =", a - b)
elif tanda == "*":
    print(f"{a} * {b} =", a * b)  
elif tanda == "/":
    print(f"{a} / {b} =", a / b)
else:
    print("input yang anda masukkan salah")
        