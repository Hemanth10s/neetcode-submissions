class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ref_set = set(nums)
        i = 0
        max_length = 0
        for num in ref_set:
            if num -1 not in ref_set:
                length = 1
                while num+length in ref_set:
                    length+=1
                max_length = max(max_length, length)
            i+=1
        return max_length
