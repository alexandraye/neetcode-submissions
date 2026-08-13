class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurrences_s = {}
        for i in s:
            if i in occurrences_s:
                occurrences_s[i] += 1
            else:
                occurrences_s[i] = 1
        occurrences_t = {}
        for j in t:
            if j in occurrences_t:
                occurrences_t[j] += 1
            else:
                occurrences_t[j] = 1
        return occurrences_s == occurrences_t