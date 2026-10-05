# # Задача 1
# m = int(input())
# if m <= 2000:
#     print('SMALL')
# elif m <= 5000:
#     print('CARGO')
# else:
#     print('COURIER')

# Задача 2
# p = int(input('Есть пропуск? 1 - да, 0- нет: '))
# a = int(input('Есть тревога? 1 - да, 0 - нет: '))
# c = int(input('Уровень допуска: '))
# r = int(input('Требуемый уровень'))
# if a == 1:
#     print('LOCKDOWN')
# elif p == 0:
#     print('NO_PASS')
# elif r != c and c < r:
#     print('DENIED')
# else:
#     print('ACCESS')

# # Задача 3

# h = int(input('На сколько часов: '))
# d = int(input('Выходной?: '))
# s = int(input('Скидка: '))
# discount = 25
# if 1 <= h <= 2:
#     if d == 0:
#         rate = 80
#         x = rate
#     elif d == 1:
#         rate = 100
#         x = rate
#     if s == 0:
#         print(int(h * x))
#     elif s == 1:
#         z = h * x * discount / 100
#         print(int((h * x) - z))
# elif 3 <= h <= 5:
#     if d == 0:
#         rate = 60
#         x = rate
#     elif d == 1:
#         rate = 80
#         x = rate
#     if s == 0:
#         print(int(h * x))
#     elif s == 1:
#         z = h * x * discount / 100
#         print(int((h * x) - z))
# elif 6 <= h <= 24:
#     if d == 0:
#         rate = 40
#         x = rate
#     elif d == 1:
#         rate = 80
#         x = rate
#     if s == 0:
#         print(int(h * x))
#     elif s == 1:
#         z = h * x * discount / 100
#         print(int((h * x) - z))