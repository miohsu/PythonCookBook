from itertools import zip_longest


xpts = [1, 5, 4, 20, 10, 7]
ypts = [101, 78, 37, 15, 62, 99, 100]

for x, y in zip_longest(xpts, ypts, fillvalue='haha'):
    print(x, y)
