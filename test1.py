cd = 1

def a():
    def b():
        cd = 2
        print(cd)
    b()

a()
print(cd)