def tv_remote(word: str) -> int:
    keyboard = [
        "abcde123",
        "fghij456",
        "klmno789",
        "pqrst.@0",
        "uvwxyz_/",
    ]
    cur_pos = (0, 0)
    total_presses = 0
    for letter in word:
        letter_pos = None
        for i, row in enumerate(keyboard):
            if letter in row:
                letter_pos = (i, row.index(letter))
                break
        if letter_pos is None:
            raise ValueError("Invalid character: " + letter)
        row_dist = abs(cur_pos[0] - letter_pos[0])
        col_dist = abs(cur_pos[1] - letter_pos[1])
        total_presses += row_dist + col_dist + 1
        cur_pos = letter_pos
    return total_presses
