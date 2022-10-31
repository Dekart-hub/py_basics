inp = input().split(' ')
try:
    list_inp = [int(inp[i]) for i in range(len(inp))]
except ValueError:
    print(-1)
    exit(2)

list_odd_ls = [i for i in list_inp if i % 2 == 0]
list_even_ls = [i for i in list_inp if i % 2 != 0]
list_less0_ls = [i for i in list_inp if i < 0]

print("Списковые выражения")
print("Чётные: ", list_odd_ls)
print("Нечётные: ", list_even_ls)
print("Меньше 0: ", list_less0_ls)

list_odd = list(filter(lambda x: x % 2 == 0, list_inp))
list_even = list(filter(lambda x: x % 2 != 0, list_inp))
list_less0 = list(filter(lambda x: x < 0, list_inp))

print("Функции")
print("Чётные: ", list_odd)
print("Нечётные: ", list_even)
print("Меньше 0: ", list_less0)
