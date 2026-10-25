class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [None] * len(nums)
        suffix = [None] * len(nums)
        out = [None] * len(nums)
        prod = 1

        for i, num in enumerate(nums):
            prefix[i] = prod
            prod *= num

        j = len(nums) - 1
        prod = 1
        while j >= 0:
            suffix[j] = prod
            prod *= nums[j]
            j -= 1

        for k in range(len(nums)):
            out[k] = prefix[k] * suffix[k]
        
        return out