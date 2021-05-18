# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

# TODO здесь ваш код

import room_1
import room_2

for i in room_1.folks:
    print('В комнате',room_1, 'живут:', i)

for i in room_2.folks:
    print('В комнате room_1 живут:', i)