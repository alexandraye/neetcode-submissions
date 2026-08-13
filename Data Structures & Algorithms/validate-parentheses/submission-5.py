class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        dic = {')':'(', '}':'{', ']':'['}
        for let in s:
            if let not in dic:
                seen += let
            elif seen == [] and let in dic:
                return False
            elif seen[-1] == dic[let]:
                seen = seen[:-1]
            else:
                return False
        return seen == []