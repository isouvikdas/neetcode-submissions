class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack: list[list[int]] = []
        output = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if i == 0:
                stack.append([i, t])
                continue
            while stack and stack[-1][1] < t:
                output[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append([i, t])
        return output