"""
FizzBuzz
Write a program that prints the numbers from 1 to 100,
but for multiples of three print “Fizz” instead of the
number and for multiples of five print “Buzz”. For
numbers which are multiples of both three and five,
print “FizzBuzz”.
"""
num = 0
while num < 100:
    num += 1
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

"""
List practice
Use a list comprehension to construct the list
['ab', 'ac','ad', 'bb', 'bc', 'bd']. Use a slice on the
above list to construct the list ['ab', 'ad', 'bc']. Use
a list comprehension to construct the list ['1a', '2a',
'3a', '4a']. Simultaneously remove the element '2a' from
the above list and print it. Copy the above list and add
'2a' back into the list such that the original is still
missing it. 
"""
lst_1 = [a + b for a in "ab" for b in "bcd"]
print("Список № 1: ", lst_1, "\n")

lst_2 = lst_1[::2]
print("Список № 2: ", lst_2, "\n")

lst_3 = [a + b for a in '1234' for b in 'a']
print("Список № 3: ", lst_3, "\n")

lst_4 = lst_3.pop(1)
print("Список № 4: ", lst_4, "\n")

lst_5 = lst_3[::]
lst_5.append('2a')
print("Список № 3:", lst_3, '\n', "Список № 5:", lst_5)

"""
Tuple practice
Create the list ['a', 'b', 'c'], then create a tuple from
that list. Create the tuple ('a', 'b', 'c'), then create a
list from that tuple. (Hint: the material needed to do this
has been covered, but it's not entirely obvious) Make the
following instantiations simultaneously: a = 'a', b=2,
c='gamma'. (That is, in one line of code). Create a tuple
containing just a single element which in turn contains the
three elements 'a', 'b', and 'c'. Verify that the length is
actually 1 by using the len() function.
"""
lst = ['a', 'b', 'c']
lst = tuple(lst)
print(lst)
tpl = ('a', 'b', 'c')
tpl = list(tpl)
print(tpl, '\n')

a, b, c = 'a', 'b', 'gamma'
print(a, b, c)

lst = ["a", "b", "c"]
tpl = (lst,)
print(tpl)
if len(tpl) == 1:
    print("Это кортеж из одного числа")
else:
    print("Это фигня")
