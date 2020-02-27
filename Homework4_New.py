import random

"""
1. Dict comprehensions
Создайте словарь с помощью генератора словарей, так чтобы его
ключами были числа от 1 до 20, а значениями кубы этих чисел.
"""
dct = {el: el ** 3 for el in range(1, 21)}
print(dct)

"""
2. Дан список стран и городов каждой страны. Затем даны
названия городов. Для каждого города укажите, в какой стране
он находится.
"""
countrys_and_cities = {}
n = int(input("Введите количество стран: "))
for i in range(n):
    country, *cities = \
        input("Введите страну и города этой страны: ").split()
    for city in cities:
        countrys_and_cities[city] = country

m = int(input("Введите количество запросов стран: "))
for j in range(m):
    j = countrys_and_cities.get(input("Введите название города: "))
    print(j)

"""
3. Даны два списка чисел. Посчитайте, сколько различных чисел
содержится одновременно как в первом списке, так и во втором.
"""
list_first = set(list(input().split()))
list_second = set(list(input().split()))
list_intersection = list_first.intersection(list_second)
print(list_intersection)

"""
4. Даны два списка чисел. Посчитайте, сколько
различных чисел входит только в один из этих списков
"""
list_first = set(list(input().split()))
list_second = set(list(input().split()))
list_difference = list_first.difference(list_second)
print(list_difference)

"""
5. Каждый из N школьников некоторой школы знает Mi
языков. Определите, какие языки знают все школьники
и языки, которые знает хотя бы один из школьников.
"""
students = {}
number_of_students = \
    int(input("Введите количество студентов: "))
for student in range(1, number_of_students + 1):
    number_of_languages = \
        int(input("Введите количество языков: "))
    languages = []
    for language in range(number_of_languages):
        language = input("Введите название языка: ")
        languages.append(language)
    students[student] = languages

total_languages = []
for i in students.values():
    for j in i:
        total_languages.append(j)
print('Общее количество языков = ', len(total_languages))
print('Все языки: ', total_languages)

n_random = random.randint(1, number_of_students)
print('Студент под номером', n_random, 'знает',
      len(students[n_random]), 'языка(ов)')
print('а именно', (students[n_random]))

"""
6. Во входной строке записан текст. Словом считается
последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или
символами конца строки. Определите, сколько различных
слов содержится в этом тексте.
"""
trash = input('Введите текст ').split()
lst_1 = []
new_strin = ''
text = []

for i in trash:
    if '/' in i:
        k = i.split('/')
        if '' in k:
            k.remove('')
        new_strin += ' '.join(k) + ' '
    else:
        lst_1.append(i)

lst_2 = new_strin.strip().split()
lst = lst_1 + lst_2

for word in lst:
    if word not in text:
        text.append(word)

print('Всего в тексте', len(text), 'не повторяющихся слов')

"""
7. Даны два натуральных числа. Вычислите их
наибольший общий делитель при помощи алгоритма
Евклида (мы не знаем функции и рекурсию).
"""
n, m = int(input('Введите два числа: '))

while m != 0:
    if n < m:
        n, m = m, n
    m, n = n % m, m
print(n)
