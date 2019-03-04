from collections import defaultdict
import os

from Chapter_4 import conf


items = ['a', 'b', 'c']
data = [(11, 12), (13, 14), (15, 16)]
word_summary = defaultdict(list)

# for index, value in enumerate(items, start=10):
#     print(index, value)


# for n, (x, y) in enumerate(data):
#     print(n, x, y)

file_path = os.path.join(conf.BASEDIR, 'files','news')
with open(file_path, 'r') as fp:
    lines = fp.readlines()

for index, line in enumerate(lines, 1):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(index)

print(word_summary)

