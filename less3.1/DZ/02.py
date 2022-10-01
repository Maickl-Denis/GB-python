# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

import random


def generaton_random_list(count):
    if count < 0:
        return "Все плохо"
    result = random.sample(range(count * 2), count)
    print(f"Был создан список длинной {count} с рандомными значениями: {result}")
    return result

def proizvedenie_par(ls):
    len_ls = int(len(ls)/2)
    for i in range(len_ls):
        ls[i] = ls[i] * ls.pop(-1)
    print(ls)

proizvedenie_par(generaton_random_list(int(input("Введите положительное число размера генерируемого списка: "))))