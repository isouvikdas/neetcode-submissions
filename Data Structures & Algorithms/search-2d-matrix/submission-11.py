class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        while t <= b:
            mid_row = (t + b) // 2
            if target < matrix[0][0]:
                return False
            elif target > matrix[len(matrix) - 1][len(matrix[0]) - 1]:
                return False
            elif target < matrix[mid_row][0]:
                b = mid_row - 1
            elif target > matrix[mid_row][-1]:
                t = mid_row + 1
            else:
               break
        
        row = (t + b) // 2
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False