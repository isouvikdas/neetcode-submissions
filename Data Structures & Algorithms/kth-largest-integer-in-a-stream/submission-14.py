from heapq import heapify, heappop, heappush

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums

        heapify(self.heap)
        while len(self.heap) > k:
            heappop(self.heap)
            print(self.heap)

    def add(self, val: int) -> int:
        print(self.heap)
        print(f"val {val} to be added")
        result = heappop(self.heap) if len(self.heap) >= self.k else val

        if result <= val:
            heappush(self.heap, val)
            result = heappop(self.heap)
            heappush(self.heap, result)
        else:
            heappush(self.heap, result)
        print(f"result: {result}")
        return result
