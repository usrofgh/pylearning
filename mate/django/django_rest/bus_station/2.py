def longest_common_prefix(strings_list: list) -> str:
    if strings_list.count(""):
        return ""
    if len(strings_list) == 1:
        return strings_list[0]

    max_len = len(max(strings_list))

    for i in range(max_len - 1, -1, -1):
        res = [el[:i] for el in strings_list]
        if len(set(res)) == 1:
            return res[0]
    return ""


strings_list = ["a"]
print(longest_common_prefix(strings_list))
