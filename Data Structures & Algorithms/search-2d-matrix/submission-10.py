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
            if matrix[mid_row][0] > target:
                b = mid_row - 1
                while l <= r:
                    mid_col = (l + r) // 2
                    if matrix[b][mid_col] < target:
                        l = mid_col + 1
                    elif matrix[b][mid_col] > target:
                        r = mid_col - 1
                    else:
                        return True
            elif matrix[mid_row][r] < target:
                t = mid_row + 1
                while l <= r:
                    mid_col = (l + r) // 2
                    if matrix[t][mid_col] < target:
                        l = mid_col + 1
                    elif matrix[t][mid_col] > target:
                        r = mid_col - 1
                    else:
                        return True
            else:
                while l <= r:
                    mid_col = (l + r) // 2
                    if matrix[mid_row][mid_col] < target:
                        l = mid_col + 1
                    elif matrix[mid_row][mid_col] > target:
                        r = mid_col - 1
                    else:
                        return True
        return False