# class Solution:
    # Brute-Force
    # @staticmethod
    # def filterDigits(arr: List[str]) -> List[int]:
    #     return [int(x) for x in arr if x != "."]

    # @staticmethod
    # def checkNumbers(board: List[List[str]]) -> bool:
    #     i: int = 0
    #     j: int = 0
    #     digits: List[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    #     while i < len(board):
    #         j = 0
    #         while j < len(board[i]):
    #             curr: str = board[i][j]
    #             if curr not in digits and curr != ".":
    #                 return False
    #             j += 1
    #         i += 1
    #     return True


    # def checkRows(self, board: List[List[str]]) -> bool:
    #     i: int = 0
    #     while i < len(board):
    #         temp_list: List[str] = board[i]
    #         filtered_list: List[str] = Solution.filterDigits(board[i])
    #         if len(set(filtered_list)) != len(filtered_list):
    #             return False
    #         i += 1
    #     return True

    # def checkCols(self, board: List[List[str]]) -> bool:
    #     i: int = 0
    #     while i < len(board):
    #         current_col: List[str] = [row[i] for row in board]
    #         filtered_col: List[str] = Solution.filterDigits(current_col)
    #         if len(filtered_col) != len(set(filtered_col)):
    #             return False
    #         i += 1
    #     return True

    # def checkSubBox(self, board: List[List[str]]) -> bool:
    #     for k in range(9):
    #         row_offset = (k // 3) * 3
    #         col_offset = (k % 3) * 3
    #         sub_box = []
    #         for i in range(3):
    #             for j in range(3):
    #                 sub_box.append(board[row_offset + i][col_offset + j])
    #         filtered_box = Solution.filterDigits(sub_box)
    #         if len(filtered_box) != len(set(filtered_box)):
    #             return False
    #     return True



    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     if not Solution.checkNumbers(board):
    #         return False

    #     if not self.checkRows(board):
    #         return False

    #     if not self.checkCols(board):
    #         return False

    #     if not self.checkSubBox(board):
    #         return False
    #     return True

# ai solution optimal than brute force
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sub_boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue

                # Calculate sub-box index
                sub_box_index = (i // 3) * 3 + (j // 3)

                # Check for duplicates
                if num in rows[i] or num in cols[j] or num in sub_boxes[sub_box_index]:
                    return False

                # Add number to row, column, and sub-box
                rows[i].add(num)
                cols[j].add(num)
                sub_boxes[sub_box_index].add(num)

        return True

