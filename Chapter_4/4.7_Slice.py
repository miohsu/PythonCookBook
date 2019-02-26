# 迭代器切片
import itertools


def count(n=1):
    while True:
        yield n
        n += 1


if __name__ == '__main__':
    for num in itertools.islice(count(0), 10, 20):
        print(num)
