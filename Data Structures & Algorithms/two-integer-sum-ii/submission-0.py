class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = defaultdict()

        for i,j in enumerate(numbers):
            diff = target - j
            if diff in seen:
                return[seen[diff]+1, i+1]
            seen[j] = i
        return []