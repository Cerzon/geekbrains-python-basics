__author__ = 'Ткаченко Кирилл Павлович'


# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    """
    Округляем дробную часть до указанного знака после запятой
    """
    fractional = (number % 1) * (10**ndigits)
    if fractional % 1 >= 0.5:
        fractional = int(fractional) + 1
    else:
        fractional = int(fractional)
    return int(number) + fractional / 10**ndigits


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    """
    Потрошим число на 6 цифр и сравниваем суммы первых и последних трёх
    """
    if ticket_number > 999999:
        return 'Некорректный номер для обработки'
    ticket_digits = [(ticket_number % 10**x) // 10**(x - 1) for x in range(1, 7)]
    return sum(ticket_digits[:3]) == sum(ticket_digits[3:])


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
