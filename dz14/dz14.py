#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10


n = int(input('Введите десятичное число: '))
print(format(n, 'b'))