def longest_vowel_chain(string: str) -> int:
    vowels = "aeiou"
    chain_size = 0
    res = 0

    for v in string:
        if v in vowels:
            chain_size += 1
            continue

        if chain_size > res:
            res = chain_size
        chain_size = 0

    return res


print(longest_vowel_chain("ultrarevolutionariees"))
