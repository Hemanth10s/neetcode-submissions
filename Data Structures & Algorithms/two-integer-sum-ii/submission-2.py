class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        store={}
        for i,j in enumerate(numbers):
            if target - j not in store:
                store[j] = i
            else:
                return [store[target-j]+1, i+1]
        return []