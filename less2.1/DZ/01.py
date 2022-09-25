# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

from decimal import Decimal

num = input("Введите число: ")
sum = 0
if num.isdigit():
    print(f"Вы ввели целое число {num} -> сумма элементов ", end='')
    while int(num):
        sum += int(num) % 10
        num = int(num) // 10
    print(sum)
else:
    try:
        float(num)
        print(f"Вы ввели дробное число {num} -> сумма элементов ", end='')
        dot_num = (Decimal(num)).as_tuple().exponent * (-1)
        num = float(num) * (10 ** dot_num)
        while int(num):
            sum += int(num) % 10
            num = int(num) // 10
        print(sum)
    except ValueError:
        print("что то пошло не так")

