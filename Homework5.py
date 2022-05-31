"""Задание 1."""

# f = open(r'C:\Users\myasnikovvg\PycharmProjects\pythonProject/Homework5.txt', 'w', encoding='utf-8')
# from itertools import count
# for i in count():
#     user_text = input('Text: ')
#     print(user_text, file = f)
#     if user_text == '':
#         break
# f.close()

"""Задание 2"""

# f = open(r'C:\Users\myasnikovvg\PycharmProjects\pythonProject\Text', 'r', encoding='utf-8')
# i = 0
# x = 0
# for line in f:
#     i = i+1
#     print(f'Строка номер {i}: {line}', end = '')
#     print(f'Длинна строки номер {i}:', len(line.split()))
#     x = x + len(line.split())
# print('Общее колличество строк:', i)
# print('Общее колличество слов:', x)
# f.close()

"""Задание 3"""

# f = open(r'C:\Users\myasnikovvg\PycharmProjects\pythonProject\Text2', 'r', encoding='utf-8')
# x = 0
# user_list = []
# print('Сотрудники с зарплатой менее 20000:')
# for line in f:
#     line = line.split()
#     line2 = float(line[-1])
#     if line2 < 20000:
#         print(line[0])
#     x = round(x + line2, 2)
#     user_list.append(line2)
# print('Средняя зарплата всех сотрудников:', round(x/len(user_list), 2))

"""Задание 4"""

# f_base = open(r'C:\Users\myasnikovvg\PycharmProjects\pythonProject\Text3', 'r', encoding='utf-8')
# f_final = open(r'C:\Users\myasnikovvg\PycharmProjects\pythonProject\Text3Final', 'w', encoding='utf-8')
# user_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
# for line in f_base:
#     line = line.split()
#     for el in line:
#         if el in user_dict:
#             line[line.index(el)]=user_dict[el]
#             f_final.write(f'{" ".join(line)}\n')
#
# print(f_final)

"""Задание 5"""

# f = open(r'C:\Users\myasnikovvg\PycharmProjects\pythonProject\Text4', 'w', encoding='utf-8')
#
# user_numbers = input('Numbers: ')
# print(user_numbers, file = f)
# f.close()
# f = open(r'C:\Users\myasnikovvg\PycharmProjects\pythonProject\Text4', 'r', encoding='utf-8')
# for line in f:
#     line = line.split()
#     line = map(int, line)
# print(f'Сумма: {sum(line)}')

"""Задание 6"""

# x = []
# f = open(r'C:\Users\myasnikovvg\PycharmProjects\pythonProject\Timetable', 'r', encoding='utf-8')
# for line in f:
#     line = line.replace('(л)', '')
#     line = line.replace('(пр)', '')
#     line = line.replace('(лаб)', '')
#     line = line.replace(':', '')
#     line = line.split()
#     line2 = line.pop(0).split()
#     line = map(int, line)
#     line = str(sum(line)).split()
#     line = list(map(int, line))
#     user_dict = dict(zip(line2, line))
#     print(user_dict)

"""Задание 7"""

# import json
# firm_dict = {}
# avg_dict = {}
# x = 0
# firm_profit = []
# final_list = []
# f = open(r'C:\Users\myasnikovvg\PycharmProjects\pythonProject\Firms', 'r', encoding='utf-8')
# for line in f:
#     line = line.split()
#     income = int(line[2])
#     waste = int(line[3])
#     profit = income - waste
#     if profit > 0:
#         x = round(x + profit)
#         firm_profit.append(profit)
#     del line[1]
#     del line[2]
#     firm_name = line.pop(0)
#     firm_dict[firm_name] = income
# avg_profit = int(x / len(firm_profit))
# avg_dict["average_profit"] = avg_profit
# final_list.append(firm_dict)
# final_list.append(avg_dict)
# print(final_list)
# with open("my_file.json", "w") as write_f:
#     json.dump(final_list, write_f)