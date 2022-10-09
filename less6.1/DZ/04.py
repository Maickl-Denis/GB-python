lines = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
         "Борис Аркадьев", "Антон Серов", "Павел Анисимов"]


def FIO(lines: list) -> dict:
    result = {}
    for fio in lines:
        name, second_name = str(fio).split()
        if second_name[0] in result:
            if name[0] in result[second_name[0]]:
                result[second_name[0]][name[0]].append(str(fio))
            else:
                result[second_name[0]][name[0]] = [fio]
        else:
            result[second_name[0]] = {name[0]: [fio]}
    return result


def sort(rs):
    ks = list(rs.keys())
    ks.sort()
    for key in ks:
        print(key, '=>', rs[key])


sort(FIO(lines))
