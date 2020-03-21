"""
Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел, отсортированных
по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(lst):
    count = ''
    for el in range(len(lst) - 1):
        if lst[el] + 1 == lst[el + 1] and lst[el] - 1 != lst[el - 1]:
            count += "{}-".format(lst[el])
        elif lst[el] + 1 != lst[el + 1]:
            count += "{}, ".format(lst[el])
    count += str(lst[-1])
    print('"{}"'.format(count))


lst = [0, 1, 2, 3, 4, 7, 8, 10]
get_ranges(lst)
