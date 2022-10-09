# 3. Написать функцию, аргументы -имена сотрудников, возвращает словарь, цлючи - первые буквы имен,
# значения - списки, содержащие имена, начинающиеся с соответствующей буквы

lines = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]


def FIO(lines: list) -> dict:
    result = {}
    for name in lines:
        if name[0] not in result:
            result[name[0]] = [name]
        else:
            result[name[0]].append(name)
    return result


def sort(rs):
    for key in sorted(rs):
        print(key, '=>', rs[key])


sort(FIO(lines))
