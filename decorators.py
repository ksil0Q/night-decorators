import time


# декоратор на время
def dec(func):
    def wrapper(*args, **kwargs):
        print('func starts')
        start = time.time()
        val = func(*args, **kwargs)
        print(f'func stopped at {time.time() - start}')
        return val
    return wrapper


@dec
def worker(a: float):
    print('working...')
    time.sleep(a)
    return 'a'

print(worker(3.0))


# декоратор с параметрами
def mul(multiplier):
    def dec(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * multiplier
        return wrapper
    return dec


@mul(4)
def worker(a, b):
    return a + b

print(worker(1, 2))


# логирующий декоратор
from functools import wraps


def log(func):
    @wraps(func) # встроенный декоратор чтоб проуинуть внутрь инфу(__name__, __docs__ итд), без него инфа о функции будет как при вызове wrapper
    def wrapper(*args, **kwargs):
        print(f'Called func with name: {func.__name__};\n'
              f' docs:{func.__doc__};\n'
              f' and args: {", ".join(str(arg) for arg in args)};\n'
              f' result: {func(*args, **kwargs)}')

    return wrapper


@log
def worker(a, b):
    """some docs"""
    return a + b


print(worker(1, 2))
print(worker.__doc__)
print(worker.__name__)
