import os
from datetime import datetime
from functools import wraps

def logger(path):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {func.__name__} called\n')
            return result
        return wrapper
    return decorator

@logger('hw.log')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    hello_world()
    print("Лог создан! Проверь hw.log")