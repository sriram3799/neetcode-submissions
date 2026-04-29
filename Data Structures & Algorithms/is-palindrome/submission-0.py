class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2=''
        s1 = ''.join(s.split(' '))
        for a in s1:
            if a.isalnum():
                s2+=a.lower()
        return True if s2 == s2[::-1] else False