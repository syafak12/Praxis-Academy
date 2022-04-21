# def multiply_2_pure(numbers):
#     new_numbers = []
#     for n in numbers:
#         new_numbers.append(n * 2)
#     return new_numbers

# original_numbers = [1, 3, 5, 10]
# changed_numbers = multiply_2_pure(original_numbers)
# print(original_numbers) 
# print(changed_numbers) 


# mutable_collection = ['Tim', 10, [4, 5]]
# immutable_collection = ('Tim', 10, [4, 5])

# # Reading from data types are essentially the same:
# print(mutable_collection[2])
# print(immutable_collection[2])

# 21-25 belum bisa
# # Let's change the 2nd value from 10 to 15
# mutable_collection[1] = 15

# # This fails with the tuple
# immutable_collection[1] = 15

# immutable_collection[2].append(6)
# print(immutable_collection[2])

# 31 belum bisa
# immutable_collection[2] = [4, 5]

# def write_repeat(message, n):
#     for i in range(n):
#         print(message)

# def hof_write_repeat(message, n, action):
#     for i in range(n):
#         action(message)

# hof_write_repeat('Hello', 5, print)

# # Import the logging library
# import logging
# # Log the output as an error instead
# hof_write_repeat('Hello', 5, logging.error)

# def add2(numbers):
#     new_numbers = []
#     for n in numbers:
#         new_numbers.append(n + 2)
#     return new_numbers

# print(add2([23, 88]))

# def hof_add(increment):
#     # Create a function that loops and adds the increment
#     def add_increment(numbers):
#         new_numbers = []
#         for n in numbers:
#             new_numbers.append(n + increment)
#         return new_numbers
#     # We return the function as we do any other value
#     return add_increment

# add5 = hof_add(5)
# print(add5([23, 88]))  
# add10 = hof_add(10)
# print(add10([23, 88])) 

# def hof_product(multiplier):
#     return lambda x: x * multiplier

# mult6 = hof_product(6)
# print(mult6(6))


# names = ['Shivani', 'Jason', 'Yusef', 'Sakura']
# greeted_names = map(lambda x: 'Hi ' + x, names)

# # This prints something similar to: <map object at 0x10ed93cc0>
# print(greeted_names)
# # Recall, that map returns an iterator 

# # We can print all names in a for loop
# for name in greeted_names:
#     print(name)


# numbers = [13, 4, 18, 35]
# div_by_5 = filter(lambda num: num % 5 == 0, numbers)

# # We can convert the iterator into a list
# print(list(div_by_5))


# # Let's arbitrarily get the all numbers divisible by 3 between 1 and 20 and cube them
# arbitrary_numbers = map(lambda num: num ** 3, filter(lambda num: num % 3 == 0, range(1, 21)))

# print(list(arbitrary_numbers)) 


# # Recall
# names = ['Shivani', 'Jan', 'Yusef', 'Sakura']
# # Instead of: map(lambda x: 'Hi ' + x, names), we can do
# greeted_names = ['Hi ' + name for name in names]

# print(greeted_names)


# # Recall
# numbers = [13, 4, 18, 35]
# # Instead of: filter(lambda num: num % 5 == 0, numbers), we can do
# div_by_5 = [num for num in numbers if num % 5 == 0]

# print(div_by_5) # [35]

# # We can manage the combined case as well:
# # Instead of: 
# # map(lambda num: num ** 3, filter(lambda num: num % 3 == 0, range(1, 21)))
# arbitrary_numbers = [num ** 3 for num in range(1, 21) if num % 3 == 0]
# print(arbitrary_numbers)








