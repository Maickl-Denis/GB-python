# * 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15
num1 = int(input("Position one: "))
num2 = int(input("Position two: "))
NElem = int(input("Number of elements: "))

ls = [i for i in range(-NElem, NElem + 1)]

if 0 < num1 <= NElem * 2 + 1 and 0 < num2 <= NElem * 2 + 1:
    print(ls)
    print(f"{ls[num1 - 1]} * {ls[num2 - 1]} = {ls[num1 - 1] * ls[num2 - 1]}")
else:
    print("Вы вышли из диапазона")
