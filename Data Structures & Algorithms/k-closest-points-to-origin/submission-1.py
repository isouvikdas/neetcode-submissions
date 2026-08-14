from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        m = {}
        for p in points:
            d = self.calculate_distance(p)
            if d in m:
                m[d].append(p)
            else:
                m[d] = [p]
        
        darr = [p for p in m.keys()]
        darr = sorted(darr)
        print(darr)
        print(m)
        ans = []
        for i in darr:
            for d in m[i]:
                if len(ans) == k:
                    break
                ans.append(d)
                
        return ans
        

    def calculate_distance(self, point: list[int]) -> int:
        return round(sqrt((0 - point[0]) ** 2 + (0 - point[1]) ** 2), 2)
