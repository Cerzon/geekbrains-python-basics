from random import randint


class LotoCard:
    def __init__(self, gamer=True):
        lst = []
        while len(lst) < 15:
            num = randint(1, 90)
            if not num in lst:
                lst.append(num)
        row1, row2, row3 = sorted(lst[::3]), sorted(lst[1::3]), sorted(lst[2::3])
        for _ in range(4):
            row1.insert(randint(0, len(row1)), ' ')
            row2.insert(randint(0, len(row2)), ' ')
            row3.insert(randint(0, len(row3)), ' ')
        self.card = row1 + row2 + row3
        if gamer:
            self.name = ' Ваша карточка '
        else:
            self.name = ' Карточка компьютера '

    def __str__(self):
        return ('{:-^27}\n' + ('{:>3}' * 9 + '\n') * 3 + '-' * 27).format(self.name, *self.card)

    def check_number(self, number):
        return number in self.card

    def stroke_number(self, number):
        self.card[self.card.index(number)] = '-'

    def winner(self):
        return self.card.count('-') == 15


class BarrelsBag:
    def __init__(self):
        self.barrels = list(range(1, 91))

    def __iter__(self):
        return self

    def __next__(self):
        remain = len(self.barrels)
        if remain == 0:
            raise StopIteration
        return self.barrels.pop(randint(0, remain - 1)), remain - 1


gamer_card = LotoCard()
pc_card = LotoCard(False)

for barrel, remain in BarrelsBag():
    print('\nВыпал бочёнок: {} (осталось {})'.format(barrel, remain))
    print(gamer_card)
    print(pc_card)
    answer = input('Зачеркнуть номер? [y/n] ')
    if answer.lower() == 'y':
        if gamer_card.check_number(barrel):
            gamer_card.stroke_number(barrel)
        else:
            print('\nДа вы охуели, нет такого номера на карточке!\nПроигрыш за самонадеянность.\n')
            break
    elif gamer_card.check_number(barrel):
        print('\nСлепота куриная! Всё, однозначный проигрыш.\n')
        break
    if gamer_card.winner():
        print('\nПоздравляю, Вы выиграли!\n')
        break
    if pc_card.check_number(barrel):
        pc_card.stroke_number(barrel)
    if pc_card.winner():
        print('\nВы всё проебали, компьютер победил.\n')
        break