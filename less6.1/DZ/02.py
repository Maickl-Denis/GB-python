# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

def krat(num: int) -> list:
    return [x for x in range(20, num + 1) if x % 20 == 0 or x % 21 == 0]


print(krat(int(input("Введите число: "))))
