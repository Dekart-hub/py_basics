def calc(a, b: int, operation: str):
    """
    Функция выполняет арифметическое действие переданное в параметре над переданными в парамметре числами
    :param a: первое число
    :param b: второе число
    :param operation: операция
    :return: результат действияя
    """
    result = 0
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '/':
        if b != 0:
            result = a / b
        else:
            result = "error"
    elif operation == '*':
        result = a * b
    return result


history = {
    '+': [],
    '-': [],
    '/': [],
    '*': []
}

OPERATORS = ('+', '-', '/', '*')

while True:
    try:
        a, b, operation = int(input()), int(input()), input()
    except:
        print("Inappropriate usage, try again")
        continue
    if operation not in OPERATORS:
        print("Unknown operation, try again")
        continue
    res = str(a) + str(operation) + str(b) + '=' + str(calc(a, b, operation))
    history[operation].append(res)
    print(res)
    for operation in history.keys():
        print(operation, history[operation])
