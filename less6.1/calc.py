# 1. Напишите программу вычисления арифметического
#    выражения заданного строкой. Используйте операции +,-,/,*
#    приоритет операций стандартный. Добавьте скобки, приоритет операций меняется.

# st = input()
#
# eval(f"print({st})")
# exec(f"print({st})")


# def f(inp):
#     res = []
#     n = 0
#     for i in range(len(inp)):
#         if inp[i] in ("+", "-", "*", "/"):
#             res.append(int(inp[n:i]))
#             res.append(inp[i])
#             n = i + 1
#     res.append(int(inp[i:]))
#
#     return res
#
# print(f("12+78*2"))

from operator import add, sub, mul, truediv

def logic_prog():
    user_input = input("Введите пример без скобок: ")
    data = parse(user_input)
    result = calculate(data)
    print(f'Результат вычислений {result:.2f}')


def operation(a: float, op: str, b: float) -> float:
    operators = {'+': add, '-': sub, '*': mul, '/': truediv}
    callback = operators.get(op)
    if not callback:
        raise ArithmeticError('operator unknown')
    return round(callback(a, b), 2)


def calculate(lst: list) -> float:
    result = 0.0
    for s in '*/+-':
        while s in lst:
            index = lst.index(s)
            result = operation(lst[index - 1], s, lst[index + 1])
            lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result


def parse(s: str) -> list:
    result = []
    digit = ""
    for symbol in s:
        if symbol.isdigit() or symbol == '.':
            digit += symbol
        elif symbol in ['(', ')']:
            if digit:
                result.append(float(digit))
                digit = ""
            result.append(symbol)
        else:
            if digit:
                result.append(float(digit))
            digit = ""
            result.append(symbol)
    else:
        if digit:
            result.append(float(digit))
    return result

logic_prog()
