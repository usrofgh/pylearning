d = {"a": 1}
print(d.__getitem__("a"))
d.__setitem__("b", 2)
print(d)

# hash("a") # O(1)
# 34242424242 % 8 = index # O(1)
# get_element_by_index in list # O(1)

# в целом __get__item__ O(1)
# для __set__item__ тоже
