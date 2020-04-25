"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""
num = int(input('Введите число: '))

degree = 1
if num != 0:
    while num & degree == 0:
        degree = degree << 1
print(degree)
