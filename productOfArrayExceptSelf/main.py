#####################################################################################
############################ Solution ###############################################
# Not optimal & doesn't pass leetcode

class Solution1:
    def prefixProductArray(self, list: List[int]):
        result: List[int] = []
        i: int = 0
        while i < len(list):
            j: int = 0
            current: int = list[i]
            product: int = 1
            while j < len(list):
                if i == j:
                    break
                product *= list[j]
                j += 1
            result.append(product)
            i += 1
        return result

    def suffixProductArray(self, list: List[int]):
        result: List[int] = []
        i: int = 0
        while i < len(list):
            j: int = i + 1
            product: int = 1
            while j < len(list):
                product *= list[j]
                j += 1
            result.append(product)
            i += 1
        return result

    def productExceptSelf(self, list: List[int]) -> List[int]:
        prefix: List[int] = self.prefixProductArray(list)
        suffix: List[int] = self.suffixProductArray(list)
        result: List[int] = []
        for item1, item2 in zip(prefix, suffix):
            result.append(item1 * item2)
        return result


# Optimal Solution
class Solution:
    def productExceptSelf(self, list: List[int]) -> List[int]:
        n: int = len(list)
        result: List[int] = [1] * n
        prefix: int = 1
        for i in range(n):
            result[i] = prefix
            prefix *= list[i]

        suffix: int = 1
        for i in range(n - 1, - 1, -1):
            result[i] *= suffix
            suffix *= list[i]
        return result
