import random
# # 1. Создайте список из N натуральных чисел(0 до N),
# #    упорядоченных по возрастанию. Среди чисел не хватает
# #    одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# #    Найдите это число.
#
#
# N = int(input("Введите число: "))
#
#
# def generaton_random_list(count: int) -> list:
#     if count < 0:
#         print("Все плохо")
#         return result
#     result = [x for x in range(count + 1)]
#     result.remove(random.choice(result))
#     print(f"Был создан список длинной {count} с рандомными значениями: {result}")
#     return result
#
#
# def chech_nem(ar: list):
#     for i in range(1, len(ar)):
#         if ar[i] - 1 != ar[i - 1]:
#             return ar[i] - 1
#     return -1
#
#
# print(chech_nem(generaton_random_list(N)))
#########################################################
# 2. Создайте список, в который попадают числа,
#    описывающие возрастающую последовательность.
#    Порядок элементов менять нельзя.

#
# def generaton_random_list(count: int) -> list:
#     result = []
#     if count < 0:
#         print("Все плохо")
#         return result
#     for num in range(count):
#         result.append(random.choice(range(10)))
#     print(f"Был создан список длинной {count} с рандомными значениями: {result}")
#     return result
#
# def magix(arr: list):
#     result = []
#     for i in range(len(arr)):
#         flag = arr[i]
#         zero_ar = [flag]
#         for y in range(i, len(arr)):
#             if arr[y] > flag:
#                 zero_ar.append(arr[y])
#                 flag = arr[y]
#
#
#         if len(zero_ar)>1:
#             result.append(zero_ar)
#     return result
#
# N = int(input("Введите число: "))
#
# print(magix(generaton_random_list(N)))