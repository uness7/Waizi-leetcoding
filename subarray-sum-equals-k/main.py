# Using prefixSum and dict()

class Solution:
    def subarraySum(self, n: List[int], k: int) -> int:
        counter = 0
        size: int = len(n)
        prefixSum: int = 0
        myHashMap = {0: 1}
        for i in range(size):
            prefixSum += n[i]
            if prefixSum - k in myHashMap:
                counter += myHashMap[prefixSum - k]
            myHashMap[prefixSum] = myHashMap.get(prefixSum, 0) + 1
        return counter
