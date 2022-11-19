# An iterator is an object that contains a countable number of values.
# Итератор должен содержать функции __iter__(), __next__()

# range - итератор, или генератор? - Ни то , ни другое. Range это объект по к-му можно итерирваться - iterable, как и для списка.
# Чтобы был итератор, range нужно обвернуть в функцию iter(). Только тогда можно юзать next. По этой же причине не является джен. Так как любой генератор == итератор.

it = iter(range(1, 5, 2))
print(next(it))
print(next(it))

numbers = [1, 3, 5]
for n in numbers:  # можем итерироваться по numbers, но это не значит, что список - итератор, как и range(). Чтобы можно было итерировться, нужно обвернуть в iter()
    print(n)

# print(next(range(1, 5, 2))) TypeError: 'range' object is not an iterator - потому что не итератор