# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
root_point = sd.get_point(300, 30)

# def branch(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v2.draw()
#     return v1.end_point, v2.end_point
#
#
# angle_0 = 90
# length_0 = 100
# next_point1, next_point2 = branch(point=root_point, angle=angle_0, length=length_0)
# next_angle = angle_0 - 30
# next_length = length_0 * .75
# print(next_point1, next_point2)
# next_point1 = branch(point=next_point1, angle=next_angle, length=next_length)
#
# next_angle = next_angle - 30
#
# next_point1 = branch(point=next_point2, angle=next_angle+90, length=next_length)


# def branch(point1, point2, angle1, angle2,  length, delta):
#     if length < 10:
#         return
#     i = 0
#     while i < 3:
#         v1 = sd.get_vector(start_point=point1, angle=angle1, length=length, width=1)
#         v1.draw()
#         next_point1 = v1.end_point
#         next_angle1 = angle1 - delta
#         next_length = length * .75
#         v2 = sd.get_vector(start_point=point2, angle=angle2, length=length, width=1)
#         v2.draw()
#         next_point2 = v2.end_point
#         next_angle2 = angle2 + delta
#         branch(point1=next_point1, point2=next_point2, angle1=next_angle1, angle2=next_angle2, length=next_length, delta=delta)
#         i += 1
#     branch(point1=next_point1, point2=next_point2, angle1=next_angle1, angle2=next_angle2, length=next_length, delta=delta)
#
#
# delta = 30
# branch(point1=root_point, point2=root_point, angle1=90, angle2=90, length=150, delta=delta)
# for delta in range(-50, 1, 10):
#     branch(point=root_point, angle=90, length=150, delta=delta)
start_point = sd.get_point(300, 30)
angle1 = 60
angle2 = 120
length = 100


def draw_branches(point, angle1, length):
    if length < 2:
        return
    v1 = sd.get_vector(start_point=point, angle=angle1, length=length)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle1 - 30
    next_length = length * .75
    draw_branches(point=next_point, angle1=next_angle, length=next_length)
    v2 = sd.get_vector(start_point=point, angle=angle1 + 60, length=length)
    v2.draw()
    next_point = v2.end_point
    next_angle = angle1 + 30
    next_length = length * .75
    draw_branches(point=next_point, angle1=next_angle, length=next_length)


draw_branches(point=start_point, angle1=angle1, length=length)
# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
