from datetime import datetime
from time import time

def operation_logger(data, result):
    time = datetime.now().strftime('%d.%m.%y %H:%M')
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{time} - Operation: {data} = {result}\n')



