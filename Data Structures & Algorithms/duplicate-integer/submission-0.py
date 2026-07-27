class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        num_count = dict()
        for num in nums:
            if num not in num_count:
                num_count[num]=1
            else:
                print(num)
                return True
        return False
         