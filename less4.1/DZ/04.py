# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# in
# 0
# -1
# 4
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0
import random

num = int(input("Введите натуральную степень k: "))


def magit_to_file(num: int):
    if num != 0 and num > 0:
        with open('temp1.txt', "a", encoding="utf-8") as file:
            for i in reversed(range(1, num+1)):
                num1 = random.choice(range(5))
                if num1 == 0:
                    continue
                print(f"{num1}*x^{i} {random.choice(['+', '-'])}", file=file, end=" ")

            else:
                print(f"{num1} = 0", file=file)


magit_to_file(num)