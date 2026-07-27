class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_map = defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            res_map[str(count)].append(s)
        return res_map.values()