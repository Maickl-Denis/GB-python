# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36
import random
from math import modf


def generaton_random_float_list(cnt):
    result = []
    for i in range(cnt):
        result.append((round(random.uniform(0, 10), 2)))
    print(f"Был создан список длинной с рандомными значениями: {result}")
    return result


def raznica_float(lst):
    result = []
    for num in lst:
        result.append(round(float(num % 1), 2))
    print(f"Min: {min(result)}, Max: {max(result)}. Difference: {max(result) - min(result)}")


raznica_float(generaton_random_float_list(int(input("Введите размер списка: "))))
