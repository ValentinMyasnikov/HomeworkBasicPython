# Задание 1.

# user_list = ['Hello', 123, True, 43, 'Kate']
# for i in user_list:
#     print(type(i))

# Задание 2.

# user_list = []
# el_num = int(input('Введите количество элементов списка: '))
# for el in range(el_num):
#     el_user = input('Введите элемент списка: ')
#     user_list.append(el_user)
# print(user_list)
# for i in range(0, len(user_list)-1, 2):
#     user_list[i], user_list[i+1] = user_list[i+1], user_list[i]
# print(user_list)

# Задание 3.

# month = int(input('Введите номер месяца: '))
# dict_month = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
# for i in dict_month:
#      if month in dict_month[i]:
#          print(i)

# Задание 4.

# user_str = input('Введите строку: ').split()
# for i, word in enumerate(user_str, 1):
#     i = str(i)
#     print('№'+ i + ':', word[:10])


# Задание 5.

# my_list = [7, 6, 5, 4, 3]
# while True:
#     print(my_list)
#     numb = int(input('Введите число: '))
#     my_list.append(numb)
#     my_list.sort(reverse=True)

# Задание 6/1. Первая часть

# user_dict1 = {}
# print('Словарь 1')
# for el in range(4):
#     a = input('Введите ключ: ')
#     b = input('Введите значение: ')
#     user_dict1[a] = b
# print('Словарь 1: ', user_dict1)
# cort1 = (1, user_dict1)
# user_dict2 = {}
# print('Словарь 2')
# for el in range(4):
#     a = input('Введите ключ: ')
#     b = input('Введите значение: ')
#     user_dict2[a] = b
# print('Словарь 2: ', user_dict2)
# cort2 = (2, user_dict2)
# user_dict3 = {}
# print('Словарь 3')
# for el in range(4):
#     a = input('Введите ключ: ')
#     b = input('Введите значение: ')
#     user_dict3[a] = b
# print('Словарь 3: ', user_dict3)
# cort3 = (3, user_dict3)
# user_list = []
# user_list.append(cort1)
# user_list.append(cort2)
# user_list.append(cort3)
# print(user_list)

# Задание 6/2.

# user_list1 = input('Введите наименование товаров: ').split()
# user_list2 = input('Введите цены товаров: ').split()
# user_list3 = input('Введите количество товаров: ').split()
# user_list4 = input('Введите единицы измерения товаров: ').split()
# user_dict = {}
# user_dict['название'] = user_list1
# user_dict['цена'] = user_list1
# user_dict['количество'] = user_list1
# user_dict['единицы измерения'] = user_list1
# print(user_dict)
