# class sapi:
# # class atribut
#     species = 'hewan'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# # objeknya sapi
# syafak = sapi("syafak", 5)
# syafik = sapi("syafik", 6)
# # Access instansi atribut
# print("{} is {} and {} is {}.".format(
#     syafak.name, syafak.age, syafik.name, syafik.age))
# # apakah syafak hewan?
# if syafak.species == "hewan":
#     print("{0} is a {1}!".format(syafak.name, syafak.species))



# class kelas_saya:
#     variable = " saya datang kesini dengan sungguh-sungguh"
#     def function(self):
#         print("ini merupakan kata kata saya")
# myobjectx = kelas_saya()
# print(myobjectx.variable)


# class Siswa:
#   def __init__(self, nama, umur, alamat):
#       self.nama = nama
#       self.umur = umur
#       self.alamat = alamat
# p1 = Siswa('Syafak','12','Rembang')
# #Untuk Mengakses class diatas caranya sebagai berikut:
# print(p1.nama)
# print(p1.umur)
# print(p1.alamat)

# # Semua kelas biasanya memiliki fungsi yang disebut dengan __init__(), dimana fungsi ini akan secara otomatis menjalankan perintah ketika Class dijalankan. Untuk lebih jelas kita langsung saja ke contoh syntaxnya.

# class Siswa:
#   def __init__(self, nama, umur, alamat):
#       self.nama = nama
#       self.umur = umur
#       self.alamat = alamat
# p1 = Siswa('Nispul','12','Lombok Timur')
# #Untuk Mengakses class diatas caranya sebagai berikut:
# print(p1.nama)
# print(p1.umur)
# print(p1.alamat)


# # Menggunakan 2 Function (Method) dalam satu kelas Pada Python dengan cara sebagai berikut :
# class praxis:
#   def __init__(self, nama, umur, alamat):
#       self.nama = nama
#       self.umur = umur
#       self.alamat = alamat
#   def m2(abc):
#     print("Assalamualaikum, Perkenalkan saya :" + abc.nama 
#     + ' Umur :' + abc.umur
#     + ' Alamat :'+ abc.alamat )
# p1 = praxis('Syafak','12','rembang kota')
# p1.m2()

