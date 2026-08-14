class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
    
        for char in s:
            if char.isalnum():
                clean += char.lower()
        
        for i in range(len(clean)//2):
            j = len(clean) - 1 - i
            if clean[i] != clean[j]:
                return False
        return True
