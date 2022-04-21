# def add(a, b):
#     return a + b
# plus = add
# print(3, 4)

# (lambda a, b: a + b)(3, 4)  # returns 7
# addition = lambda a, b: a + b
# print(addition(3, 4))


# val = [1, 2, 3, 4, 5, 6]

# # Multiply every item by two
# list(map(lambda x: x * 2, val)) # [2, 4, 6, 8, 10, 12]
# # Take the factorial by multiplying the value so far to the next item
# reduce(lambda: x, y: x * y, val, 1) # 1 * 1 * 2 * 3 * 4 * 5 * 6


# def power(base, exp):
#     return base ** exp
# cube = partial(power, exp=3)
# cube(5)

# def retry(func):
#     def retried_function(*args, **kwargs):
#         exc = None
#         for _ in range(3):
#             try:
#                return func(*args, **kwargs)
#             except Exception as exc:
#                 print("Exception raised while calling %s with args:%s, kwargs: %s. Retrying" % (func, args, kwargs).

#         raise exc
#      return retried_function
# def do_something_risky()


# dictionary = ['fox', 'boss', 'orange', 'toes', 'fairy', 'cup']
# def puralize(words):
#    for i in range(len(words)):
#        word = words[i]
#        if word.endswith('s') or word.endswith('x'):
#            word += 'es'
#        if word.endswith('y'):
#            word = word[:-1] + 'ies'
#        else:
#            word += 's'
#        words[i] = word

# def test_pluralize():
#     pluralize(dictionary)
#     assert dictionary == ['foxes', 'bosses', 'oranges', 'toeses', 'fairies', 'cups']


# dictionary = ['fox', 'boss', 'orange', 'toes', 'fairy', 'cup']
# def puralize(words):
#    result = []
#    for word in words:
#        word = words[i]
#        if word.endswith('s') or word.endswith('x'):
#            plural = word + 'es')
#        if word.endswith('y'):
#            plural = word[:-1] + 'ies'
#        else:
#            plural = +  's'
#        result.append(plural)
#     return result

# def test_pluralize():
#     result = pluralize(dictionary)
#     assert result == ['foxes', 'bosses', 'oranges', 'toeses', 'fairies', 'cups']



# from collections import namedtuple
# VerbTenses = namedtuple('VerbTenses', ['past', 'present', 'future'])
# # versus
# class VerbTenses(object):
#     def __init__(self, past, present, future):
#         self.past = past,
#         self.present = present
#         self.future = future
# print(VerbTenses)


# class Bus(object):
#      passengers = set()
#      def add_passenger(self, person):
#         self.passengers.add(person)

# bus1 = Bus()
# bus2 = Bus()
# bus1.add_passenger('abe')
# bus2.add_passenger('bertha')
# bus1.passengers  # returns ['abe', 'bertha']
# bus2.passengers  # also ['abe', 'bertha']
# print(bus1.passengers)
# print(bus2.passengers)




