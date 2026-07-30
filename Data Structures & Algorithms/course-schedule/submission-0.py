class Solution:
    def canFinish(self, nc: int, pres: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(nc)}
        for crs, pre in pres:
            preMap[crs].append(pre)
        
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(nc):
            if not dfs(crs): return False
        return True