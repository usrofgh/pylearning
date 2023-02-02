a = 3

def change_a():
    a = 1
    global a
    a = 5

change_a()