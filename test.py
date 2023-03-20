def fix_string_case(word: str) -> str:
    lower_count = 0
    upper_count = 0
    for ch in word:
        if "Z" < ch <= "z":
            lower_count += 1
        elif "A" <= ch <= "Z":
            upper_count += 1

    if lower_count < upper_count:
        return word.upper()
    return word.lower()


print(fix_string_case("oUAEi"))
