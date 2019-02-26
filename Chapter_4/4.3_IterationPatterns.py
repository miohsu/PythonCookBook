def frange(start, stop, increment=1):
    x = start
    while x < stop:
        yield x
        x += increment


if __name__ == '__main__':
    print(list(frange(2, 5)))
    for num in frange(4, 7, 2):
        print(num)
