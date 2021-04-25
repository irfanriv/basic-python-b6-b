#dictionary created
pelanggan_dict = {
    "nama" : "Irfan",
    "umur" : 19,
}
#list created
pelanggan_list = [
    "Irfan", "bob"
]
print(pelanggan_dict["nama"])
print(pelanggan_dict["umur"])
#input data kamus
for i in range(2) :
    nama = input("masukkan nama kamu : ")
    umur = input("masukkan umur kamu : ")
    data = {
    "nama" : nama,
    "umur" : umur,
    }   
    pelanggan_list.append(data)
#for i in pelanggan_list :
   # print("nama pelanggan")