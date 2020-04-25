"""
Написать программу которая находит ближайшую степень
двойки к введенному числу. 10(8), 20(16), 1(1)
"""
num = int(input('Введите число: '))
degree = 1
while degree < num:
    degree = degree << 1

if degree - num < num - (degree >> 1):
    print(degree)
else:
    print(degree >> 1)
