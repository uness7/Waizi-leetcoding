# Similar to validSuduko problem (easy)

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # hashmaps
        rows = collections.defaultdict(set) # sets don't allow duplicates, this is useful in this problem
        cols = collections.defaultdict(set)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] in rows[r] or matrix[r][c] in cols[c]:
                    return False
                rows[r].add(matrix[r][c])
                cols[r].add(matrix[r][c])
        return True
