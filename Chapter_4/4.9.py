from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

items = ['a', 'b', 'c']

# for p in permutations(items, 2):
#     print(p)

# for c in combinations(items, 1):
#     print(c)

for cr in combinations_with_replacement(items, 2):
    print(cr)
