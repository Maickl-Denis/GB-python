import random


# ls = [1, 2,3,4,5,6]
#
# print(random.choice(ls))
# print(random.sample(ls, 3))
#
#
#
# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.
# def magic(count, find_num2):
#     if count < 0:
#         return "Все плохо"
#     ls = random.sample(range(count * 2), count)
#     print(ls)
#
#     if find_num2 in ls:
#         return "Yes"
#     return "No"
#
#
# num1 = int(input("Введите число: "))
# num2 = int(input("Введите число: "))
# print(magic(num1, num2))

# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.

# def from_words_list(count, sourse):
#     ls=[]
#     for i in range(count):
#         ls.append("".join(random.choices(sourse, k=3)))
#     print(ls)
#     return ls
#
# def find_second_encounter(word, words_list):
#     if words_list.count(word) > 1:
#         first_encounter = words_list.index(word)
#         print(
#             f"второе вхождение: {words_list.index(word, first_encounter + 1)}")
#     else:
#         print("-1")
#
#
#
# gg = from_words_list(int(input("Введите число:")), input("Введите слово:"))
# find_second_encounter(input("Что ищем: "), gg)
