# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# x1 = 50
# y1 = 50
# x2 = 350
# y2 = 450
# x = 0
# for _ in range(7):
#     start_point = sd.get_point(x1, y1)
#     end_point = sd.get_point(x2, y2)
#     sd.line(start_point=start_point, end_point=end_point, color=rainbow_colors[x], width=4)
#     x += 1
#     x1 += 5
#     x2 += 5


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
x = 300
y = 0
color = 0
for _ in range(7):
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=400, color=rainbow_colors[color], width=10)
    color += 1
    y += 11
sd.pause()
