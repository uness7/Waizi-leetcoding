###########################################################################################
###########################################################################################

from typing import List, Tuple, Dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:          
	# iterate over the list
        for num in nums:
            new_target = target - num # get the difference

	    # check if the difference is an element of the list && that the difference doesn't equal the element itself
            if new_target in nums and new_target != num:
                return [nums.index(num), nums.index(new_target)]

	    # otherwise
            elif new_target in nums:
                if nums.count(num) > 1:
                    return [i for i, value in enumerate(nums) if value == num]
        return []


# Basic tests

a = Solution()

print(a.twoSum([3, 3], 6))

print(a.twoSum([1, 2, 9, 3], 11))

print(a.twoSum([0, 1, 3, 2], 5))

print(a.twoSum([2,7,11,15], 9))

print(a.twoSum([1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1], 11))

