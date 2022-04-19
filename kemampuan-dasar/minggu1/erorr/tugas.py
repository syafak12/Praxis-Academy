# import os
# print(os.getcwd())
# print(('/document/praxis-academy'))
# print(os.system('mkdir hari06'))

# import os
# print(dir(os))
# print(help(os))

# print(os.chdir('/alumni/minggu1'))

# import shutil
# print(shutil.copyfile('saya1.db', 'kami.db'))
# print(shutil.move('/percobaan_os/saya', 'os1'))


# import glob
# print(glob.glob('*.glob1py'))

# import sys
# print(sys.argv)

# import argparse

# parser = argparse.ArgumentParser(
#     prog='top',
#     description='Show top lines from each file')
# parser.add_argument('saya1.db.', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)

# print(sys.stderr.write('Warning, log file not found starting a new one\n'))

# membaca huruf depan -bf- membaca f saja kalau b itu artinya ber-awalan
# import re
# print(re.findall(r'\bf[a-z]*', 'fandai fandai tupai falu kudune fanny'))
# print(re.sub(r'(\b[a-z]+) \1', r'\1', 'saya makan nasi'))
# print('teh untuk dua juga'.replace('juga', 'orang'))

# import math
# print(math.cos(math.pi / 5))
# print(math.log(1024, 4))

# # memanggil 3 dari kiri
# import random
# print(random.choice(['apel', 'jeruk', 'kates', 'semongko', 'gandul']))

# # pengambilan sampel tanpa penggantian
# print(random.sample(range(200), 20))

# # acak
# print(random.random())

# # bilangan bulat acak yang dipilih dari rentang (4)
# print(random.randrange(4))

# import statistics
# data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# print(statistics.mean(data))
# print(statistics.median(data))
# print(statistics.variance(data))

# from urllib.request import urlopen
# with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
#     for line in response:
#        line = line.decode()
#        if line.startswith('datetime'):
#            print(line.rstrip())


# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('kapasansyafak@gmail.com', 'familybuah@gmail.com',
# """To: kapasansyafak@gmail.com
# From: familybuah@gmail.com
# Beware the Ides of March.
# """)


# from datetime import date
# now = date.today()
# print(now)
# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# birthday = date(1964, 7, 31)
# age = now - birthday
# print(age.days)

# import zlib
# s = b'witch which has which witches wrist watch'
# print(len(s))

# t = zlib.compress(s)
# print(len(t))

# zlib.decompress(t)
# print(zlib.crc32(s))

# from timeit import Timer
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# print(Timer('a,b = b,a', 'a=1; b=2').timeit())


# def average(values):
#     """Computes the arithmetic mean of a list of numbers.

#     print(average([20, 30, 70]))
#     40.0
#     """
#     return sum(values) / len(values)

# import doctest

# import unittest

# class TestStatisticalFunctions(unittest.TestCase):
#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#         with self.assertRaises(ZeroDivisionError):
#             average([])
#         with self.assertRaises(TypeError):
#             average(20, 30, 70)
# print(unittest.main())