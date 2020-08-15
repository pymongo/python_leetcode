from typing import List


class Solution:
    @staticmethod
    def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        """
        二分法的伪代码
        nums1.sort()
        nums2.sort()
        last_num_2=0
        for num2 in nums2:
            if num2 == last_num_2:
                continue
            if bsearch(nums1, num2) != -1:
                res.append(num2)
        """
        # set1 = set(nums1)
        # set2 = set(nums2)
        # return list(set2 & set1)
        # 能不能不用额外空间?(除了输入和输出的空间)
        return list(set(nums1).intersection(set(nums2)))

    @staticmethod
    def intersection_2_hashmap(nums1: List[int], nums2: List[int]) -> List[int]:
        # 时间复杂度：O(m+n)
        if len(nums1) > len(nums2):
            return Solution.intersection_2_hashmap(nums2, nums1)

        # 哈希表记录器只遍历较短的数组nums1, 节约空间和时间
        m = dict()
        for num in nums1:
            m[num] = m.get(num, 0) + 1

        intersection = list()
        for num in nums2:
            if m.get(num, 0) > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)

        return intersection
