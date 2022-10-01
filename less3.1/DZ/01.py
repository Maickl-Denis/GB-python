# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

import random


def generaton_random_list(count):
    if count < 0:
        return "Все плохо"
    result = random.sample(range(count * 2), count)
    print(f"Был создан список длинной {count} с рандомными значениями: {result}")
    return result


def sum_element(ls):
    sum = 0
    for i in ls[::2]:
        sum += i
    print(f"Сумма элементов стоящих на нечетных позициях = {sum}")

sum_element(generaton_random_list(int(input("Введите положительное число размера генерируемого списка: "))))
