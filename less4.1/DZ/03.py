# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]
import random


def generaton_random_list(count: int) -> list:
    result = []
    if count < 0:
        print("Все плохо")
        return result
    for num in range(count):
        result.append(random.choice(range(10)))
    print(f"Был создан список длинной {count} с рандомными значениями: {result}")
    return result


def unic_num(ls: list) -> list:
    result = []
    for elem in ls:
        if not ls.count(elem) > 1:
            result.append(elem)
    return result

print(f"В массиве имеются следующие не повторяющиеся элементы: "
      f"{unic_num(generaton_random_list(int(input('Введите длину массива: '))))}")
