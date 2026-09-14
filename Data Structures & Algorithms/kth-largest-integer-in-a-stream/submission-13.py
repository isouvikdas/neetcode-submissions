from heapq import heappush, heappop, heapify

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums

        heapify(self.heap)
        while len(self.heap) > k:
            heappop(self.heap)
        print(self.heap)

    def add(self, val: int) -> int:
        result = heappop(self.heap) if len(self.heap) >= self.k else val
        if val < result:
            heappush(self.heap, result)
        else:
            heappush(self.heap, val)
            result = heappop(self.heap)
            heappush(self.heap, result)
        return result

