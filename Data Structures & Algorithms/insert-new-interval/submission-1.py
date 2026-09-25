class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        result = []
        if len(intervals) == 1:
            result.append(intervals[0])
            return result

        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if prev[1] < curr[0]:
                result.append(prev)
                if i == len(intervals) - 1:
                    result.append(curr)
                    return result
                prev = curr
            else:
                prev[1] = max(curr[1], prev[1])
                if i == len(intervals) - 1:
                    result.append(prev)
                    return result