class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0

        for i in nums:
            if i != 0:
                product *= i
            else:
                zero_count += 1
        
        if zero_count > 1: return [0] * len(nums)

        result = []

        print(product)

        for i in nums:
            if zero_count and i != 0:
                result.append(0)
            elif zero_count and i == 0:
                result.append(product)
            else:
                result.append(product // i)
        
        return result