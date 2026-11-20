class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            ordered = "".join(sorted(word))
            if ordered in seen:
                seen[ordered].append(word)
            else:
                seen[ordered] = [word]
        
        out = []
        for key in seen:
            out.append(seen[key])
        return out