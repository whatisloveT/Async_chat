'''Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.'''
list = ['attribute','класс','функция']
for i in list:
    a = bytes(i, encoding='utf-8')
    print(a)
    print(type(a))
    print(i==a)
#Отстаю от программы, не смог выполнить