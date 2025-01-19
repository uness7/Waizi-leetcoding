from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:          
        my_dict = {}
        for i, num in enumerate(nums):
            diff = target - num 
            if diff in my_dict:
                return [my_dict[diff], i]
            my_dict[num] = i

# Basic tests
a = Solution()
print(a.twoSum([2,7,11,15], 9))
