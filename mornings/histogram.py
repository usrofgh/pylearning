def histogram(results: list) -> str:
    str_res = ""
    j = 1
    for i in range(len(results)):
        v = " " + str(results[i]) if results[i] else ""
        str_res = (
                str(j) + "|" + "#" * results[i] +
                v + "\n" + str_res
        )
        j += 1
    return str_res.strip()


print(histogram([7,3,10,1,0,5]))



def histogram(results: list) -> str:
    return "".join(
        "{}|{} {}\n".format(7 - index, element * "#", element)
        for index, element in enumerate(reversed(results), 1)
    ).replace(" 0", "")
