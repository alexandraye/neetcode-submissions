class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            c1 = s[i]
            c2 = s[j]
            s[i] = c2
            s[j] = c1
            i += 1
            j -= 1
        