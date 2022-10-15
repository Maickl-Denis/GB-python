from logger import operation_logger as logg

def div(a, b):
    logg(f'{a} / {b}', a / b)
    print (a / b)
    input()


def mult(a, b):
    logg(f'{a} * {b}', a * b)
    print (a * b)
    input()

def sub(a, b):
    logg(f'{a} - {b}', a - b)
    print (a - b)
    input("Нажмите Enter для продолжения...")

def sum(a, b):
    logg(f'{a} + {b}', a + b)
    print (a + b)
    input("Нажмите Enter для продолжения...")

def div_compl(a, b):
    logg(f'{a} // {b}', a // b)
    print (a // b)
    input("Нажмите Enter для продолжения...")

def pow(a, b):
    logg(f'{a} ** {b}', a ** b)
    print (a ** b)
    input("Нажмите Enter для продолжения...")

def remainder_of_div(a, b):
    logg(f'{a} % {b}', a % b)
    print (a%b)
    input("Нажмите Enter для продолжения...")

def sqrt_pow(a, b):
    logg(f'{a} sqrt^{b}',f"{(a ** (1/b)):.2f}")
    print (f"{(a ** (1/b)):.2f}")
    input("Нажмите Enter для продолжения...")