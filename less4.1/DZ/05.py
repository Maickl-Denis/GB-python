# 5. ** Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
# in
# "temp.txt"
# "temp1.txt"
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
#
# in
# "poly.txt"
# "poly_2.txt"
#
# out
# The contents of the files do not match!


def union_file():
    union_f = open('union_file.txt', "w", encoding="utf-8")
    file1 = open('temp.txt')
    file2 = open('temp1.txt')

    ln = len(file1.readlines())
    file1.seek(0)
    if len(file1.readlines()) != len(file2.readlines()):
        print("The contents of the files do not match!")
    else:
        file1.seek(0)
        file2.seek(0)
        for i in range(ln):
            print(f"{file1.readline()[:-4]}+ {file2.readline()}", file=union_f, end='')


union_file()
