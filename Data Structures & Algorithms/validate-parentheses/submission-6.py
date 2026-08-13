class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        dic = {')':'(', '}':'{', ']':'['}
        for let in s:
            if let not in dic:
                seen.append(let)
            elif not seen:
                return False
            elif seen[-1] == dic[let]:
                seen.pop()
            else:
                return False
        return seen == []