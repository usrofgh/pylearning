def longest_substring(string: str) -> int:
    max_length = 0
    start = 0
    seen = {}

    for end, char in enumerate(string):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length
