# import pickle
# class Animal:
#      def __init__(self, number_of_paws, color):
#          self.number_of_paws = number_of_paws
#          self.color = color
# class Sheep(Animal):
#      def __init__(self, color):
#         Animal.__init__(self, 4, color)
# syafak = Sheep("putih")
# print (str.format("domba saya  {0} dan memiliki {1} kuku", syafak.color, syafak.number_of_paws))
# my_pickled_mary = pickle.dumps(syafak)
# print ("Apakah Anda ingin melihatnya? ini dia!")
# print (my_pickled_mary)


# import pickle
# class hewan:
#     def __init__(self, number_of_paws, color):
#         self.number_of_paws = number_of_paws
#         self.color = color

# class sapi(hewan):
#     def __init__(self, color):
#         hewan.__init__(self, 4, color)

# syafak = sapi("putih")

# print (str.format("sapi saya {0} dan memiliki {1} kuku", syafak.color, syafak.number_of_paws))
# my_pickled_syafak = pickle.dumps(syafak)

# binary_file = open('my_pickled_mary.bin', mode='wb')
# my_pickled_mary = pickle.dump(syafak, binary_file)
# binary_file.close()


# import pickle
# class praxis:
#     def __init__(self, number_of_paws, color):
#         self.number_of_paws = number_of_paws
#         self.color = color

# class Sheep(praxis):
#     def __init__(self, color):
#         praxis.__init__(self, 4, color)
# # Langkah 1: Mari kita buat domba Mary
# syafak = Sheep("putih")

# # Langkah 2: Mari kita pickle Mary
# my_pickled_syafak = pickle.dumps(syafak)

# # Langkah 3: Sekarang, mari kita buka acar domba kita Mary membuat contoh lain, domba lain... Dolly!
# doni = pickle.loads(my_pickled_syafak)

# # Dolly dan Mary adalah dua objek yang berbeda, sebenarnya jika kita menentukan warna lain untuk dolly
# # tidak ada turunan untuk Mary
# doni.color = "hitam"

# print (str.format("doni adalah {0} ", doni.color))
# print (str.format("syafak adalah {0} ", syafak.color))


import pickle
class my_zen_class:
    number_of_meditations = 0
    def __init__(self, name):
        self.number_of_meditations = 0
        self.name = name

    def meditate(self):
        self.number_of_meditations = self.number_of_meditations + 1

    def __getstate__(self):
        # metode ini dipanggil saat Anda
        # akan mengasinkan kelas, untuk mengetahui apa yang harus diasinkan

        state = self.__dict__.copy()

       # Anda tidak akan pernah mendapatkan status Buddha jika Anda menghitung
        # meditasi, jadi
        # jangan acar penghitung ini, lain kali Anda akan melakukannya
        # mulailah bermeditasi dari awal :)

        del state['number_of_meditations']

        return state

    def __setstate__(self, state):
        # metode ini dipanggil ketika Anda akan
        # membongkar kelas,
        # jika Anda memerlukan inisialisasi setelah
        # unpickling Anda dapat melakukannya di sini.

        self.__dict__.update(state)

# Saya mulai bermeditasi
my_zen_object = my_zen_class("Dave")
for i in range(100):
    my_zen_object.meditate()

# Sekarang saya acar pengalaman meditasi saya
print(str.format("I'm {0}, and I've meditated {1} times'", my_zen_object.name, my_zen_object.number_of_meditations))
my_pickled_zen_object = pickle.dumps(my_zen_object)
my_zen_object = None

# Sekarang saya mendapatkan kembali pengalaman meditasi saya
my_new_zen_object = pickle.loads(my_pickled_zen_object)

# Seperti yang diharapkan, properti number_of_meditations
#belum direstorasi karena belum diasamkan
print(str.format("I'm {0}, and I don't have a beginner mind yet because I've meditated only {1} times'", my_new_zen_object.name, my_new_zen_object.number_of_meditations))



