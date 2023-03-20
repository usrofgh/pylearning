def roman_to_int(roman: str) -> int:
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    r = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    res = 0

    for k, v in r.items():
        while True:
            if k in roman:
                res += v
                roman = roman.replace(k, "")
                continue
            break

    for ch in roman:
        res += romans.get(ch)

    return res


print(roman_to_int("CMXXVIII"))
