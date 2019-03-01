from itertools import dropwhile, islice
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASEDIR, 'files', 'passwd'), 'r') as fp:
    for line in dropwhile(lambda line: line.startswith('#'), fp):
        print(line, end='')
