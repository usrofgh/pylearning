def missing_number(unique_nums: list) -> int:
    n = len(unique_nums)
    missing_num = n
    for i in range(n):
        missing_num ^= i ^ unique_nums[i]
    return missing_num




print(missing_number([2, 0, 5, 3, 1]))
#  [9,6,4,2,3,5,7,0,1]
# [0, 1, 2, 3, 4, 5, 6, 7,   9[