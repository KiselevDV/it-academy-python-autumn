"""
Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""


def all_calls(call_func):
    def wrapper(rec):
        result = call_func(rec)
        with open('results.txt', 'a') as file:
            file.write(str(result) + '\n')

    return wrapper


@all_calls
def call_func(rec):
    return rec


rec = int(input())
call_func(rec)
