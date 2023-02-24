def foo():
    print('[mod1] foo()')


class Foo:
    pass
if __name__ == "__main__":
    print ("Executed when invoked directly")
else:
    print ("Executed when imported")


print(__name__)