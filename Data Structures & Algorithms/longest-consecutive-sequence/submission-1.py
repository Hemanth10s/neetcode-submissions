class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ref_set = set(nums)

        i = 0
        max_length = 0
        while i<len(nums):
            j=nums[i]
            if j-1 not in ref_set:
                length = 1
                while j+1 in ref_set:
                    j+=1
                    length+=1
                max_length = max(max_length, length)
            i+=1
        return max_length
