print("menghitung luas, keliling lingkaran")
print("masukkan jari-jari lingkaran : ")
r = float(input(""))
def keliling_lingkaran(r):
    phi = 22/7
    return 2*phi*r
def luas_lingkaran(r):
    phi = 22/7
    return phi*(r**2)
keliling = keliling_lingkaran(r)
luas = luas_lingkaran(r)
print("keliling lingkaran dengan jari-jari {} cm, adalah {} cm" .format(r,keliling))
print("luas lingkaran dengan jari-jari {} cm, adalah {} cm" .format(r,luas))
