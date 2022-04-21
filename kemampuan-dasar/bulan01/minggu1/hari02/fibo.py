def fib(n):    
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
def fib2(n):   
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
#     return result
# from traceback import print_tb
# import fibo
# print(fibo.fib(1000))
# print(fibo.fib2(100))

# from fibo import fib, fib2
# print(fib(500))

# from fibo import *
# print(fib(500))

# from fibo import fib as fibonacce
# print(fibonacce(500))

# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))

# import sys
# sys.ps1
# sys.ps2
# sys.ps1 = 'C>'

# import fibo, sys
# print(dir(fibo))
# print(dir(sys))  

# a = [1, 2, 3, 4, 5]
# import fibo
# fib = fibo.fib
# print(dir())

# import builtins
# print(dir(builtins))

# import sound.effects.echo
# from sound.effects import echo

# from sound.effects.echo impo
# import sound.effects.echo
# import sound.effects.surround
# from sound.effects import *

# from . import echo
# from .. import formats
# from ..filters import equalizer



