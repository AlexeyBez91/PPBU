# i = 0
# while i<10:
#     i += 1 # i = i + 1
#     print(i, end=' ')


# i = 0
# while i < 10:
#     i += 1
#     if i == 7:
#         continue # убирает 7 из цикла
#     print(i, end=' ')
# print()


# i = 0
# while i < 10:
#     i += 1
#     if i == 7:
#         break # прерывает цикл на 7
#     print(i, end=' ')


i = 0
while i < 10:
    i += 1
    if i == 17:
        break # прерывает цикл
    print(i, end=' ')
else:
    print('\nOK')


# n = int(input('Введите: '))
# sm = 0
# cnt = 0
# while n != 0:
#     sm += n
#     cnt += 1
#     n = int(input('Введите: '))
# print(f'Сумма - {sm}\n'
#       f' Кол-во - {cnt}')


'''
    s = 3 + 2 + 1
    k = 1 + 1 + 1
123 % 10 = 3
   // 10 = 12 % 10 = 2
             // 10 = 1 % 10 = 1
                      // 10 = 0
'''

# n = int(input('Введите: '))
# nn = n
# sm = 0
# cnt = 0
# while n > 0:
#     rem = n % 10
#     sm += rem
#     cnt += 1
#     n //= 10
# print(f'В числе "{nn}" {cnt} цифр(ы) суммой {sm}')