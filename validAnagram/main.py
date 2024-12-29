class Solution:
    def isAnagram() -> bool:
        return len(s) == len(t) and sorted(s) == sorted(t)
