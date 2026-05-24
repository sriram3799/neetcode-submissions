class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s)<len(t):
            return ""
        need = collections.Counter(t)
        have = collections.defaultdict(int)
        formed = 0
        required = len(need)
        res_start,res_len = 0,float("inf")
        i = 0

        for j,c in enumerate(s):
            if c in need:
                have[c]+=1
                if have[c] == need[c]:
                    formed+=1
                while formed == required:
                    if j-i+1 < res_len:
                        res_start=i
                        res_len = j-i+1
                    left = s[i]
                    if left in need:
                        have[left] -= 1
                        if have[left] < need[left]:
                            formed-=1
                    i+=1
        return "" if res_len == float("inf") else s[res_start:res_start+res_len]

