import os
import do
from logger import operation_logger as logg


def original(aktion: int):
    if aktion == 1:
        number1, number2 = data(aktion)
        do.sum(number1, number2)
    elif aktion == 2:
        number1, number2 = data(aktion)
        do.sub(number1, number2)
    elif aktion == 3:
        number1, number2 = data(aktion)
        do.mult(number1, number2)
    elif aktion == 4:
        number1, number2 = data(aktion)
        do.div(number1, number2)
    elif aktion == 5:
        number1, number2 = data(aktion)
        do.pow(number1, number2)
    elif aktion == 6:
        number1, number2 = data(aktion)
        do.div_compl(number1, number2)
    elif aktion == 7:
        number1, number2 = data(aktion)
        do.remainder_of_div(number1, number2)
    elif aktion == 8:
        number1, number2 = data(aktion)
        do.sqrt_pow(number1, number2)

def data(flag: int):
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        if flag <= 4 or flag == 6 or flag == 7:
            number1 = float(input("Введите первое число: "))
            number2 = float(input("Введите первое число: "))
        elif flag == 5 or flag == 8:
            number1 = float(input("Введите число: "))
            number2 = int(input("Введите степень: "))
    except:
        print("Вы ввели не допустимые символы")
        logg("warning", "введено не допустимое значение", "")
        input("Нажмите Enter для продолжения...")
        original(flag)

    else:
        return number1, number2
