# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код
snowflake_data = [[120, 500], [40, 500], [270, 500], [100, 500], [140, 500], [290, 500], [430, 500], [370, 500]]


def drawing_snowflakes(x, y):
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=lenght)




lenght = sd.random_number(10, 40)

while True:
    sd.clear_screen()
    for x, y in snowflake_data:
        drawing_snowflakes(x=x, y=y)
    for i in snowflake_data:
        i[1] -= 10
        if i[1] < 50:
            break
        i[0] += 10
    sd.sleep(0.1)
    if sd.user_want_exit():
        break



sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


