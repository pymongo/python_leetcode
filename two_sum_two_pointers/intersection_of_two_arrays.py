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
        # set1, set2 = set(nums1), set(nums2)
        # return list(set2 & set1)
        # 能不能不用额外空间?(除了输入和输出的空间)
        return list(set(nums1).intersection(set(nums2)))

    @staticmethod
    def intersection_2_two_pointers(nums1: List[int], nums2: List[int]) -> List[int]:
        # 时间复杂度O(nlogn+mlogm)
        nums1.sort()
        nums2.sort()
        i, j, m, n = 0, 0, len(nums1), len(nums2)

        res = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res

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

    @staticmethod
    def intersection_k_arrays(arrs: List[List[int]]) -> int:
        k = len(arrs)
        m = dict()
        for i in range(k):
            for num in arrs[i]:
                m[num] = m.get(num, 0) + 1

        res = 0
        for count in m.values():
            # 由于本题入参中没有重复，所以出现k次的数字一定是在每个数组中各出现一次
            if count == k:
                res += 1
        return res
