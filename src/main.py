from chat import Chat
from time import time
from math import ceil
from util.math import carpet
from util.console import flush

if __name__ == '__main__':
    chat = Chat()

    total = 0
    while total < 1: 
        start = time()
        cost = chat.waste(n = 8000)
        finish = time()
        total += cost
        duration = finish - start
        remaining = ceil((1 - total) / cost * duration)
        
        flush()
        print(f'total: ${carpet(total, 4)} | remaining: {carpet(remaining, 2)}s')
    print('Completed!')