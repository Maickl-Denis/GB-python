# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]


num = input("Введите число: ")

factorial = 1
result = []
if num.isdigit() and int(num) != 0:
    for i in range(2, int(num) + 1):
        result.append(factorial)
        factorial *= i
    else:
        result.append(factorial)
    print(f"{num} -> {result}")
else:
    print("Все плохо, делай заного")