from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # set1 = set(nums1)
        # set2 = set(nums2)
        # return list(set2 & set1)
        # 能不能不用额外空间?(除了输入和输出的空间)
        return list(set(nums1).intersection(set(nums2)))
