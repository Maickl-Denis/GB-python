# # 1. Задайте строку из набора чисел. Напишите программу,
# # которая покажет большее и меньшее число.
# # В качестве символа-разделителя используйте пробел.


# from unittest import result


# def magic(ls: list):
#     result_list = []
#     for data in ls:
#         num = ''
#         if data.replace("-", "").isdigit():
#             num = data
#         else:
#             for w in data:
#                 if w.replace("-", "").isdigit():
#                     num += w
#         result_list.append(num)
#     return result_list


# def  min_sum(val):
#     art = magic(val)

#     if art:
#         return min(art, key=int), max(art, key=int)
#     else:
#         return []

# in_data = input("Введите списко цифр: ").split()


# print(min_sum(in_data))



# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
# с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
# Уравнения и корни запишите в файл.

# from math import sqrt

# a = float(input("Введите коофецент 'a': "))
# b = float(input("Введите коофецент 'b': "))
# c = float(input("Введите коофецент 'c': "))

# d = b ** 2 - 4 * a * c

# with open('temp.txt', 'a', encoding="utf-8") as file:
#     # file.write(f"Уравнение: {a}*x^2 + {b}*x + {c}\n")
#     print(f"Уравнение: {a}*x^2 + {b}*x + {c}", file=file)
#     if d > 0 and a:
#         x1 = (-b + sqrt(d)) / (2 * a)
#         x2 = (-b - sqrt(d)) / (2 * a)
#         file.write(f"Корни уравнения: {x1, x2}\n")
#     elif int(d) == 0:
#         x = (-b) / (2 * a)
#         file.write(f"Единственный корень: {x}\n")
#     else:
#         file.write("Корней нет")



# 3. Задайте два числа. Напишите программу, которая найдёт
# НОК (наименьшее общее кратное) этих двух чисел.
# from math import gcd


# def magix(n1, n2):
#     return int((n1 * n2) / gcd(n1, n2))


# num1 = int(input("Введите число 1: "))
# num2 = int(input("Введите число 2: "))

# print(magix(num1, num2))
