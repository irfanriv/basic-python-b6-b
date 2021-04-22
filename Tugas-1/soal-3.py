print("Nilai ujian teori dan praktek mahasiswa")
x = float(input("Nilai ujian teori anda : "))
y = float(input("Nilai ujian praktek anda : "))
if x >= 70 and y >= 70 :
    print("Selamat, anda lulus!")
elif x < 70 and y >= 70 :
    print("Anda harus mengulang ujian teori.")
elif x >= 70 and y <= 70 :
    print("Anda harus mengulang ujian praktek.")
else :
    print("Anda harus mengulang ujian teori dan praktek.")