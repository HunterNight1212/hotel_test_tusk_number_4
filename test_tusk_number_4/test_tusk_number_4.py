def print_table(size=int(input('введите диапазон таблицы:'))):
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print(f'{i * j:4}', end='')
        print()
print_table()
