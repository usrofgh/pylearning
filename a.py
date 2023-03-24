import string as s


def consonant_value(string: str) -> int:
    if len(string) == 1:
        return 0
    alphab = s.ascii_lowercase
    volums = "aeiou"
    res = []
    buff = 0

    for i in range(len(string)):
        if string[i] not in volums:
            buff += alphab.index(string[i]) + 1

            if i + 1 == len(string):
                res.append(buff)
                break
            else:
                continue
        if buff:
            res.append(buff)
        buff = 0
    return max(res) if res else 0


print(consonant_value("abb"))
