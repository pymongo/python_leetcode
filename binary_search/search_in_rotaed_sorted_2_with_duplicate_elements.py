"""
做此题时发现，之前的解答一个都不能用，有序数组中有重复元素时，peak_index和min_index的搜索结果会是错的
这个二分模板是个特例，end的初始值必须是len(nums)而且最坏情况比直接遍历还慢
所以倒不如直接用
return target in nums
在lintcode上都有Your submission beats 91.00% Submissions!的性能
"""
from typing import List


def leetcode_best(nums: List[int], target: int) -> bool:
    size = len(nums)
    if size == 0:
        return False
    # 如果end的初始值不是len(nums)，则二分法循环内不会处理([1],1)和([1,3],3)的输入用例
    start, end = 0, size

    while start < end:
        mid = start + (end - start) // 2
        if target == nums[mid]:
            return True
        # FIXME 注意，处理重复元素！！
        # TODO 注意这个end是动态的
        if nums[start] == nums[mid] == nums[end - 1]:
            start += 1
            end -= 1
            continue
        elif nums[start] <= nums[mid]:
            # 左侧递增
            if nums[start] <= target < nums[mid]:
                end = mid
            else:
                start = mid + 1
        else:
            # 右侧递增
            if nums[mid] < target <= nums[end - 1]:
                start = mid + 1
            else:
                end = mid
    return False
