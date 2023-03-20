def fix_string_case(word: str) -> str:
    transofrm = ["l" if ch > "Z" else "u" for ch in word]
    return word.lower() if transofrm.count("l") == transofrm.count("u") else word.upper()
