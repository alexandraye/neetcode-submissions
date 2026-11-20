class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            if num in seen:
                return [min(seen[num],i), max(seen[num],i),]
            else:
                rest = target - num
                seen[rest] = i