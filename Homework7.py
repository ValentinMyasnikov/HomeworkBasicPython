"""Задание 1"""

# class Matrix:
#     def __init__(self, matrix1, matrix2):
#         self.matrix1 = matrix1
#         self.matrix2 = matrix2
#
#
#     def matrix_re(self):
#         for i in self.matrix1:
#             for j in i:
#                 print(j, end=' ')
#             print()
#
#     def matrix_rec(self):
#         for i in self.matrix2:
#             for j in i:
#                 print(j, end=' ')
#             print()
#
#     def matrix_sum(self):
#         user_list1 = []
#         user_list2 = []
#         user_list3 = []
#         user_list4 = []
#         for i in self.matrix1:
#             for j in i:
#                 user_list1.append(j)
#         for x in self.matrix2:
#             for y in x:
#                 user_list2.append(y)
#         z = list(map(sum, zip(user_list1, user_list2)))
#         for el in z[0:2]:
#             user_list3.append(el)
#         for el in z[2:4]:
#             user_list4.append(el)
#         for t in zip(user_list3, user_list4):
#             print(t[0], t[1])
#
# Matrix1 = Matrix([[1, 2], [3, 4]], [[5, 6], [7, 8]])
#
# Matrix1.matrix_re()
# Matrix1.matrix_rec()
# Matrix1.matrix_sum()


"""Задание 2"""

# from abc import ABC, abstractmethod
# user_list = []
#
# class Cloth(ABC):
#     @abstractmethod
#     def cons(self):
#         pass
#
# class Coat(Cloth):
#     def __init__(self, size):
#         self.size = size
#
#     def cons(self):
#         x = round(self.size / 6.5 + 0.5, 2)
#         user_list.append(x)
#         return f'Расход материала на пальто: {x}'
#
# class Suit(Cloth):
#
#     def __init__(self, height):
#         self.height = height
#
#     def cons(self):
#         y = round(self.height * 2 + 0.3, 2)
#         user_list.append(y)
#         return f'Расход материала на костюм: {y}'
#
#
# def summ():
#     return f'Всего необходимо материала: {round(sum(user_list), 2)}'
#
# Coat1 = Coat(4)
# print(Coat1.cons())
# Suit1 = Suit(4)
# print(Suit1.cons())
# Coat2 = Coat(8)
# print(Coat2.cons())
# print(summ())

"""Задание 3"""

# class Cell:
#
#     def __init__(self, number):
#         self.number = number
#
#     def __add__(self, other):
#         return self.number + other.number
#
#     def __sub__(self, other):
#         if (self.number - other.number) < 0:
#             return f'Разность количества ячеек меньше нуля'
#         else:
#             return self.number - other.number
#
#     def  __mul__(self, other):
#         return self.number * other.number
#
#     def __floordiv__(self, other):
#         return self.number // other.number
#
#     def make_order(self, row):
#         x = self.number // row
#         y = self.number % row
#         for i in range(0, row):
#             print('*' * x)
#         print('*' * y)
#
# Cell1 = Cell(20)
# Cell1.make_order(3)
#
# Cell2 = Cell(9)
# Cell2.make_order(2)
#
# print(Cell1 + Cell2)
# print(Cell1 - Cell2)
# print(Cell1 * Cell2)
# print(Cell1 // Cell2)