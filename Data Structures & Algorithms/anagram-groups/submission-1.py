class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        result = []
        for i in strs:
            original = i
            new = str(sorted(i))
            if new not in m:
                m[new] = []
            m[new].append(original)
        for i in m:
            result.append(m[i])
        return result