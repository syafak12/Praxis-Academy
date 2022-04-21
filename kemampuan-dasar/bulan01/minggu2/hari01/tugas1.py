# list(map(int, ["1", "2", "3"]))
# print(list)


# def hello_world(h):
#     def world(w):
#         print(h, w)
#         return world # returning functions
# h = hello_world # assigning
# x = h("hello") # assigning
# print(x)
# # x("world")
# function_list = [h, x]
# function_list

# def naive_sum(list):
#     s = 0
#     for l in list:
#         s += l
#     return s
# sum(list)

# def func1():
#     pass
# def func2():
#     pass
# def func3():
#     pass
# print(executing = lambda f: f())


# def fib(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return fib(n-1)+fib(n-2)


# # procedural code
# starting_number = 96

# # get the square of the number
# square = starting_number ** 2

# # increment the number by 1
# increment = square + 1

# # cube of the number
# cube = increment ** 3

# # decrease the cube by 1
# decrement = cube - 1

# # get the final result
# result = print(decrement)


# # define a function `call` where you provide the function and the arguments
# def call(x, f):
#     return f(x)

# # define a function that returns the square
# square = lambda x : x*x

# # define a function that returns the increment
# increment = lambda x : x+1

# # define a function that returns the cube
# cube = lambda x : x*x*x

# # define a function that returns the decrement
# decrement = lambda x : x-1

# # put all the functions in a list in the order that you want to execute them
# funcs = [square, increment, cube, decrement]

# # bring it all together. Below is the non functional part. 
# # in functional programming you separate the functional and the non functional parts.
# from functools import reduce # reduce is in the functools library
# print(reduce(call, funcs, 96))


