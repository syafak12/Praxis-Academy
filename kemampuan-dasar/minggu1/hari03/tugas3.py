# import reprlib
# print(reprlib.repr(set('supercalifragilisticexpialidocious')))

# import pprint
# t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
# print(pprint.pprint(t, width=30))

# import textwrap
# doc = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate
# the wrapped lines."""
# print(textwrap.fill(doc, width=40))

# import locale
# locale.setlocale(locale.LC_ALL, 'English_United States.1252')

# conv = locale.localeconv()          # get a mapping of conventions
# x = 1234567.8
# locale.format("%d", x, grouping=True)
# locale.format_string("%s%.*f", (conv['currency_symbol'],
#                      conv['frac_digits'], x), grouping=True)


# from string import Template
# t = Template('${village}folk send $$10 to $cause.')
# print(t.substitute(village='Nottingham', cause='the ditch fund'))


# t = Template('Return the $item to $owner.')
# d = dict(item='unladen swallow')
# t.substitute(d)
# print(t.safe_substitute(d))

import time, os.path
photofiles = ['img_1074.jpg', 'fotoku2.jpeg', 'fotoku3.jpeg']
class BatchRename(Template):
    delimiter = '%'
fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

# import struct

# with open('myfile.zip', 'rb') as f:
#     data = f.read()

# start = 0
# for i in range(3):                      # show the first 3 file headers
#     start += 14
#     fields = struct.unpack('<IIIHH', data[start:start+16])
#     crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

#     start += 16
#     filename = data[start:start+filenamesize]
#     start += filenamesize
#     extra = data[start:start+extra_size]
#     print(filename, hex(crc32), comp_size, uncomp_size)

# import threading, zipfile

# class AsyncZip(threading.Thread):
#     def __init__(self, infile, outfile):
#         threading.Thread.__init__(self)
#         self.infile = infile
#         self.outfile = outfile

#     def run(self):
#         f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
#         f.write(self.infile)
#         f.close()
#         print('Finished background zip of:', self.infile)

# background = AsyncZip('mydata.txt', 'myarchive.zip')
# background.start()
# print('The main program continues to run in foreground.')

# background.join()    # Wait for the background task to finish
# print('Main program waited until background was done.')

# import logging
# logging.debug('Debugging information')
# logging.info('Informational message')
# logging.warning('Warning:config file %s not found', 'server.conf')
# logging.error('Error occurred')
# logging.critical('Critical error -- shutting down')


# from array import array
# a = array('H', [4000, 10, 700, 22222])
# print(sum(a))
# print(a[1:3])


# dari koleksi impor deque
# from collections import deque
# d = deque(["tugas1", "tugas2", "tugas3"])
# d.append("task4")
# print("wajib", d.popleft())


# unsearched = deque([starting_node])
# def breadth_first_search(unsearched):
#     node = unsearched.popleft()
#     for m in gen_moves(node):
#         if is_goal(m):
#             print(return m)


# import bisect
# scores = [(100, 'syafak'), (200, 'doni'), (400, 'adi'), (500, 'dea')]
# bisect.insort(scores, (300, 'musyaffak'))
# print(scores)

# from heapq import heapify, heappop, heappush
# data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# print(heapify(data))     # atur ulang daftar menjadi urutan tumpukan
# print(heappush(data, -5))    # tambahkan entry baru
# print([heappop(data) for i in range(3)])    # ambil 3 entry terkecil

# from decimal import *
# print(round(Decimal('0.70') * Decimal('1.05'), 2))
# print(round(.70 * 1.05, 2))

# print(Decimal('1.00') % Decimal('.10'))
# print(1.00 % 0.10)
# print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
# print(sum([0.1]*10) == 1.0)

# getcontext().prec = 36
# print(Decimal(1) / Decimal(7))










