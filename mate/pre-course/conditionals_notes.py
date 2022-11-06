print(int(False))  # 0
print(int(True))  # 1
print(False < True)  # True
print(False == False)  # True
print(10 > False)  # True // 10 > 0
# print(1 < '1') // error
print(1 == [1])  # False
# print(1 < [1])  # Error. Only ==
# Сравнивать можем, но >=, <=, != - и т.д. - нет



print(5 and 3)  # 3 // and True - get last operator
print(0 and False)  # 0 // and False - get first operator
print(5 or 3)  # 5 // or True - get first operator
print(0 or False)  # 5 // or False - get last operator
print(0 or 1 and 2 or 3)  # 2 // not > and > or : 0 or (1 and 2) or 3 - 0 or 2 or 3 - 2 or 3 - 2(get first true)


# all - if all True - True
# any - if at least one True - True
print(all([False for i in 'priveticka' if i in 'abcd']))  # False
print(all([False for i in 'privetik' if i in 'abcd']))  # True

print(any([False for i in 'privetik' if i in 'abcd']))  # False
print(any([False for i in 'privetik' if i in 'abcd']))  # True