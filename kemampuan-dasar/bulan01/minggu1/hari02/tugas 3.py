# year = 2016
# event = 'Referendum'
# f'Results of the {year} {event}'


# yes_votes = 42_572_654
# no_votes = 43_132_495
# percentage = yes_votes / (yes_votes + no_votes)
# '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)


# s = 'Hello, world.'
# str(s)
# repr(s)
# str(1/7)
# x = 10 * 3.25
# y = 200 * 200
# s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
# print(s)

# hello = 'hello, world\n'
# hellos = repr(hello)
# print(hellos)

# repr((x, y, ('spam', 'eggs')))

# import math
# print(f'The value of pi is appoximately {math.pi:.3f}.')

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():
#     print(f'{name:10} ==> {phone:10d}')


# animals = 'eels'
# print(f'My hovercraft is full of {animals}.')
# print(f'My hovercraft is full of {animals!r}.')

# print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# print('{0} and {1}'.format('spam', 'eggs'))
# print('{1} and {0}'.format('spam', 'eggs'))

# print('This {food} is {adjective}.'.format(
#     food='spam', adjective='absolutely horrible'))

# print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='georg'))

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ' 'Dcab: {0[Dcab]:d}'.format(table))

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
#     print(repr(x*x*x).rjust(4))


# '12'.zfill(5)
# '-3.14'.zfill(7)
# '3.14159265359'.zfill(5)

# import math
# print('The value of pi is approximately %5.3f.' % math.pi)


# f = open('syafak.txt', 'r')

# with open('syafak.txt') as f:
#     read_data = f.read()
#     print(read_data)
# print(f.read)  
# print(f.closed)

# f = open('inputisifile.txt', 'r')

# with open('inputisifile.txt') as f:
#     read_data = f.read()
#     print(read_data)
# print(f.read)  


# for line in f:
#     print(line, end='')


f = open('syafak.txt', 'w')
print(f.write('This is a test\n'))

value = ('the answer', 42)
s = str(value)  # convert the tuple to string
print(f.write(s))

f = open('syafak.txt', 'rb+')
print(f.write(b'0123456789abcdef'))
print(f.seek(5))
print(f.read(1))
print(f.seek(-3, 2))
print(f.read(1))


import json
x = [1, 'simple', 'list']
print(json.dumps(x))




