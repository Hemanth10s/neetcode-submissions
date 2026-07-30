class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count_map = Counter(nums)

        freq_list = [[] for i in range(len(nums)+1)]

        for num,count in num_count_map.items():
            freq_list[count].append(num)

        result = []

        print(freq_list)

        for i in range(len(nums), 0, -1):
            for j in freq_list[i]:
                result.append(j)
                if (len(result)==k):
                    return result
        return result