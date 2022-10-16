import menu
from logger import operation_logger as logg


if __name__ == '__main__':
    try:
        menu.menu()
    except:
        logg("CRASH", "что то сильно сломалось но мы не понимаем что", "но мы продолжаем работать")
        menu.menu()
