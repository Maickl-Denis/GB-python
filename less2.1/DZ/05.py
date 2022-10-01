# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
import random

num = int(input("Введите число: "))

first_list = []
result = []

for i in range(num):
    first_list.append(i)

print(first_list)

while first_list:
    result.append(first_list.pop(random.randint(0, len(first_list) - 1)))

print(result)
