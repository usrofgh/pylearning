def remove_element(nums: list, val_: int) -> int:
    i = 0
    while i < len(nums):
        v = nums[i]
        if v == val_:
            nums.remove(v)
            continue
        i += 1
    return len(nums)




def remove_element(nums: list, val: int) -> int:
    for i in range(nums.count(val)):
        nums.remove(val)
    return len(nums)
