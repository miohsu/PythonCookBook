# 反向迭代
class CountDown(object):
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n < self.start:
            yield n
            n += 1


if __name__ == '__main__':
    print(list(reversed(CountDown(10))))
    print(list(CountDown(10)))
