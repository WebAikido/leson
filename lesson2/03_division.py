# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 400, 37
x = a/b

print(x)
i = 0
while x:
    i += 1
    if i > x:
        x = i - 1
        print('Целочисленное деление', a, 'на', b, 'дает', x)
        break
