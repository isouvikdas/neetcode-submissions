class Solution:
    def findOrder(self, nc: int, pres: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(nc)}
        for crs, pre in pres:
            preMap[crs].append(pre)

        result = []
        visitSet = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visitSet:
                return True
            cycle.add(crs)
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False 
            cycle.remove(crs)
            result.append(crs)
            return True
        
        for crs in range(nc):
            if crs not in visitSet:
                if not dfs(crs): return []
        return result