# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
Ax = int(input("введите координаты точи Ax: "))
Ay = int(input("введите координаты точи Ay: "))
Bx = int(input("введите координаты точи Bx: "))
By = int(input("введите координаты точи By: "))

print(f"{(((Ax - Bx) ** 2)+((Ay - By) ** 2))**0.5:.2f}")
