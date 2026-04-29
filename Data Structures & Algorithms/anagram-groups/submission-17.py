class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ag = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s.lower():
                count[ord(c)-ord('a')] += 1
            ag[tuple(count)].append(s)
        return list(ag.values())

        