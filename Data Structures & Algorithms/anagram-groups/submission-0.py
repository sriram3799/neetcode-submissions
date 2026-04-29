from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for w in strs:
            sorted_word = "".join(sorted(w))
            anagram_groups[sorted_word].append(w)
        return list(anagram_groups.values())