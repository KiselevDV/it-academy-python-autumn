import Task_1


def runner(*functions):
    """Реализация функции от функций"""
    if len(functions) == 0:
        functions = [el for el in dir(Task_1) if not el.startswith('__')]
    for el in functions:
        func = getattr(Task_1, el)
        func()


runner()
