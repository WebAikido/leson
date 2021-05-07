# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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
print('--------------------------')


figures = ['треугольник', 'квадрат', 'пятиугольник', 'шестиугольник']
a = 1
for i in figures:
    print(a, ':', i)
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
    figure_number = int(input('Введите желаемый номер фигуры:'))
    if 0 < number_color < 8 :
        color = color[number_color - 1][0]
        next_point = sd.get_point(300, 300)
        if 0 < figure_number < 5:
            figure_number += 2
            drawing_polygon(number_of_parties=figure_number, next_point=next_point, color=color)
            break
        else:
            print('Вы ввели не коректный номер фигуры')
    else:
        print('Вы ввели не коректное число')

sd.pause()
