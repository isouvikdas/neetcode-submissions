class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return 0
        time = []
        for i in range(len(position)):
            time.append([position[i], (target - position[i]) / speed[i]])

        time.sort(reverse=True)
        # print(time)

        result = []
        result.append(time[0])
        for i in range(1, len(time)):
            if result[-1][1] < time[i][1]:
                result.append(time[i])
        print(result)
        return len(result)