print("program menghitung luas lingkaran")
r = int(input("masukkan jari-jari: "))
phi = 22/7
luas_lingkaran = phi*(r**2)
print("Luas lingkaran dengan jari-jari {} cm adalah {} cm\u00b2.".format(r, luas_lingkaran))
#bonus: format luas menjadi 2 angka dibelakang koma
print("Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2.".format(r, luas_lingkaran))