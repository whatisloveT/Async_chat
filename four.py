'''
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
'''

list = ['разработка','администрирование','protocol','standard']
for i in list:
    enc_str_bytes = i.encode('utf-8')
    print(enc_str_bytes)
    print(type(enc_str_bytes))
    dec_str = enc_str_bytes.decode('utf-8')
    print(dec_str)
    print(type(dec_str))