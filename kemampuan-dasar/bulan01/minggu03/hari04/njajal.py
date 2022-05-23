import pymongo 

Client = pymongo.MongoClient("Turusgede")
print(Client.list_database_names())

mydb = Client["mydb"]
mycol = mydb["Turuswetan"]

data = {'nama': 'syafak', 'usia': 22}
mycol.insert_one(data)
datalist = [{'nama': 'adi', 'usia': 25}, {'nama': 'uud', 'usia': 30}]
mycol.insert_many(datalist)

# melakukan looping dari database
mydb=Client["Turusgede"]
mycol = mydb['DtlCont']
for x in mycol.find({"jumlah anak":{"$gte": "3"}}):
  print(x)


mydb = Client["Turusgede"]
mycol = mydb['DtlCont']
for x in mycol.find():
  print(x)


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
