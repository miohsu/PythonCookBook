from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for i in items:
        if isinstance(i, Iterable) and not isinstance(i, ignore_types):
            yield from flatten(i)
        else:
            yield i


if __name__ == '__main__':
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    new_items = flatten(items)
    print(list(new_items))

