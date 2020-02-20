"""
1. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
"""
text = input("Please enter an offer: ")
punctuation_marks = ' ! ( ) " ; : ? ( ) , . [ ] '

for i in punctuation_marks:
    text = text.replace(i, ' ')

lst = text.split()
other_word = len(lst[0])
word = ''

for j in range(len(lst)):
    if other_word < len(lst[j]):
        other_word = len(lst[j])
        word = lst[j]
print(word)

"""
3. Вводится строка. Требуется удалить из нее повторяющиеся
символы и все пробелы. Например, если было введено
"abc cde def", то должно быть выведено "abcdef".
"""
text = "abc cde def"
text_new = ''

for i in text:
    if i not in text_new and i != ' ':
        text_new += i
print(text_new)

"""
3. Посчитать количество строчных (маленьких) и прописных (больших)
букв в введенной строке. Учитывать только английские буквы.
"""
sentence = input('Введите строку: ')
up = 0
down = 0

for i in sentence:
    if 'A' <= i <= 'Z':
        up += 1
    elif 'a' <= i <= 'z':
        down += 1
print('В заданном предложении', up,
      'прописных и', down, 'строчных букв.')
