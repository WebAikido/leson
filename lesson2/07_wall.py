# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
y1 = 0
y2 = 50


for z in range(7):
    x1 = -50
    x2 = 50
    for x in range(2):
        for _ in range(7):
            left_bottom = sd.get_point(x1, y1)
            right_top = sd.get_point(x2, y2)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_BLUE, width=0)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_RED, width=1)
            x1 += 100
            x2 += 100
        y1 += 50
        y2 += 50
        x1 = 0
        x2 = 100
    y1 += 0
    y2 += 0

sd.pause()
