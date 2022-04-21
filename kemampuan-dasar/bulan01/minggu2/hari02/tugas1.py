# def test_sum():
#     assert sum([1, 2, 3]) == 6, "Should be 6"

# if __name__ == "__main__":
#     test_sum()
#     print("cek nama")


# def test_sum():
#     assert sum([1, 2, 3]) == 6, "Should be 6"

# def test_sum_tuple():
#     assert sum((1, 2, 2)) == 6, "Should be 6"

# if __name__ == "__main__":
#     test_sum()
#     test_sum_tuple()
# print("Everything passed")

# python test_sum_2.py

# import unittest


# class TestSum(unittest.TestCase):

#     def test_sum(self):
#         self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

#     def test_sum_tuple(self):
#         self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

# if __name__ == '__main__':
#     unittest.main()

# python3 test_sum_unittest.py


# musyaffak@musyaffak-Aspire-E5-475:~/Praxis-Academy/kemampuan-dasar$ pip install nose2
# Collecting nose2
#   Downloading nose2-0.11.0-py2.py3-none-any.whl (144 kB)
#      |████████████████████████████████| 144 kB 543 kB/s 
# Requirement already satisfied: six>=1.7 in /usr/lib/python3/dist-packages (from nose2) (1.14.0)
# Collecting coverage>=4.4.1
#   Downloading coverage-6.3.2-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (212 kB)
#      |████████████████████████████████| 212 kB 868 kB/s 
# Installing collected packages: coverage, nose2
#   WARNING: The scripts coverage, coverage-3.8 and coverage3 are installed in '/home/musyaffak/.local/bin' which is not on PATH.
#   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
#   WARNING: The scripts nose2 and nose2-3.8 are installed in '/home/musyaffak/.local/bin' which is not on PATH.
#   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
# Successfully installed coverage-6.3.2 nose2-0.11.0

# musyaffak@musyaffak-Aspire-E5-475:~/Praxis-Academy/kemampuan-dasar$ python3 -m nose2

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK


# def test_sum():
#     assert sum([1, 2, 3]) == 6, "Should be 6"

# def test_sum_tuple():
#     assert sum((1, 2, 2)) == 6, "Should be 6"
# print(sum)

# def sum(arg):
#     total = 0
#     for val in arg:
#         total += val
#     return total
# print(sum)

# target = __import__("my_sum.py")
# sum = target.sum
# print(sum)


# import unittest

# # from my_sum import sum
# class TestSum(unittest.TestCase):
#     def test_list_int(self):
#         """
#         Test that it can sum a list of integers
#         """
#         data = [1, 2, 3]
#         result = sum(data)
#         self.assertEqual(result, 6)

# if __name__ == '__main__':
#     unittest.main()

# musyaffak@musyaffak-Aspire-E5-475:~/Praxis-Academy/kemampuan-dasar$ python3 -m unittest test

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK

# musyaffak@musyaffak-Aspire-E5-475:~/Praxis-Academy/kemampuan-dasar$ python3 -m unittest discover

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK

# musyaffak@musyaffak-Aspire-E5-475:~/Praxis-Academy/kemampuan-dasar$ python3 -m unittest discover -s test
# .....................s.....................
# ----------------------------------------------------------------------
# Ran 43 tests in 6.112s

# OK (skipped=1)



