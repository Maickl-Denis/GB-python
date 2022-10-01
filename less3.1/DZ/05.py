# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

#
# F−1 = 1,
# F−2 = -1,
# Fn = F(n+2)−F(n+1).

def phib(n):
    f0 = 0
    f1 = 1
    i = 0
    while i < n:
        f1, f0 = f0 + f1, f1
        i += 1
    return f0


def neg_phib(n):
    f0 = 0
    f1 = 1
    i = 0
    while i < n:
        f1, f0 = f0 - f1, f1
        i += 1
    return f0


def list_phib(num):
    result = [0]
    for i in range(1, num + 1):
        result.append(phib(i))
        result.insert(0, neg_phib(i))
    return result


n = int(input("Введите число: "))
print(list_phib(n))
