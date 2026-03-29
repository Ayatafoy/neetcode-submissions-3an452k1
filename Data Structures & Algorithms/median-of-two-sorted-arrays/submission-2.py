class Solution:
    def findNedianSortedArray(self, nums: List[int]) -> float:
        # print(nums)
        # print(len(nums) % 2)
        # print(len(nums) // 2)
        if len(nums) % 2 == 1:
            median_idx = len(nums) // 2
            median = nums[median_idx]
            # print(median)
        elif len(nums) % 2 == 0:
            median = (nums[(len(nums) - 1) // 2] + nums[len(nums) // 2]) / 2
            # print(median)
        return median
    
    def mergeLists(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0 and len(nums2) == 0:
            return []
        if len(nums1) == 0:
            return nums2
        if len(nums2) == 0:
            return nums1
        result = []
        n = len(nums1) + len(nums2)
        i = 0
        j = 0
        # print(f'n: {n}')
        while i + j <= n - 2:
            # print(f'i: {i}')
            # print(f'j: {j}')
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                if i < len(nums1) - 1:
                    i += 1
                else:
                    result.extend(nums2[j:])
                    break
            else:
                result.append(nums2[j])
                if j < len(nums2) - 1:
                    j += 1
                else:
                    result.extend(nums1[i:])
                    break
            # print(f'result: {result}\n')
            # print(f'------')
        return result
            



    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = self.mergeLists(nums1, nums2)
        print(f'merged_nums: {merged_nums}')
        median = self.findNedianSortedArray(merged_nums)
        return median