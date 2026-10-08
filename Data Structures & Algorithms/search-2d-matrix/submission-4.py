class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Cols = len(matrix), len(matrix[0])
        
        top, bot = 0, Rows - 1

        while top <= bot:
            row = bot + (top - bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not(top <= bot):
            return False

        left, right = 0, Cols - 1
        row = bot + (top - bot) // 2

        
        while left <= right:
            mid = left + (right - left) // 2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1

        return False
