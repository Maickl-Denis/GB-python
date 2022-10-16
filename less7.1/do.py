from logger import operation_logger as logg


def div(a, b):
    if b:
        logg("successful", f'{a} / {b}', a / b)
        print(a / b)
        input("Нажмите Enter для продолжения...")
    else:
        logg("warning", "Деление на ноль", "")
        print("Деление на ноль может открыть черную дыру, мы не можем этого допустить")
        input("Нажмите Enter для продолжения...")


def mult(a, b):
    logg("successful", f'{a} * {b}', a * b)
    print(a * b)
    input("Нажмите Enter для продолжения...")


def sub(a, b):
    logg("successful", f'{a} - {b}', a - b)
    print(a - b)
    input("Нажмите Enter для продолжения...")


def sum(a, b):
    logg("successful", f'{a} + {b}', a + b)
    print(a + b)
    input("Нажмите Enter для продолжения...")


def div_compl(a, b):
    logg("successful", f'{a} // {b}', a // b)
    print(a // b)
    input("Нажмите Enter для продолжения...")


def pow(a, b):
    logg("successful", f'{a} ** {b}', a ** b)
    print(a ** b)
    input("Нажмите Enter для продолжения...")


def remainder_of_div(a, b):
    logg("successful", f'{a} % {b}', a % b)
    print(a % b)
    input("Нажмите Enter для продолжения...")


def sqrt_pow(a, b):
    if b:
        logg("successful", f'{a} sqrt^{b}', f"{(a ** (1/b)):.2f}")
        print(f"{(a ** (1/b)):.2f}")
        input("Нажмите Enter для продолжения...")
    else:
        logg("warning", "Корень со степьнью 0", "")
        print("Получения корня в 0 степени вызывет вторжение инопланетян, так что извените мы не готовы на это")
        input("Нажмите Enter для продолжения...")
