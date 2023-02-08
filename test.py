class PowTwo:
    def __init__(self, max_power: int = 0):
        self.max_power = max_power

    def __iter__(self):
        self.current_power = 0
        return self

    def __next__(self):
        if self.current_power > self.max_power:
            raise StopIteration

        result = 2 ** self.current_power
        self.current_power += 1
        return result


# write the same, but generator

def pow_two(max_power: int = 0):
    curr_power = 0
    while curr_power < max_power:
        yield 2 ** curr_power
        curr_power += 1


print(list(pow_two(4)))
# list(pow_two(4))