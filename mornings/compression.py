def compression(chars: list) -> int:
    if len(chars) == 1:
        return 1

    res = []
    counter = 1
        for i in range(1, len(chars)):
        if chars[i] == chars[i - 1]:
            counter += 1
            if i == len(chars) - 1:
                res.append(chars[i - 1] + str(counter))
                break
        else:
            res.append(chars[i - 1])
            counter = 1
    return sum([len(ch) for ch in res])


print(compression(["a", "a", "b", "b", "c", "c", "c"]))