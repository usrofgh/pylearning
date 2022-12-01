def a(msg, bsg = 1):

    def b():
        print(msg)
        print(bsg)
    return b

callit = a('hello')
# print(a())
print(callit())

# print(a.__closure__)
print(callit.__closure__)