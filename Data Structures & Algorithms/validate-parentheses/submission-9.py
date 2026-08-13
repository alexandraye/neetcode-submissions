class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        dic = {')':'(', '}':'{', ']':'['}
        for let in s:
            if let in dic:
                if not seen or seen[-1] != dic[let]:
                    return False
                seen.pop()
            else:
                seen.append(let)
        return not seen