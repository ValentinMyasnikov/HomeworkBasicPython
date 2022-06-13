"""Задание 1"""

# class Data:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def set_data(cls, data):
#         d = int(data[0:2])
#         m = int(data[3:5])
#         y = int(data[6:10])
#         return cls(d, m, y)
#
#     @staticmethod
#     def print_data(obj):
#         if obj.day > 31 or obj.month > 12:
#             return f'Проверьте правильность даты'
#         elif obj.day < 1 or obj.month < 1:
#             return f'Проверьте правильность даты'
#         else:
#             return f'Day: {obj.day}, Month: {obj.month}, Year: {obj.year}'
#
# data1 = "23-01-2022"
# d1 = Data.set_data(data1)
# print(Data.print_data(d1))

"""Задание 2"""

# class Positive(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# try:
#     num1 = int(input('Введите число: '))
#     num2 = int(input('Введите делитель: '))
#     if num2 == 0:
#         raise Positive('На ноль делить нельзя')
# except (ValueError, Positive) as err:
#     print(err)
# else:
#     x = num1/num2
#     print(x)
# finally:
#     print('end')

"""Задание 3"""
# from itertools import count
#
# class Positive(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# x = None
# user_list = []
#
# for x in count():
#     try:
#         x = int(input('Введите число от 1 до 10, если хотите выйти из цикла - введите 0: '))
#         if x == 0:
#             print(user_list)
#             break
#         elif x != 0:
#             user_list.append(x)
#         else:
#             raise Positive('Слова не вводим')
#     except (ValueError, Positive) as err:
#         print(err)

"""Задание 4, 5, 6"""

# class OfficeEquipStorage():
#     def __init__(self, location, capacity, workers, loaders):
#         self.location = location
#         self.capacity = capacity
#         self.workers = workers
#         self.loaders = loaders
#
#     def storage_info(self):
#         return f'Месторасположение: {self.location}, вместимость: {self.capacity} куб.м, количество работников: {self.workers} чел., количество погрузчиков: {self.loaders} машин'
#
# St1 = OfficeEquipStorage('rural', 10000, 10, 5)
# print(St1.storage_info())
#
# class OfficeEquipment():
#     def __init__(self, model, year, price, amount):
#         self.model = model
#         self.year = year
#         self.price = price
#         self.amount = amount
#
# class Printer(OfficeEquipment):
#     def __init__(self, model, year, price, amount, print_speed):
#         super().__init__(model, year, price, amount)
#         self.print_speed = print_speed
#
#     def printer_info(self):
#         return f'Модель: {self.model}, год выпуска: {self.year}, цена: {self.price} руб., количество на складе: {self.amount} шт., скорость печати: {self.print_speed} стр/мин'
#
# Pr1 = Printer('samsung', 2010, 6000, 15, 50)
# print(Pr1.printer_info())
#
# class Scan(OfficeEquipment):
#     def __init__(self, model, year, price, amount, scan_quality):
#         super().__init__(model, year, price, amount)
#         self.scan_quality = scan_quality
#
#     def scan_info(self):
#         return f'Модель: {self.model}, год выпуска: {self.year}, цена: {self.price} руб., количество на складе: {self.amount} шт., качество сканирования: {self.scan_quality} dpi'
#
# Sc1 = Scan('huawei', 2019, 14000, 8, 1200)
# print(Sc1.scan_info())
#
#
# class Copy(OfficeEquipment):
#     def __init__(self, model, year, price, amount, copy_speed, copy_quality):
#         super().__init__(model, year, price, amount)
#         self.copy_speed = copy_speed
#         self.copy_quality = copy_quality
#
#     def copy_info(self):
#         return f'Модель: {self.model}, год выпуска: {self.year}, цена: {self.price} руб., количество на складе: {self.amount} шт., скорость копирования: {self.copy_speed} стр/мин, качество копирования: {self.copy_quality} dpi'
#
# Cop1 = Copy('hp', 2015, 11000, 12 , 30, 1000)
# print(Cop1.copy_info())
#
'''ЧТО ОТПРАВИТЬ НА СКЛАД'''
#
# def to_store():
#     user_dict = {}
#     while True:
#         ask = int(input('Что отправить на склад? Введите: 1 - принтер, 2 - сканер, 3 - ксерокс. Для завершения программы введите 4. Введите: '))
#         if ask == 1:
#             pr_model = input('Введите модель: ')
#             user_dict['Принтеры'] = user_dict.get('Принтеры', []) + [pr_model]
#             print(user_dict)
#         elif ask == 2:
#             sc_model = input('Введите модель: ')
#             user_dict['Сканеры'] = user_dict.get('Сканеры', []) + [sc_model]
#             print(user_dict)
#         elif ask == 3:
#             xer_model = input('Введите модель: ')
#             user_dict['Ксероксы'] = user_dict.get('Ксероксы', []) + [xer_model]
#             print(user_dict)
#         else:
#             print(f"Итого на склад.\nПринтеров: {len(user_dict.get('Принтеры'))} шт.\nСканеров: {len(user_dict.get('Сканеры'))} шт.\nКсероксов: {len(user_dict.get('Ксероксы'))} шт.")
#             print(f'Модели: {user_dict}')
#             break
#
# to_store()

"""Задание 7"""

# class Complex:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __add__(self, other):
#         return f'{self.a + other.a} + {self.b + other.b} * i'
#
#     def __mul__(self, other):
#         return f'{self.a * other.a} + {self.b * other.b} * i'
#
# mc_1 = Complex(10, 20)
# mc_2 = Complex(30, 40)
# print(mc_1 + mc_2)
# print(mc_1 * mc_2)
