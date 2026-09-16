class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        if len(s) != len(t):
            return False
        for char in range(len(s)):
            if s_sorted[char] != t_sorted[char]:
                return False
        return True
        