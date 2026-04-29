from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ag = defaultdict(list)
        for s in strs:
            sw = "".join(sorted(s))
            ag[sw].append(s)
        return list(ag.values())
