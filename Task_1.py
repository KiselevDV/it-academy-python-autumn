"""
1.Оформите решение задач из прошлых домашних
работ в функции. Напишите функцию runner.
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


def dict_comprehensions():
    # Создайте словарь с помощью генератора
    # словарей, так чтобы его ключами были числа
    # от 1 до 20, а значениями кубы этих чисел.
    print({el: el ** 3 for el in range(1, 21)})


def countrys_and_cities():
    # Дан список стран и городов каждой страны. Затем даны
    # названия городов. Для каждого города укажите, в какой
    # стране он находится. Программа получает на вход количество
    # стран N. Далее идет N строк, каждая строка начинается с
    # названия страны, затем идут названия городов этой страны.
    # В следующей строке записано число M, далее идут M запросов
    # — названия каких-то M городов, перечисленных выше. Для
    # каждого из запроса выведите название страны, в котором
    # находится данный город.
    countrys_and_cities = {}
    countrys = []
    n = int(input("Введите количество стран: "))
    for i in range(n):
        country, *cities = \
            input("Введите страну и города этой страны: ").split()
        for city in cities:
            countrys_and_cities[city] = country

    m = int(input("Введите количество запросов стран: "))
    for j in range(m):
        j = countrys_and_cities.get(input("Введите название города: "))
        countrys.append(j)
    print(*countrys, sep='\n')


def two_lists_1():
    # Даны два списка чисел. Посчитайте, сколько
    # различных чисел содержится одновременно как в
    # первом списке, так и во втором.
    list_first = set(list(input().split()))
    list_second = set(list(input().split()))
    print(len(list_first.intersection(list_second)))


def two_lists_2():
    # Даны два списка чисел. Посчитайте, сколько
    # различных чисел входит только в один из этих списков.
    list_first = set(list(input().split()))
    list_second = set(list(input().split()))
    print(len(list_first.symmetric_difference(list_second)))


def language():
    # Каждый из N школьников некоторой школы знает Mi
    # языков. Определите, какие языки знают все школьники
    # и языки, которые знает хотя бы один из школьников.
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

    how_many = []
    everyone_knows = []
    for values in students.values():
        if len(values) > len(how_many):
            how_many = values
        for el in values:
            if el not in everyone_knows:
                count = 0
                for key in students.keys():
                    if el in students[key]:
                        count += 1
                if count == len(students):
                    everyone_knows.append(el)

    print('Языки которые знают все: ', len(everyone_knows))
    print('А именно: ', *everyone_knows)
    print('Языки которые знает хотябы один: ', len(how_many))
    print('А именно: ', *how_many)


def text():
    # Во входной строке записан текст. Словом считается
    # последовательность непробельных символов идущих подряд,
    # слова разделены одним или большим числом пробелов или
    # символами конца строки. Определите, сколько различных
    # слов содержится в этом тексте.
    text = input('Введите строку: ')
    lst = text.replace('\n', ' ').split()
    lst_new = []

    for i in lst:
        j = i.strip(' ,./!@#$%^&*()_+!"№;%:?*()_')
        if j not in lst_new:
            lst_new.append(j)

    print('Всего в тексте', len(lst_new), 'не повторяющихся слов')


def euclidean_theorem():
    """Найти НОД при помощи алгоритма Евклида"""
    n, m = (int(input()) for _ in range(2))
    if n < m:
        n, m = m, n

    while m != 0:
        m, n = n % m, m
    print(n)
