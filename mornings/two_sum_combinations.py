def two_sum(nums: list, target: int) -> list:
    seen = {}
    for index, value in enumerate(nums):
        remaining = target - nums[index]
        if remaining in seen:
            return [seen[remaining], index]
        seen[value] = index



from itertools import combinations


def two_sum(nums: list, target: int) -> list:
    res = []
    for item in combinations(nums, 2):
        if sum(item) == target:
            res.append(nums.index(item[0]))
            res.append(nums.index(item[1], res[0] + 1))
            return sorted(res)

