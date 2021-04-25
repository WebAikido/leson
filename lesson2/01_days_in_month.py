# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
def mont():
    user_input = input("Введите, пожалуйста, номер месяца: ")
    month_user = int(user_input)
    print('Вы ввели', month_user)
    return month_user


month_day = [('January', 31), ('February', 28), ('March', 31), ('April', 30), ('May', 31), ('June', 30), ('July', 31),
            ('August', 31), ('September', 30), ('October', 31), ('November', 30), ('December', 31)]

month_user = mont()
if 1 <= month_user <= 12:
    x = month_user-1
    print('Вы выбрали месяц', month_day[x][0], 'в нем ', month_day[x][1], 'дней!')
else:
    print(month_user, 'Тако месяца не существует выберите месяц от 1 до 12')
    mont()
