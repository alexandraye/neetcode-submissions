class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1] * length
        suffix = [1] * length
        result = [1] * length

        prefix[1] = nums[0]
        for l in range(2, length):
            prefix[l] = nums[l-1] * prefix[l-1]
        
        r = length - 3
        suffix[-2] = nums [-1]
        while r >= 0:
            suffix[r] = nums[r+1] * suffix[r+1]
            r -= 1

        for i in range(length):
            result[i] = suffix[i] * prefix[i]
        
        return result