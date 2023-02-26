# hash-function - принимает хешируемый объект и возвращает числовое значение
# из значения можно получить хеш, но не наоборот

# hash() - O(1)

print(hash(1))  # 1
print(hash(1.0))  # 1
print(hash(2))  # 2
print(hash(2))  # 2
print(hash(True))  # 1
print(hash(False))  # 0
print(hash(-1))  # -2 // -1 is reserved value

print(hash(2.1))  # 230584300921369602
print(hash("a"))  # 8214431473463863175
print(hash("a"))  # 8214431473463863175

print(hash(0.1) == hash(230584300921369408))
# print(hash([1, 2, 3]))  # TypeError: unhashable type: "list"


class User:
    pass


user = User()

print(hash(user))  # hash_int
print(hash(user.__hash__()))  # hash_int
print(hash(User))  # hash_int. Mutable but hashed
# print(User.__hash__())  # TypeError: descriptor '__hash__' of 'object' object needs an argument


# Hash tables

d = {}
#  в hash table 8 ячеек памяти
d[11] = 100  # hash(11) = 11, 11 % 8(размер HT) = 3 - помещаем в 3-ю ячейку
d[15] = 200  # hash(15) = 15, 15 % 8 = 7 - помещаем 200 в 7-ю ячейку
print(d[11])  # hash(11) = 11, 11 % 8 = 3, считываем с 3-й ячейки значение - 100
# print(d[19])  # hash(19) = 19, 19 % 8 = 3, считывать 3-ю ячейку? ведь мы по 11k записывали? - нет. будет keyError,
# так как в ячейках также лежат ключи, не только значения, и если ключа не будет - ошибка
# https://prnt.sc/kNW8eMK6KREh
