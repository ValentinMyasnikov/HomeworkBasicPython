"""Задание 1."""

# def user_func():
#     try:
#         x = int(input('Введите первое число: '))
#         y = int(input('Введите второе число: '))
#         z = x / y
#         print(z)
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
# user_func()

"""Задание 2."""

# def user_func(name, surname, year, city, email, phone):
#     print(f'Имя: {name}, фамилия: {surname}, город проживания: {city}, год рождения: {year}, электронная почта: {email}, номер телефона: {phone}')
# user_func(surname='Brown', name='Jack', email='Jack_Brown@gmail.ru', year=1990, phone=123456, city='London')

"""Задание 3."""

# def user_func(x, y, z):
#     user_list = [x, y, z]
#     user_list.remove(min(user_list))
#     return (sum(user_list))
# print(user_func(6, 2, 9))

"""Задание 4/1."""

# def user_func(x, y):
#     return x**y
#
# print(user_func(1,-2))

"""Задание 4/2."""

# def user_func(x, y):
#     result = 1
#     for i in range(abs(y)):
#         result *= x
#     if y >= 0:
#         return result
#     else:
#         return 1 / result
#
# print(user_func(2, -4))

"""Задание 5."""

# final_list = []
# def user_func():
#     while True:
#         user_list = input('Введите числа через пробел, если хотите выйти из программы напишите stop в любом месте: ').split()
#         for i in user_list:
#             if i == 'stop':
#                 index = user_list.index('stop')
#                 user_list.remove('stop')
#                 user_list = list(map(int, user_list))
#                 sum1 = sum(user_list[0:index])
#                 print('Вы ввели stop, программа будет завершена, сумма чисел до stop: ', sum1)
#                 final_list.append(sum1)
#                 final_sum = print('Программа завершена, итоговая сумма: ', sum(final_list))
#                 return
#         user_list = list(map(int, user_list))
#         user_sum = sum(user_list)
#         print('Сумма чисел в списке: ', user_sum)
#         final_list.append(user_sum)
#         final_sum = print('Общая сумма: ', sum(final_list))
#
# user_func()

"""Задание 6."""

# def int_func(x):
#     x = x.title()
#     return x
#
# print(int_func('привет, как дела?'))

"""Задание 7."""

# def int_func():
#     user_str = input('Текст: ')
#     user_str = user_str.title()
#     return user_str
#
# print(int_func())