class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counts = [0]*26
        for cs,ct in zip(s,t):
            counts[ord(cs)-ord('a')]+=1
            counts[ord(ct)-ord('a')]-=1
        for val in counts:
            if val!=0:
                return False
        return True