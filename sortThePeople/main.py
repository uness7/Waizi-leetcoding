from typing import *
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        my_dict: Dict = {}
        for x, y in zip(heights, names):
            my_dict[x] = y 
        res: Dict = dict(sorted(my_dict.items(), key=lambda item : item[0], reverse=True))
        result : List[str] = []
        list(map(lambda item : result.append(item[1]), res.items()))
        return result

a = Solution()
print(a.sortPeople(["Nor", "Jo", "Jennna"], [130, 190, 189]))
        


