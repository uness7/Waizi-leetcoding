# range-sum-query-immutable
# My answer does : 23xx ms NOT VERY OPTIMAL BUT PASSES

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        size: int = (right - left) + 1
        prefixSum: int = 0
        prefixSum = self.nums[left]
        for i in range(1, size):
            prefixSum += self.nums[left + i]
        return prefixSum

