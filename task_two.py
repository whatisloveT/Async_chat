'''Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных '''

list = [b'class',b'function',b'method']
for i in list :
    print(i)
    print(type(i))
    print(len(i))
