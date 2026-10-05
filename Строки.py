# s = 'Здравствуйте, гости!'
# print(s.index(','))
# print(s [0])
# print(s [6])
# print(s [-1])
# print(len(s))
# print(s[:5])
# print(s[:12])
# print(s[::-1])
# # for i in s:
# #     print(i, end=' ')
# print(s[19])
# for i in range(len(s)):
#     print(s[i], end=' ')
#
#
# print(s.isalpha())
# print(s.isalnum())
# s1 = '123'
# print(s1.isalnum())
# print(s.startswith('З'))
# print(s.endswith('!'))

s = '!  Здравствуйте, гости! !'
print(n := s.lower())
print(s.upper())
print(s.title()) # все слова начинаются с большой буквы
print(s.capitalize()) # переменная начинается с большой буквы
print(s.rjust(40)) # переменная пишется в 40 знакоместах / выравнивание по правому краю
print(s.ljust(40)) # переменная пишется в 40 знакоместах / выравнивание по левому краю
print(s.center(40)) # переменная пишется в 40 знакоместах / выравнивание по центру
print(s.strip()) # удаляем пробелы по краям
print(s.strip('! З')) # удаляем знаки по краям
print(s.rstrip('!')) # удаляет знаки справа
print(s.lstrip('!')) # удаляет знаки слева
print(s.index('т', 8, 12)) # или s.find() поиск индекса / символа или начала подстроки
print(s.find('т', 8, 12))
print(s.replace('т', 'LN').replace(',', 'Э!'))

ls = s.split() # создает список разделяя слова по пробелу
ls = s.split(', ')
print(ls)
print(','.join(ls))
