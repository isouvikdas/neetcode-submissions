class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        pairs = [[p,(target-p)/s] for p,s in zip(position, speed)]
        pairs.sort(reverse=True)
        # print(pairs)
        count = 1
        prev_t = pairs[0][1]
        for i in range(1, len(pairs)):
            curr_t = pairs[i][1]
            if prev_t >= curr_t:
                continue
            else:
                count += 1
                prev_t = curr_t

        return count

