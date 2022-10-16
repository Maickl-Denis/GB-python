import os
import do
from logger import operation_logger as logg


def original(aktion: int):
    if aktion == 1:
        number1, number2 = data(aktion)
        do.sum(number1, number2)
    if aktion == 2:
        number1, number2 = data(aktion)
        do.sub(number1, number2)
    if aktion == 3:
        number1, number2 = data(aktion)
        do.mult(number1, number2)
    if aktion == 4:
        number1, number2 = data(aktion)
        do.div(number1, number2)
    if aktion == 5:
        number1, number2 = data(aktion)
        do.pow(number1, number2)

def data(flag: int):
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        if flag <= 4:
            number1 = complex(float(input("Введите для первого комплексного числа первое значение: ")), 
                              float(input("Введите для первого комплексного числа второе значение: ")))

            number2 = complex(float(input("Введите для второго комплексного числа первое значение: ")), 
                              float(input("Введите для второго комплексного числа второе значение: ")))
        elif flag == 5:
            number1 = complex(float(input("Введите для первого комплексного числа первое значение: ")), 
                              float(input("Введите для первого комплексного числа второе значение: ")))
            number2 = int(input("Введите степень: "))
    except:
        print("Вы ввели не допустимые символы")
        logg("warning", "введено не допустимое значение", "")
        input("Нажмите Enter для продолжения...")
        original(flag)
    else:
        return number1, number2
