from collections import Counter, deque
from heapq import heapify, heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapify(maxHeap)
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                c = 1 + heappop(maxHeap)

                if c:
                    q.append([c, time + n])
            if q and q[0][1] == time:
                heappush(maxHeap, q.popleft()[0])
        return time
                