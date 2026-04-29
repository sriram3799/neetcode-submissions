from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ag = defaultdict(list)
        for s in strs:
            count = [0]*52
            for c in s:
                if 'A' <= c <= 'Z':
                    count[ord(c) - ord('A')] += 1
                elif 'a' <= c <= 'z':
                    count[ord(c) - ord('a') + 26] += 1
            ag[tuple(count)].append(s)
        return list(ag.values())
