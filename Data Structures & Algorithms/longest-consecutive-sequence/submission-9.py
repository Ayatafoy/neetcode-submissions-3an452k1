class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        lookup = set(nums)
        begin_sequence = []
        for x in nums:
            if not x - 1 in lookup:
               begin_sequence.append(x) 
        counter = 1
        max_counter = 1
        print(begin_sequence)
        sequences = []
        for k, x in enumerate(begin_sequence):
            sequences.append([])
            for i in range(len(lookup)):
                if x + i + 1 in lookup:
                    sequences[k].append(x + i + 1)
                    counter += 1
                    if counter > max_counter:
                        max_counter = counter
                else:
                    break
            counter = 1
        print(sequences)
        return max_counter