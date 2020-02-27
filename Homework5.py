"""
1. Define a dict comprehension which returns a
dictionary where the keys are numbers between
1 and n (both included) and the values are
square of keys. Define a code which count and
return the numbers of each character in a
count_me_string argument.
"""


def count_me_string(string):
    dct = {}
    for el in string:
        if not dct.get(el):
            dct[el] = 1
        else:
            dct[el] += 1
    return dct


string = input('Введите строку: ')
out_dict = count_me_string(string)
print(out_dict)

"""
2. Дан текст (строк может быть много, разделенных
\\n). Выведите слово, которое в этом тексте встречается
чаще всего. Если таких слов несколько, выведите то,
которое меньше в лексикографическом порядке.
"""
strin = input('Введите строку: ')
lst = strin.replace('\n', ' ').split()

lst_new = []
for i in lst:
    lst_new.append(i.strip(' ,./!@#$%^&*()_+!"№;%:?*()_'))

dct = {}
for word in lst_new:
    dct[word] = dct.setdefault(word, 0)
    dct[word] += 1
max_value = max(dct.values())

lst_max = []
for key in dct.keys():
    if dct[key] == max_value:
        lst_max.append(key)
lst_max = sorted(lst_max)
print("Полученный результат: ", lst_max[0])

"""
3. Дан список стран и городов каждой страны. Затем
даны названия городов. Для каждого города укажите,
в какой стране он находится
"""
quantity_1 = int(input('Введите количество стран: '))
countys_cities = {}
cityes = []

for el in range(quantity_1):
    country, *cities = input\
        ('Ввдеите страну и города этой страны: ').split()
    for city in cities:
        countys_cities[city] = country

quantity_2 = int(input('Введите количество городов: '))

for el in range(quantity_2):
    cityes.append(input('Введите город: '))
for city in cityes:
    print(countys_cities.get(city))

"""
4. Даны два списка чисел. Посчитайте, сколько
чисел содержится одновременно как в первом списке,
так и во втором.
"""
set_1 = set(list(input('Введите первое множество: ').split()))
set_2 = set(list(input('Введите второе множество: ').split()))
s = ('Обшие числа: ', len(set_1 & set_2))
print(s)

"""
5. Даны два списка чисел. Посчитайте, сколько
чисел входит только в один из этих списков.
"""
set_1 = set(list(input('Введите первое множество: ').split()))
set_2 = set(list(input('Введите второе множество: ').split()))
s = ('Числа входящие только в первый список: ',
     len(set_1 ^ set_2))
print(s)
