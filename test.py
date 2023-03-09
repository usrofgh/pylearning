def pascal_triangle_row(row_index: int) -> list:
    prev = 1
    res = [1]
    for i in range(1, row_index + 1):
        curr = (prev * (row_index - i + 1)) // i
        res.append(curr)
        prev = curr
    return res


print(pascal_triangle_row(3))
