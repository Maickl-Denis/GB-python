# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которого больше предыдущего элемента. Use comprehension.
# in
# >>10
# out
# >> [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# >> [24, 15, 23, 25]
import random


def generaton_random_list() -> list:
    return [random.randrange(25) for x in range(int(input("Введите длинну генерируемого списка: ")))]


def magik() -> list:
    ls = generaton_random_list()
    print(ls)
    return [ls[x] for x in range(1, len(ls)) if ls[x] > ls[x - 1]]


print(magik())
