# import pdb
# a = 10
# b = a + 5
# pdb.set_trace()  # остановимся тут
# c = a + b


def print_index_ok(index: int):
    print(index)
    print('ok!')


print('---START---')


for i in range(3):
    print_index_ok(i)

print('---END---')