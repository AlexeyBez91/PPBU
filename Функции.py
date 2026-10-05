# def summator(a=10, b = 4):
    # print(a + b)
    # return a * b

# n = 45
# cc = 'qwerty'
# n = summator(2, 3)
# print('функция', n)
# print(summator(2)) # позиционный аргумент
# print(summator())
# print(summator(b=8)) # ключевые аргументы


def printing(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args)

print(printing())
print(printing(1, 3, nn=16, y=45))
printing('Name1', 'Name2')
