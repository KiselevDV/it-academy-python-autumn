"""
Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""


def calls(my_func):
    def wrapper():
        result = my_func()
        with open('results.txt', 'a') as file:
            file.write(str(result) + '\n')

    return wrapper


@calls
def my_func():
    long_words = ''
    text = input("Введите текст ").split()
    for el in text:
        if len(el) > len(long_words):
            long_words = el
    print(long_words)
    return long_words


my_func()
