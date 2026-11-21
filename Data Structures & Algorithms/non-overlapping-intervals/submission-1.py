class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0]
        result = 0

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] < prev[1]:
                prev[1] = min(prev[1], curr[1])
                result += 1
            else:
                prev = curr
        return result