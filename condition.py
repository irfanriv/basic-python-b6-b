x = int(input("masukkan x:"))
y = int(input("masukkan y:"))

if x > y:
    print("x itu lebih besar dari y")
elif x < y:
    print("x itu kurang dari y")
elif x == y:
    print("x sama dengan y")
else:
    print("salah input")

tanya = input("mau makan gaa?? ")
if tanya == "boleh":
    print("yaudah siapsiap ya")
elif tanya == "ngga dulu":
    print("ohh yaudah :(")
else:
    print("jawabnya 'boleh' atau 'ngga dulu'")