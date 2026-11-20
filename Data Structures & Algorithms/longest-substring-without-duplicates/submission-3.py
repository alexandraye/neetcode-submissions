class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_out = 0
        l = 0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            
            max_out = max(r - l + 1, max_out)
            seen[s[r]] = r

        return max_out
