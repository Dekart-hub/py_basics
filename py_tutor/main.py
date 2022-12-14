import math

SQRT5 = math.sqrt(5)  # square root of 5


def t5_5_ffind(s: str):
    """
    Task 5.5
    Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс. Если она встречается два
    и более раз, выведите индекс её первого и последнего появления.
    Если буква f в данной строке не встречается, ничего не выводите.
    :param s: входная строка
    :var cnt: кол-во вхождений 'f'
    :return: nothing
    """
    cnt = s.count('f')
    if cnt == 1:
        print(s.find('f'))
    elif cnt > 1:
        print(s.find('f'), ' ', s.rfind('f'))
    return None


def t5_6_ffind(s: str):
    """
    Task 5.6
    Дана строка. Найдите в этой строке второе вхождение буквы f, и выведите индекс этого вхождения.
    Если буква f в данной строке встречается только один раз, выведите число -1, а если не встречается ни разу,
    выведите число -2.
    :param s: входная строка
    :var cnt: кол-во вхождений 'f'
    :return ничего не возвращает
    """
    cnt = s.count('f')
    if cnt == 1:
        print("-1")
    elif cnt > 1:
        print(s.find('f', s.find('f') + 1))
    else:
        print("-2")
    return None


def t5_7_delsub(s: str):
    """
    Task 5.7
    Дана строка, в которой буква h встречается минимум два раза.
    Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.
    :param s: входная строка
    :return: возвращает изменённую строке
    """
    return s[0:s.find('h')] + s[s.rfind('h'):len(s)]


def t5_8_revsub(s: str):
    """
    Task 5.8
    Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов,
    заключенную между первым и последним появлением буквы h, в противоположном порядке.
    :param s: входная строка
    :var temp: для хранения части между 'h'
    :return: возвращает изменённую строке
    """
    temp = s[s.find('h'): s.rfind('h') + 1]
    s = s[:s.find('h')] + temp[::-1] + s[s.rfind('h') + 1:]
    return s


def t5_9_repl(s: str):
    """
    Task 5.9
    Дана строка. Замените в этой строке все цифры 1 на слово one.
    :param s: входная строка
    :return: возвращает изменённую строке
    """
    return s.replace('1', "one")


def t_5_10_remch(s: str, ch: chr):
    """
    Task 5.10
    Дана строка. Удалите из этой строки все символы заданные параметром.
    :param s: входная строка
    :param ch: символ для удаления
    :return: возвращает изменённую строке
    """
    return s.replace(ch, '')


def t_5_11_replsub(s: str):
    """
    Task 5.11
    Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
    :param s: символ для удаления
    :return: возвращает изменённую строке
    """
    return s[0:s.find('h') + 1] + s[s.find('h') + 1: s.rfind('h')].replace('h', 'H') + s[s.rfind('h'): len(s)]


def t_5_12_delevr3rd(s: str):
    """
    Task 5.12
    Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
    :param s: входная строка
    :return: возвращает изменённую строку2
    """
    for i in range(0, len(s), 3):
        j = i - i // 3
        s = s[0:j] + s[j + 1:len(s)]
    return s


def t8_5_rev():
    """
    Task 8.5
    Reverse a sequence of int from input stream
    :var number: считываемое число
    :return: nothing
    """
    number = int(input())
    if number != 0:
        t8_5_rev()
    print(number)
    return None


def t8_6_fib(n: int):
    """Task 8.6
    Calculate n Fibonacci number
    The way to solve this problem was chosen according to task.
    :param n: номер числа Фибоначчи
    :var f: фи из формулы замыкания рекурсии
    :return: возращает число Фибоначчи
    """
    f = (SQRT5 + 1) / 2
    return int(f ** n / SQRT5 + 0.5)

def t9_2_snoflake(n: int):
    """
    Task 9.2
    ано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "."
    (каждый элемент массива является строкой из одного символа). Затем заполните символами "*" среднюю строку массива,
    средний столбец массива, главную диагональ и побочную диагональ. В результате единицы в массиве должны образовывать
    изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.
    :param n: размерност матрицы
    :return: None
    """
    #Для облеггчения пониманияЮ происходящего в print(), вынес получающийся массив
    # arr = [[('.', '*')[(i == j) or (i == n-j-1) or (j == n // 2) or (i == n // 2)] for i in range(n)]for j in range(n)]

    print('\n'.join([' '.join([str(i) for i in row]) for row in [[('.', '*')[(i == j) or (i == n-j-1) or (j == n // 2) or (i == n // 2)] for i in range(n)]for j in range(n)]]))
    return None
