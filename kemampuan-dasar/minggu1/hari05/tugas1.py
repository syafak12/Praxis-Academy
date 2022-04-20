# Program python untuk diilustrasikan
# pickle.dump()
# import pickle
# import io
 
# class SimpleObject(pickle):
 
#     def __init__(self, pickle):
#         self.pickle = pickle
#         l = list(pickle)
#         l.reverse()
#         self.pickle_backwards = ''.join(l)
#         return
#     def __init__(self, io):
#         self.io = io
#         l = list(io)
#         l.reverse()
#         self.io_backwards = ''.join(l)
#         return


# data = []
# data.append(SimpleObject('pickle'))
# data.append(SimpleObject('cPickle'))
# data.append(SimpleObject('last'))
 
# # Simulasikan file dengan StringIO
# out_s = io.StringIO()
 
# # Write to the stream   ( Tulis ke aliran )
# for o in data:
#     print ('WRITING: %s (%s)' % (o.name, o.name_backwards))
#     pickle.dump(o, out_s)
#     out_s.flush()

# # Program python untuk diilustrasikan
# #Picle.dumps()
# import pickle
 
# data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
# data_string = pickle.dumps(data)
# print ('PICKLE:', data_string )


# import pickle
# import pprint
 
# data1 = [ { 'a':'A', 'b':2, 'c':3.0 } ]
# print ('sebelum:',)
# pprint.pprint(data1)
 
# data1_string = pickle.dumps(data1)
 
# data2 = pickle.loads(data1_string)
# print ('sesudah:',)
# pprint.pprint(data2)
 
# print ('Saya?:', (data1 is data2))
# print ('Kamu?:', (data1 == data2))



import pickle
 
class membacateks:
    """Cetak nomor dan baris dalam file teks."""
  
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename)
        self.lineno = 0
  
    def readline(self):
        self.lineno + 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        return "%i: %s" % (self.lineno, line)
  
    def __getstate__(self):
        state = self.__dict__.copy()
        del state['file']
        return state
  
    def __setstate__(self, state):
        # Pulihkan atribut instance (yaitu, nama file dan lineno).
        self.__dict__.update(state)
        # Kembalikan status file yang dibuka sebelumnya. Untuk melakukannya, kita perlu
        # buka kembali dan baca darinya sampai jumlah baris dipulihkan.
        file = open(self.filename)
        for _ in range(self.lineno):
            file.readline()
        # Terakhir, simpan file.
        self.file = file
   
reader = membacateks("pickle.txt")
print(reader.readline())
print(reader.readline())
new_reader = pickle.loads(pickle.dumps(reader))
print(new_reader.readline())




