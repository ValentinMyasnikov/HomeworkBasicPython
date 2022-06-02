"""Задание 1"""

# import time
# i = 0
# class TrafficLight:
#     __color = ['red', 'yellow', 'green']
#
#
#     def running(self):
#         for i in range(3):
#             i += 1
#             if i == 1:
#                 print(f'Светофор переключается\n{self.__color[0]}')
#                 time.sleep(7)
#             elif i == 2:
#                 print(f'Светофор переключается\n{self.__color[1]}')
#                 time.sleep(2)
#             else:
#                 print(f'Светофор переключается\n{self.__color[2]}')
#                 time.sleep(5)
#
#         print('Светофор сломался, найдите другой светофор')
#
# TrafficLight1 = TrafficLight()
# TrafficLight1.running()

"""Задание 2"""

# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def asphalt(self):
#         mass = int(input('Введите массу асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см: '))
#         thick = int(input('Введите число см толщины полотна: '))
#         return (self._length * self._width * mass * thick)/1000
#
# Road1 = Road(5000, 20)
# print(f'Масса асфальта: {Road1.asphalt()} т')
# Road2 = Road(15000, 30)
# print(f'Масса асфальта: {Road2.asphalt()} т')

"""Задание 3"""


# class Worker:
#     def __init__(self, name, surname, position, income):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = income
#         self._income = {"wage": 10, "bonus": 5}
#
# class Position(Worker):
#
#     def __init__(self, name, surname, position, income):
#         super().__init__(name, surname, position, income)
#
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     def get_total_income(self):
#         return self._income['wage'] + self._income['bonus']
#
#     def info(self):
#         return f'Общая информация:\nРабочий по имени {self.name + " " + self.surname} занимает должность {self.position}, получает общий доход в размере {self._income["wage"] + self._income["bonus"]},\nиз которых оклад: {self._income["wage"]}, премия: {self._income["bonus"]}'
#
#
#
# Position1 = Position('Jack', 'Black', 'manager', 23)
# print(Position1.get_full_name())
# print(Position1.get_total_income())
# print(Position1.info())

"""Задание 4"""


# class Car:
#     def __init__(self, speed, color, name, is_police, show_speed):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#         self.show_speed = show_speed
#
#     def go(self):
#         return 'Машина едет'
#
#     def turn(self):
#         return 'Машина повернула налево'
#
#
#     def stop(self):
#         return 'Машина остановилась'
#
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police, show_speed, mileage):
#         Car.__init__(self, speed, color, name, is_police, show_speed)
#         self.mileage = mileage
#     def info(self):
#         if self.is_police == False:
#             print(f'Car 1 (towncar?): speed: {self.speed} mph, current speed: {self.show_speed} mph, color: {self.color}, name: {self.name}, mileage: {self.mileage} km')
#         elif self.is_police == True:
#             print(f'Car 1 (towncar?): an undercover detective perhaps!!!')
#         if self.show_speed > 60:
#             return 'Скорость превышена'
#         else:
#             return 'Скорость в пределах нормы'
#
#
# class SportCar(Car):
#     def __init__(self,  speed, color, name, is_police, show_speed, horsepower):
#         Car.__init__(self,  speed, color, name, is_police, show_speed)
#         self.horsepower = horsepower
#
#     def info(self):
#         if self.is_police == False:
#             return f'Car 2 (sportcar?): speed: {self.speed} mph, color: {self.color}, name: {self.name}, horsepower: {self.horsepower}'
#         elif self.is_police == True:
#             return f'Car 2 (sportcar?): an undercover detective perhaps!!!'
#
# class WorkCar(Car):
#     def __init__(self,  speed, color, name, is_police, show_speed, capacity):
#         Car.__init__(self,  speed, color, name, is_police, show_speed)
#         self.capacity = capacity
#
#     def info(self):
#         if self.is_police == False:
#             print(f'Car 3 (workcar?): speed: {self.speed} mph, current speed: {self.show_speed} mph, color: {self.color}, name: {self.name}, capacity: {self.capacity}')
#         elif self.is_police == True:
#             print(f'Car 3 (workcar?): an undercover detective perhaps!!!')
#
#         if self.show_speed > 40:
#             return 'Скорость превышена'
#         else:
#             return 'Скорость в пределах нормы'
#
# class PoliceCar(Car):
#     def __init__(self,  speed, color, name, is_police, show_speed, cop):
#         Car.__init__(self,  speed, color, name, is_police, show_speed)
#         self.cop = cop
#     def info(self):
#         if self.is_police == True:
#             return f'Car 4 (policecar?): speed: {self.speed} mph, color: {self.color}, name: {self.name}, cops: {self.cop}, a real police car'
#         elif self.is_police == False:
#             return f'Car 4 (policecar?): not a real police car, DANGER!!!'
#
#
#
# Car1 = TownCar(85,'red', 'honda', False, 70, 2300)
# print(Car1.info())
# print(Car1.turn())
#
# Car2 = SportCar(150,'green', 'bugatti', False, 35, 360)
# print(Car2.info())
# print(Car2.go())
#
# Car3 = WorkCar(55,'orange', 'ford', False, 23, 100)
# print(Car3.info())
# print(Car2.stop())
#
# Car4 = PoliceCar(100, 'blue', 'mazda', True, 34, 5)
# print(Car4.info())
# print(Car4.go())


"""Задание 5"""

# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return f'Запуск отрисовки'
#
#
# class Pen(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'Запуск отрисовки {self.title}'
#
#
# class Pencil(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'Запуск отрисовки {self.title}'
#
# class Handle(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'Запуск отрисовки {self.title}'
#
#
# Stationery1 = Stationery('graffity')
# print(Stationery1.draw())
#
# Stationery1 = Pen('Pen')
# print(Stationery1.draw())
#
# Stationery1 = Pencil('Pencil')
# print(Stationery1.draw())
#
# Stationery1 = Handle('Handle')
# print(Stationery1.draw())