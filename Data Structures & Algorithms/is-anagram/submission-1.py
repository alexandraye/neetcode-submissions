class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_let = {}
        t_let = {}

        for i in range(len(s)):
            s_let[s[i]] = s_let.get(s[i], 0) + 1
            t_let[t[i]] = t_let.get(t[i], 0) + 1
        
        return s_let == t_let
