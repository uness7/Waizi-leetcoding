
# Level: easy

# set() don't have duplicates (key feature) & are more optimal than lists for operations like lookup

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
	return (len(set(nums)) != len(nums))
