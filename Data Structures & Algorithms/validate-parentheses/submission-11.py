class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        dic = {')':'(', '}':'{', ']':'['}
        for let in s:
            if let not in dic:
                seen.append(let)
            else:
                if not seen or seen[-1] != dic[let]:
                    return False
                seen.pop()
        return not seen