"""list"""
import copy

'''Список - упорядоченный набор объектов'''

# '''     0   1   2   3   4   '''
# num = [22, 33, 44, 55, 99]
# '''    -5  -4  -3  -2  -1   '''
#
# print(num[0])
# print(num[2])
# print(num[1:-2]) # Срез (первое число всегда 0, последнее -1 и не важно сколько чисел в строке)
# print(num[::2]) # Полный срез с шагом "2"
# print(num[2:]) # Срез, начиная с "2"
# print(num[2::-1]) # Начинаем с "2" и обратный шаг
# print(num[::-1]) # обратный полный шаг
#
# nn = num
# num[1] = 3333
# print(num, id(num))
# print(nn, id(nn))
# print(nn is num)

# num = [1, 2, [32, 4]]

# nn = num.copy()
# nn = copy.deepcopy(num) # глубокое копирование списка / делает новый список для корректировки
# num[1] = 3333
# num[-1][1] = 400
# print(num, id(num))
# print(nn, id(nn))
# print(nn is num)

# num = [22, 33, 44, 55, 99]
# print(num)
# num.append(100) # добавляет в конец списка 100
# print(num)
# num.insert(2, 300) # добавляет в указаную точку (на 2) списка "300"
# print(num)
# num.extend([1, 2]) # позволяет к одному списку присоеденить другой список
# num += [3, 4] # как и extend
# num = num + [1, 2] # не как предыдущие, это другое
# print(num)

# num.pop() # удаление переменной из списка
# print(num)
#
# n = num.pop()
# nn = num.pop(0) # удаление конкретной переменной
# print(n)
# print(nn)
# print(num)

# num = [22, 100, 44, 100, 99, 100, 100]
# print(num)
# while 100 in num: # удаляет все "100" из списка
#     num.remove(100)
# print(num)
# print(num.index(100))
# print(num.count(100)) # сколько раз "100" в списке?
# num.clear() # очищяет весь список
# print(num)

# num = [22, 33, 44, 55, 99, 11]
# print(num)
# for i in range(len(num)):
#     print(i, num[i], end='   ') # узнаем индекс объекта по списку
# print()
# cnt = 0
# for i in num:
#     print(cnt, i, end='   ')  # узнаем индекс, но через "cnt"
#     cnt += 1
# print()
#
# for i in enumerate(num):
#     print(i, end='   ')  # узнаем индекс через кортеж
# print()

""" Кортеж (Tuple) """
''' Кортеж - упорядоченный набор неизменяемых объектов '''
''' Его можно так же моделировать, кроме как изменять заданный список '''

# tp = [22, 33, 44, 99]
# # k = 7, # " , " после 7 - обязательна для того, чтобы питон понял - это кортеж!
# k, i, z = 7, 5, 9 # раздать число каждой переменной
# print(k, i, z)
# k, *i, z = 7, 5, 9, 10, 1, 32, 56, 100
# print(k, i, z)
# k, *i, z = 7, 5, 9, 10, 1, 32, 56, 100
# print(k, *i, z)
# k, i, *z = 7, 5, 9, 10, 1, 32, 56, 100
# print(k, i, z)

# names = ['Dasha', 'Masha', 'Sasha', 'Glasha', 'Andre']
# # names.reverse()
# names.sort() # сортировка по порядку () / по обратному порядку через (reverse=True)
# # print(names)
# for k, i in enumerate(names, 1):
#     print(f'{k}. {i}')
#
# for i in zip(names, num): # zip - для взятия данных из разных списков/кортежей
#     print(i)

# arr = [0] * 10  # получение списка из 10 "0" и заполнение списка
# print(arr)
# for i in range(len(arr)):
#     arr[i] = i + 1
# print(arr)
# ls = [] # заполнение списка, начиная с пустого списка - так лучше чем в 1 варианте!
# for i in range(10):
#     ls.append(i + 1)
# print(ls)
# print (5 if len(ls) > 7 else 125)
# ls = [i + 1 for i in range(10)] # заполнение списка, намного быстрее чем предыдущие - это называется 'list comprehention'
# print(ls)
# ls = [i + 1 for i in range(10) if i > 4]
# print(ls)
# ls = [i + 1 if (i + 1) % 2 == 0 else i for i in range(10) if i > 1]
# print(ls)

# tp = (22, 33, 44, 55, 99)
# k, i, *z = 7, 5, 9, 10, 1, 32, 56, 100
# print(k, i, z)
# tp = ('login', 'password')
# print(tp)
# buf = list(tp)
# buf[-1] = 'new_password'
# tp = tuple(buf)
# print(tp)

""" левый циклический сдвиг"""
# a = [22, 33, 44, 55, 99]
# temp = a[0] # через алгоритм
# n = len(a)
# for i in range(n - 1):
#     a[i] = a[i + 1]
# a[-1] = temp
# print(a)
#
# temp = a.pop(0) # быстрый способ (не всегда получится им решить задачу)
# a.append(temp)
# print(a)

# x = 10
# y = 15
# print(x, y)
# z = x
# x = y
# y = z
# print(x, y)
# x, y = y, x
# print(x, y)

# names = ('Dasha', 'Masha', 'Sasha', 'Glasha', 'Andre')
# age = (22, 33, 44, 55, 11)
# persones = [('Dasha', 22), ('Masha', 33), ('Sasha', 44), ('Glasha', 55), ('Andre', 11)] # для понимания - расписываем
#
# for r, (n, a) in enumerate(zip(names, age), 1): # 1 ставиться для отсчета с 1
#     print(f'{r}. {n} - {a}')

