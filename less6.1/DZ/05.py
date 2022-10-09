# 5. Реализовть функцию, возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трех списков (по одному из каждого)
import random


def comik_randomizer(count: int, unic=False) -> list:
    node1 = ["автомобиль", "лес", "огонь", "город", "дом"]
    node2 = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    node3 = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if unic:
        result = []

        try:
            for i in range(count):
                result.append(f"{node1.pop(random.randint(0, len(node1) - 1))} "
                              f"{node2.pop(random.randint(0, len(node2) - 1))} "
                              f"{node3.pop(random.randint(0, len(node3) - 1))}")
        except ValueError:
            print("Мы не можем сделать так много уникальных шуток")

        return result
    else:
        return [f"{random.choice(node1)} {random.choice(node2)} {random.choice(node3)}"
                for i in range(count)]


print(comik_randomizer(10, unic=True))
print(comik_randomizer(10))
