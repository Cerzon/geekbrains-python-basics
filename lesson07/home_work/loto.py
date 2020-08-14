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


BARRELS_AMOUNT = 90
NUMS_PER_CARD = 15
ROWS_PER_CARD = 3
CELLS_PER_ROW = 9


class LotoCard:
    """
    Карточка лото с числами
    """
    def __init__(self, player):
        lst = []
        for barrel, remain in BarrelsBag(BARRELS_AMOUNT):
            lst.append(barrel)
            if BARRELS_AMOUNT - remain == NUMS_PER_CARD:
                break
        # rows = []
        self.card = []
        for i in range(ROWS_PER_CARD):
            row = sorted(lst[i::ROWS_PER_CARD])
            for _ in range(CELLS_PER_ROW - NUMS_PER_CARD // ROWS_PER_CARD):
            # for i in range(ROWS_PER_CARD):
                row.insert(randint(0, len(row)), ' ')
        # for i in range(ROWS_PER_CARD):
            self.card += row
        self.template = None
        self.player = player

    def __str__(self):
        if not self.template:
            cell_len = len(str(BARRELS_AMOUNT)) + 1
            card_header = '{:-^' + str(cell_len * CELLS_PER_ROW + 1) + '}\n'
            card_header = card_header.format(' Каторчка ' + self.player + ' ')
            row_body = ('{:>' + str(cell_len) + '}') * CELLS_PER_ROW + '\n'
            card_footer = '-' * (cell_len * CELLS_PER_ROW + 1)
            self.template = card_header + row_body * ROWS_PER_CARD + card_footer
        return self.template.format(*self.card)

    def check_number(self, number):
        return number in self.card

    def stroke_number(self, number):
        self.card[self.card.index(number)] = '-'

    def winner(self):
        return self.card.count('-') == NUMS_PER_CARD


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


class LotoGame:
    def __init__(self, gamer_card, pc_card, barrels_bag):
        self._gamer_card = gamer_card
        self._pc_card = pc_card
        self._barrels_bag = barrels_bag

    def start_game(self):
        for barrel, remain in self._barrels_bag:
            print('\nВыпал бочонок: {} (осталось {})'.format(barrel, remain))
            print(self._gamer_card)
            print(self._pc_card)
            answer = input('Зачеркнуть номер? [y/n] ')
            # проверка ответа мутировала сперва из-за переключения раскладки,
            # потом из-за лени и желания играть одной рукой на доп.клавиатуре
            if answer and answer.lower() in 'yн0':
                if self._gamer_card.check_number(barrel):
                    self._gamer_card.stroke_number(barrel)
                else:
                    print('\nВ вашей карточке нет такого номера. Вы проиграли.\n')
                    break
            elif self._gamer_card.check_number(barrel):
                print('\nСлепота куриная! Вы проиграли.\n')
                break
            if self._gamer_card.winner():
                print('\nПобеда {}.\n'.format(self._gamer_card.player))
                break
            if self._pc_card.check_number(barrel):
                self._pc_card.stroke_number(barrel)
            if self._pc_card.winner():
                print('\nПобеда {}.\n'.format(self._pc_card.player))
                break


if __name__ == '__main__':

    loto_game = LotoGame(
        LotoCard('игрока'),
        LotoCard('компьютера'),
        BarrelsBag(BARRELS_AMOUNT)
    )

    loto_game.start_game()