
"""Задание 1"""

# from sys import argv
#
# def user_salary(a,b,c):
#     return a*b+c
#
# ar1, ar2, ar3 = map(int, argv[1:])
# print(user_salary(ar1, ar2, ar3))

"""Задание 2"""

# new_list = []
# user_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

"""Вариант 1 (генератор)"""

# user_list = [new_list.append(user_list[i+1]) for i in range(len(user_list)-1) if user_list[i] < user_list[i+1]]
# print(new_list)

"""Вариант 2 (условия)"""

# for i in range(len(user_list)-1):
#     if user_list[i] < user_list[i+1]:
#         new_list.append(user_list[i+1])
#
# print(new_list)

"""Задание 3"""

# user_list = list(range(20, 241))
# print(user_list)
# user_list = [el for el in user_list if el % 20 == 0 or el % 21 ==0]
# print(user_list)

"""Задание 4"""

# new_list = []
# user_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# user_list = [new_list.append(i) for i in user_list if user_list.count(i) == 1]
# print(new_list)

"""Задание 5"""

# from functools import reduce
# user_list = [el for el in range(100, 1001) if el % 2 == 0]
# def mult(a, b):
#     return a*b
# print(reduce(mult, user_list))

"""Задание 6"""

# from itertools import count, cycle
# from random import randint
#
# x = randint(1, 14)
# for el in count(x):
#     if el % 2 == 0:
#         print(el)
#         if el == 14:
#             break
#
# i = 0
# for el in cycle('Привет'):
#     i = i+1
#     print(el)
#     if i == 6:
#         break

"""Задание 7"""

# from math import factorial
#
# def user_func(a):
#     for i in range(1, a + 1):
#         yield factorial(i)
#
# for el in user_func(5):
#     print(el)