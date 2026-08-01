class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix, suffix = 1, 1
        result = []
        for i in nums:
            result.append(prefix)
            prefix *= i

        for i in range(len(nums)-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result