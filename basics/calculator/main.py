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
        result = a / b
    elif operation == '*':
        result = a * b
    return result


history = {
    '+': [],
    '-': [],
    '/': [],
    '*': []
}

while True:
    a, b = int(input()), int(input())
    operation = input()
    res = str(a) + str(operation) + str(b) + '=' + str(calc(a, b, operation))
    history[operation].append(res)
    print(res)
    for oper in history.keys():
        print(oper, history[oper])
