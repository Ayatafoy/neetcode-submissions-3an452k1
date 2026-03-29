class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = [0] * (2 * (10 ** 4))
        for item in nums:
            index = item - 10 ** 4
            counter[index] += 1
        largest = set(heapq.nlargest(k, counter))
        result = []
        for i, item in enumerate(counter):
            if item in largest:
                 result.append(i - 10 ** 4)
        return result
        