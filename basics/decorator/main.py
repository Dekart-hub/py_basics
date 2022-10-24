def print_func(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            print(arg, ' ', end='')
        print()
        for key, value in kwargs.items():
            print(f"{key} = {value}", end=' ')
        print()
        return func(*args, **kwargs)
    return wrapper


@print_func
def find_sum(*args, **kwargs):
    local_sum = 0
    for arg in args:
        local_sum += arg
    return local_sum


find_sum(1, 2, 3, key="123")
