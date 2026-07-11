class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        mp: dict[str, List[str]] = {}
        for i in strs:
            word = str(sorted(i))
            if word not in mp:
                mp[word] = []
            mp[word].append(i)
        for k in mp.keys():
            result.append(mp[k])
        return result