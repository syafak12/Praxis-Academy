# x = int(input("Please enter an interger : "))
# if x < 0 :
#     x = 0
#     print("Negative Changed to Zero")
# elif x == 0 :
#     print("Zero")
# elif x == 1 :
#     print("Single")
# elif x == 2 :
#     print("doble")
# else :
#     print("More")



# words = ['cat,'window','defenestrate']
# for W in words:
# print(w, len(w))

# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status

# print(active_users)

# for i in range(10, 6,-2):
#     print(i)

# for i in range(10, 6,-2):
#     print('*'*i)

# for i in range(10,5):
#     print(i)

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])

# range(10)
# range(0, 10)
# sum(range(4))  # 0 + 1 + 2 + 3 :

# for n in range(2, 10) :
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)


# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found an odd number", num)

# while True:
#     pass # Busy-wait for keyboart interrupt
# class MyEmptyClass :
#     pass
# def initlog(*args) :
#     pass # Remember to implement this!

# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case 408:
#             return "I LOVE YOU"
#         case _:
#             return "Something's wrong with the internet"

# print(http_error(408))

# class point:
#     x: float
#     y: float
# # point =(x, y)
# # def func(point):
# match point:
#     case (0, 0):
#         print("Origin")
#     case (0, y):
#         print(f"Y={y}")
#     case (x, 0):
#         print(f"X={x}")
#     case (x, y):
#         print(f"X={x}, Y={y}")
#     case _:
#         raise ValueError("Not A Point")

# class point:
#     x: int
#     y: int
# point =(x, y)
# def func(point):
#     match point:
#         case Point(x=0, y=0):
#             print("Origin")
#         case Point(x=0, y=y):
#             print(f"Y={y}")
#         case Point(x=x, y=0):
#             print(f"X={x}")
#         case Point():
#             print("Somewhere else")
#         case _:
#             raise ValueError("Not A Point")


# class point:
#     x: vars
#     y: vars
# point(1, x=vars)
# point(1, y=vars)
# point(x=1, y=vars)
# point(y=vars, x=1)

# match points:
#     case []:
#         print("No points")
#     case [Point(0, 0)]:
#         print("The origin")
#     case [Point(x, y)]:
#         print(f"Single point {x}, {y}")
#     case [Point(0, y1), Point(0, y2)]:
#         print(f"Two on the Y axis at {y1}, {y2}")
#     case _:
#         print("Something else")



# match point:
#     case Point(x, y) if x == y:
#         print(f"Y=X at {x}")
#     case Point(x, y):
#         print(f"Not on the diagonal")

# from enum import Enum
# class Color(Enum):
#     RED = 'red'
#     GREEN = 'green'
#     BLUE = 'blue'

# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")

# def fib(link):
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < link:
#         print(a, end=' ')
#         a, b = b, a+b
#         print()
# fib(2000)

# # fib
# f = fib
# f(100)

# def fib2(n): 
#     """Return a list containing the Fibonacci series up to n."""
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)  
#         a, b = b, a+b
#         return result
#     f100 = fib2(100)

# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)



# i = 7

# def f(arg=i):
#     print(arg)

# i = 8
# f()



# def f(a, L=[]):
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))


# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L


# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")
# parrot(100)
        
# parrot(1000)  
# parrot(voltage=1000)
# parrot(voltage=1000000, action='VOOOOOM') 
# parrot(action='VOOOOOM', voltage=1000000)
# parrot('a million', 'bereft of life', 'jump') 
# parrot('a thousand', state='pushing up the daisies')


# untuk 5 ini kalau di gabung sama yang atas hasilnya error
# parrot()
# parrot(voltage=5.0, 'dead')
# parrot(110, voltage=200)
# parrot(actor='John Cleese')
# parrotparrot(voltage=1000)



# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")
# def standard_arg(arg):
#     print(arg)
# def pos_only_arg(arg, /):
#     print(arg)
# def kwd_only_arg(*, arg):
#     print(arg)
# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)
# standard_arg(2)
# standard_arg(arg=2)
# pos_only_arg(1)
# pos_only_arg(3)
# combined_example(1, 2, kwd_only=3)
# combined_example(1, 2, kwd_only=7)
# combined_example(1, standard=2, kwd_only=3)



# def foo(name, **kwds):
#     return 'name' in kwds
# print("def foo")

# def foo(name, /, **kwds):
#     return 'name' in kwds
#     foo(1, **{'name': 2})
# print(True)


# def concat(*args, sep="/"):
#     return sep.join(args)
# print(concat("earth", "mars", "venus"))
# print(concat("earth", "mars", "venus", sep="."))


# list(range(3, 6))
# print(list(range(3, 6)))
# args = (5, 10)
# print(list(range(*args)))


# def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")
# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)


# def make_incrementor(n):
#     return lambda a: a + n
# f = make_incrementor(42)
# print(f(2))
# print(f(8))


# pairs = [(0, 'nol'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)


# pairs = [(6, 'six'), (5, 'five'), (2, 'two'), (3, 'three'), (0, 'nol')]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)



# def f(ham: str, eggs: str = 'eggs') -> str:
#     print("Annotations:", f.__annotations__)
#     print("Argument:", ham, eggs)
#     return ham + ' and ' + eggs
# print(f('spam'))



