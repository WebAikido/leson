#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


tables_code = goods['Стол']
tables_item = store[tables_code][0]
tables_quantity1 = tables_item['quantity']
tables_price = tables_item['price']
tables_cost = tables_quantity1 * tables_price

tables_item = store[tables_code][1]
tables_quantity2 = tables_item['quantity']
tables_price = tables_item['price']
tables_cost += tables_quantity2 * tables_price
tables_total = tables_quantity1 + tables_quantity2
print('Столы - ', tables_total, 'шт, стоимость', tables_cost, 'руб')


sofa_code = goods['Диван']
sofa_item = store[sofa_code][0]
sofa_quantity1 = sofa_item['quantity']
sofa_price = sofa_item['price']
sofa_cost = sofa_quantity1 * sofa_price
sofa_item = store[sofa_code][1]
sofa_quantity2 = sofa_item['quantity']
sofa_price = sofa_item['price']
sofa_cost += sofa_quantity2 * sofa_price
sofa_total = sofa_quantity1 + sofa_quantity2
print('Диваны - ', sofa_total, 'шт, стоимость', sofa_cost, 'руб')

chair_code = goods['Стул']
chair_item = store[chair_code][0]
chair_quantity1 = chair_item['quantity']
chair_price = chair_item['price']
chair_cost = chair_quantity1 * chair_price

chair_item = store[chair_code][1]
chair_quantity2 = chair_item['quantity']
chair_price = chair_item['price']
chair_cost += chair_quantity2 * chair_price


chair_item = store[chair_code][2]
chair_quantity3 = chair_item['quantity']
chair_price = chair_item['price']
chair_cost += chair_quantity3 * chair_price
chair_total = chair_quantity1 + chair_quantity2 + chair_quantity3
print('Стул - ', chair_total, 'шт, стоимость', chair_cost, 'руб')


# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.
##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






