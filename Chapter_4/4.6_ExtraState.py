# 带有外部状态的生成器函数
from collections import deque


class LineHistory(object):
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for line_no, line in enumerate(self.lines, 1):
            yield line
            self.history.append((line_no, line))

    def clear(self):
        self.history.clear()


if __name__ == '__main__':
    data = [
        'Hello Ansible',
        'Hello Django',
        'Hello Python',
        'Hello Java',
    ]

    lines = LineHistory(data)
    for line in lines:
        if 'Python' in line:
            for line_no, hline in lines.history:
                print('{}:{}'.format(line_no, hline))
