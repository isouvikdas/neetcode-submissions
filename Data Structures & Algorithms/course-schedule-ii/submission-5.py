class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pres in prerequisites:
            preMap[crs].append(pres)

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
            result.append(crs)
            cycle.remove(crs)
            return True
            
        for nc in range(numCourses):
            if nc not in visitSet:
                if not dfs(nc): return []
        return result