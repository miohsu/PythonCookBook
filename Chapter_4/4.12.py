from itertools import chain

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
for x in chain(a, b):
    print(x)
