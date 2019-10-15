#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

from random import randint


barrels_amount = 90


class LotoCard:
    """
    Карточка лото с числами
    """
    def __init__(self, owner_name):
        lst = []
        for barrel, remain in BarrelsBag(barrels_amount):
            lst.append(barrel)
            if barrels_amount - remain == 15:
                break
        row1, row2, row3 = sorted(lst[::3]), sorted(lst[1::3]), sorted(lst[2::3])
        for _ in range(4):
            row1.insert(randint(0, len(row1)), ' ')
            row2.insert(randint(0, len(row2)), ' ')
            row3.insert(randint(0, len(row3)), ' ')
        self.card = row1 + row2 + row3
        self.template = None
        self.name = ' Карточка {} '.format(owner_name)

    def __str__(self):
        if not self.template:
            self.template = '{:-^28}\n' + ('{:>3}' * 9 + ' \n') * 3 + '-' * 28
        return self.template.format(self.name, *self.card)

    def check_number(self, number):
        return number in self.card

    def stroke_number(self, number):
        self.card[self.card.index(number)] = '-'

    def winner(self):
        return self.card.count('-') == 15


class BarrelsBag:
    """
    Мешок с заказным количеством бочонков
    """
    def __init__(self, amount):
        self.barrels = list(range(1, amount + 1))

    def __iter__(self):
        return self

    def __next__(self):
        remain = len(self.barrels)
        if remain == 0:
            raise StopIteration
        remain -= 1
        return self.barrels.pop(randint(0, remain)), remain


gamer_card = LotoCard('игрока')
pc_card = LotoCard('компьютера')

for barrel, remain in BarrelsBag(barrels_amount):
    print('\nВыпал бочонок: {} (осталось {})'.format(barrel, remain))
    print(gamer_card)
    print(pc_card)
    answer = input('Зачеркнуть номер? [y/n] ')
    # проверка ответа мутировала сперва из-за переключения раскладки,
    # потом из-за лени и желания играть одной рукой на доп.клавиатуре
    if answer and answer.lower() in 'yн0':
        if gamer_card.check_number(barrel):
            gamer_card.stroke_number(barrel)
        else:
            print('\nВ вашей карточке нет такого номера. Вы проиграли.\n')
            break
    elif gamer_card.check_number(barrel):
        print('\nСлепота куриная! Вы проиграли.\n')
        break
    if gamer_card.winner():
        print('\nПоздравляю! Вы выиграли!\n')
        break
    if pc_card.check_number(barrel):
        pc_card.stroke_number(barrel)
    if pc_card.winner():
        print('\nКомпьютер выиграл.\n')
        break