# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a
# 1v2b2w2P3u2T1Y1y2W2Q

import os
def rle(file1: str, file2: str):
    path = f"{os.getcwd()}\\GB-python\\less5.1\\DZ\\{file1}"
    if os.path.exists(path):
        with open(path) as fl,\
                open(f"{os.getcwd()}\\GB-python\\less5.1\\DZ\\{file2}", 'w', encoding="utf-8") as fl2:
            for line in fl:
                result = ''
                one_item = line[0]
                count = 0

                for item in line.rstrip():
                    if item == one_item:
                        count += 1
                    else:
                        result += f"{count}{one_item}"
                        count = 1
                        one_item = item
                else:
                    result += f"{count}{one_item}"
                print(result.rstrip(), file=fl2)
    else:
        print(f"Файл для кодирования {file1} не обнаружен")


def rle_decod(file1: str, file2: str):
    path = f"{os.getcwd()}\\GB-python\\less5.1\\DZ\\{file1}"
    if os.path.exists(path):
        with open(path) as fl, \
                open(f"{os.getcwd()}\\GB-python\\less5.1\\DZ\\{file2}", 'w', encoding="utf-8") as fl2:
            for line in fl:
                result = ''
                num = ''
                for elem in line.rstrip():
                    if elem.isdigit():
                        num += elem
                        continue
                    if elem.isalpha():
                        result += f"{elem * int(num)}"
                        num = ''
                print(result, file=fl2)
    else:
        print(f"Файл для декодирования {file1} не обнаружен")

def menu():
    while True:
        num = input("1. Вы хотите закодировать файл\n"
                    "2. Вы хотите раскодировать файл\n"
                    "0. Выход\n")
        if num == "1":
            file1 = input("Введите имя файла с текстом: ")
            file2 = input("Введите имя файла для записи: ")
            rle(file1, file2)
        elif num == "2":
            file1 = input("Введите имя файла для декодирования: ")
            file2 = input("Введите имя файла для записи: ")
            rle_decod(file1, file2)
        elif num == "0":
            break

menu()
