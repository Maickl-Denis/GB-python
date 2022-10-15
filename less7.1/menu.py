import os
import Rational
import komplex

def menu() -> int:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        numbers = numeric()
        if numbers == 0:
            break
        elif numbers == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            akt = action(numbers)
            if akt == 0:
                continue
            elif 0 < akt < 9:
                Rational.original(akt)
            else:
                print("Такого пункта меню нет")
        elif numbers == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            akt = action(numbers)
            if akt == 0:
                continue
            elif 0 < akt < 8:
                komplex.original(akt)
            else:
                print("Такого пункта меню нет")
        else:
            print("Такого пункта меню нет")


def numeric():
    try:
        che = int(input("Выберите работу с числами: \n"
                        "1. Обычные числа\n"
                        "2. Комплексные\n"
                        "0. Выход\n"))        
    except ValueError:
        print("Вы ввели некоректное значение")
        return 0
    else:
        return che
        

def action(flag: int):
    try:
        if flag == 1:
            act = int(input("Выберите действие: \n"
                            "1. Сложение\n"
                            "2. Вычитание\n"
                            "3. Умножение\n"
                            "4. Деление\n"
                            "5. Ввозведение в степень\n"
                            "6. Деление на целое\n"
                            "7. Остаток от деления\n"
                            "8. Корень числа со степенью\n"
                            "0. Выход\n"))
        else:
            act = int(input("Выберите действие: \n"
                            "1. Сложение\n"
                            "2. Вычитание\n"
                            "3. Умножение\n"
                            "4. Деление\n"
                            "5. Ввозведение в степень\n"
                            "0. Выход\n"))
    except ValueError:
        print("Вы ввели некоректное значение")
        return 0
    else:
        return act
