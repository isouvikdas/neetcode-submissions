class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            result = max(result, width * height)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return result