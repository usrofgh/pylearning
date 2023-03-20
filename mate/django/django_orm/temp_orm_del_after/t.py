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

def find_smallest(lst: list, number: int) -> list:
    sorted_list = sorted(enumerate(lst), key=lambda x: x[1])[:3]
    return [x[0] for x in sorted_list]

