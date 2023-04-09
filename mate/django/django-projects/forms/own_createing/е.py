def longest_substring(string: str):
    max_length = 0
    start = 0
    seen = {}

    for end, char in enumerate(string):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length

string = 'skjdhaksjdhakjdhaskjdhasjkheiqwe928348344$#@RFDF$GGFHTYefafdwew4234tfgDFG3$3432432rseafDFASer233432e'
print(longest_substring(string))