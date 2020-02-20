"""
1. Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество
L товара Посчитайте общую цену в рублях и копейках за L товаров.
"""

m = int(input('Введите количество рублей: '))
n = int(input('Введите количество копеек: '))
p = int(input('Введите количество товара: '))
c = n / 100
total = (m + c) * p
rub = int(total // 1)
penny = (total * 100) % 100
print('Общая цена', rub, 'рублей', penny, 'копеек')

"""
3. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания
"""
sentence = input("Введите предложение: ").split()
s_1 = []

for i in sentence:
    i = i.strip(', . ! ; : ? -  « » ' ' " " ... ')
    s_1.append(i)

longword = s_1[0]

for j in s_1:
    if len(j) > len(longword):
        longword = j
print(longword)

"""
4. Вводится строка. Требуется удалить из нее
повторяющиеся символы и все пробелы. Например,
если было введено "abc cde def", то должно быть выведено "abcdef".
"""
strin = input()
s = strin.split()
converted_strin = ''.join(s)
new_strin = []

for i in converted_strin.lower():
    if i not in new_strin:
        new_strin.append(i)
new_strin = ''.join(new_strin)

print(new_strin)

"""
5. Посчитать количество строчных (маленьких) и прописных (больших)
букв в введенной строке. Учитывать только английские буквы.
"""
text = input()
lower_letter = 0
upper_letter = 0

for letter in text:
    if letter.islower():
        lower_letter += 1
    elif letter.isupper():
        letter.isupper()
        upper_letter += 1

print(lower_letter)
print(upper_letter)

"""
6. Выведите n-ое число Фибоначчи, используя только временные
переменные, циклические операторы и условные операторы. n - вводится
"""
n_1 = n_2 = 1
n = int(input('Введите чсло: '))

if n < 2:
    quit()

print('\n', n_1, n_2, end=' ')

for i in range(2, n):
    n_1, n_2 = n_2, n_1 + n_2
    print(n_2, end=' ')
print()

"""
7. Определите, является ли число палиндромом (читается слева направо
и справа налево одинаково).  Число положительное целое, произвольной
длины. Задача требует работать только с числами (без конвертации
числа в строку или что-нибудь еще)
"""
num = int(input('Введите число: '))
n = num
rev = 0

while n > 0:
    digit = n % 10
    n = n // 10
    rev = rev * 10 + digit

if num == rev:
    print('Заданное число является палиндромом!')
else:
    print('Заданное число не является палиндромом!')

"""
2.1 Вы должны написать функцию, которая принимает
положительное целое число и возвращает:
"Fizz Buzz", если число делится на 3 и 5;
"Fizz", если число делится на 3;
"Buzz", если число делится на 5;
Число, как строку для остальных случаев.
"""


def checkio(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        word = 'Fizz Buzz'
    elif number % 3 == 0:
        word = 'Fizz'
    elif number % 5 == 0:
        word = 'Buzz'
    else:
        word = str(number)
    return word


"""
2.2 Дан массив целых чисел. Нужно найти сумму элементов с
четными индексами (0-й, 2-й, 4-й итд), затем перемножить эту
сумму и последнийэлемент исходного массива. Не забудьте, что
первый элемент массива имеет индекс 0.
"""


def checkioo(array):
    sum = 0
    for i in array[::2]:
        sum += i
    if array == []:
        composition = 0
    else:
        composition = sum * array[-1]
    return composition


"""
2.3 Вам даны текущие цены на акции. Вам необходимо
выяснить за какие акции дают большую цену.
"""


def best_stock(a):
    max_value = 0.0
    key_max_value = ''
    for key, value in a.items():
        if value > max_value:
            max_value = value
            key_max_value = key
    return key_max_value


"""
2.4 На вход Вашей функции будет передано одно предложение.
Необходимо вернуть его исправленную копию так, чтобы оно
всегда начиналось с большой буквы и заканчивалось точкой.
"""


def correct_sentence(text: str) -> str:
    word = text[0]
    other_words = text[1::]
    word = word.capitalize()
    new_text = word + other_words
    if new_text[-1] != '.':
        new_text = new_text + '.'
    return new_text


"""
2.5 Дана последовательность строк. Вы должны объединить эти строки
в блок текста, разделив изначальные строки запятыми. В качестве
шутки над праворукими роботами, вы должны заменить все вхождения
слова "right" на слова "left", даже если это часть другого слова.
Все строки даны в нижнем регистре.
"""


def left_join(phrases):
    strin = ','.join(phrases)
    s = strin.replace('right', 'left')
    return s
