(acc, seen) = ([], set())

x, y, z = [1, 2, 3]
x1, y1, z1 = {1}, {2}, {3}
x2, y2, z2 = 'xyz'

t1, t2 = 1, 2
t1, t2 = t2, t1

rectangle = (0, 0), (4, 4)
(x1, y1), (x2, y2) = rectangle

first, *rest, last = range(1, 10)  # 1, [2 ... 8], 9

import dis


# dis.dis('first, *rest, last = ("a", "b", "c")')
# dis.dis('first, *rest, last = [  "a", "b", "c"]')

def f(*args, **kwargs):
    print(args, kwargs)


b = {'baz ': 42}
f(1, 2, *range(1, 11), foo='bar', **b, boo=24)
