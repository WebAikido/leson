# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 127, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_PURPLE = (255, 0, 255)

color = [
    (COLOR_RED, 'red'),
    (COLOR_ORANGE, 'orange'),
    (COLOR_YELLOW, 'yellow'),
    (COLOR_GREEN, 'green'),
    (COLOR_CYAN, 'cyan'),
    (COLOR_BLUE, 'blue'),
    (COLOR_PURPLE, 'purple'),
]

a = 1

for i, k in color:
    print(a, ':', k)
    a += 1


def hexagon(point, color, angle=30, length=100):
    v1 = sd.vector(start=point, angle=angle, length=length, color=color, width=3)
    return v1


def drawing_polygon(number_of_parties, next_point, color):
    x = int(360 / number_of_parties)
    for angle in range(0, 361, x):
        next_point = hexagon(point=next_point, angle=angle, color=color)


# pentagon = drawing_polygon(5, next_point=next_point)
while True:
    number_color = int(input('Введите желаемый цвет:'))

    if 0 < number_color < 8:
        color = color[number_color - 1][0]
        next_point = sd.get_point(300, 300)
        triangle = drawing_polygon(3, next_point=next_point, color=color)
        next_point = sd.get_point(100, 100)
        square = drawing_polygon(4, next_point=next_point, color=color)
        next_point = sd.get_point(400, 100)
        pentagon = drawing_polygon(5, next_point=next_point, color=color)
        next_point = sd.get_point(100, 400)
        hexagon = drawing_polygon(6, next_point=next_point, color=color)
        break
    else:
        print('Вы ввели не коректное число')

# print(color[number_color-1][0])
#
# color = color[1][0]
# drawing_polygon(3, next_point=next_point, color=color)

sd.pause()
