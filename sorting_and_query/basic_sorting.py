"""
## 算法的稳定性概念
稳定排序，如果a原本在b前面，而a=b，排序之后a仍然在b的前面；而不稳定排序可能出现在b之后

## 十大排序算法的空间复杂度
除了三大桶排序和归并排序需要额外的空间，其余排序算法都是O(1)而且能在数组内直接排序(in-place)

## 为什么不看桶排序
桶排序平均时间复杂度O(n+k)看似很美，在leetcode上桶排序的速度不如快速排序
计数排序和基数排序的思想跟桶排序类似，可以归为桶排序一类

## Reference:
- https://www.geeksforgeeks.org/selection-sort-vs-bubble-sort/
- https://jianshu.com/p/bbbab7fa77a2
"""
import unittest
from typing import List, Tuple
from pprint import pprint as p
from binary_tree.binary_tree import dbg
from copy import deepcopy


# FIXME 这不是正统的sift_down过程，正规代码请看 collections/my_heap.py
def sift_down(nums: List[int], size: int, index: int):
    while index < size:
        left = index * 2 + 1
        right = left + 1
        max_index = index
        if left < size and nums[left] > nums[max_index]:
            max_index = left
        if right < size and nums[right] > nums[max_index]:
            max_index = right
        # 循环退出条件1. 二叉树节点的根已经是最大值，没有发生交换
        # 循环退出条件2. 二叉树节点的根发生过交换，没有发生交换
        if max_index == index:
            return
        nums[index], nums[max_index] = nums[max_index], nums[index]
        # 当前二叉树节点的值与左儿子或右儿子发生互换，需要检查左儿子或右儿子是否仍能保持堆结构
        index = max_index


# 大根堆/小根堆的heappush/heappop操作跟「优先队列」很像，常常使用heap实现优先队列
# 如果需要删除堆的任意节点，需要额外辅助数据结构才能知道往上或往下调整
def heap_sort_iterative(nums: List[int]):
    """
    大根堆(max_heapify), 大根堆有两个特性:
    1. 要求二叉树必须是完全二叉树(按BFS的顺序遍历不能有None值，也就是从上到下从左到右排列)
    2. 根节点的值比左右子树的值都要大
    以一个值等于下标的二叉树(0(1(3)(4))(2))为例，1在BFS数组中的下标为1
    1的parent的下标为:  (index-1) // 2 = 0 // 2    = 0
    1的左子树节点的下标为: index * 2 + 1 = 1 * 2 + 1 = 3
    1的右子树节点的下标为: index * 2 + 2 = 1 * 2 + 2 = 4
    本题用BFS二叉树得到的数组进行堆排序，堆排序可以分为: heapify和heappop两个过程
    """
    heap_size = len(nums)
    # 从倒数第一个非叶子结点开始遍历(从右到左，从下到上)，并进行heapify
    # 照抄了heapq内部实现，实际上开始位置的索引是size//2 - 1(最深的左叶子节点)
    # step.1 从最后一个非叶子节点往上heapify
    for i in reversed(range(heap_size // 2)):
        # sift/bubble up
        sift_down(nums, heap_size, i)
    # 将heap_size减1使之与heap内最后一个元素的下标值相等，方便下标访问
    heap_size -= 1
    # step.2 heappop: 每次将堆顶(堆的根)弹出与堆最后一个值交换，然后堆的大小减1进行heapify维护堆的特性，数组就划分成两个区域前面是堆，后面是排序好的部分
    while heap_size > 0:
        nums[0], nums[heap_size] = nums[heap_size], nums[0]
        # sift/bubble down
        sift_down(nums, heap_size, 0)
        heap_size -= 1
    # for i in range(heap_size - 1):
    #     nums[0], nums[heap_size - 1 - i] = nums[heap_size - 1 - i], nums[0]
    #     heapify_iterative(nums, heap_size - 1 - i, 0)


def heap_sort(input_numbers: List[int]) -> List[int]:
    """
    https://youtube.com/watch?v=j-DqQcNPGbE
    ## 堆排序的几个概念
    - 完全二叉树: 从上到下，从左到右生成的二叉树
    - 堆的规则/特征: 1. 是个完全二叉树 2. 父节点的数值比子节点大
    - heapify: 将一个完全二叉树的某个节点按堆的规则进行重排，常用于堆的数据发生变化时(例如堆顶被扔掉)，需要对变化的节点进行重排
    ## 时间复杂度分析
    初始化heappush的时间复杂度为O(n*logn)，建完堆以后"排序"heapop需要n-1次，每次需要logn时间复杂度
    那么 n-1n−1 次调整即需要 O(nlog n)O(nlogn) 的时间复杂度。因此，总时间复杂度为 O(n+nlog n)=O(nlog n)O(n+nlogn)=O(nlogn)。
    平均/最好/最坏都是O(nlogn)；不稳定排序
    """

    # sift_down过程: 调整完全二叉树，使二叉树满足堆的第二个条件(父节点的数值比子节点大)
    def heapify(nums: List[int], length: int, index: int):
        children_left: int = 2 * index + 1
        children_right: int = children_left + 1
        # children_right: int = 2 * index + 2
        max_index: int = index
        if children_left < length and nums[children_left] > nums[max_index]:
            max_index = children_left
        if children_right < length and nums[children_right] > nums[max_index]:
            max_index = children_right
        if max_index != index:
            nums[index], nums[max_index] = nums[max_index], nums[index]
            # max_index 节点发生了值变动，重新/再次检查下 max_index 作为的父节点是否满足堆的条件
            # TODO 补充不用递归的写法
            heapify(nums, length, max_index)

    size = len(input_numbers)

    # Step.1 build_heap，如果在C语言里，这一步最好抽取成方法，还有交换变量也要抽取成方法
    last_node: int = size - 1
    last_node_not_leaf: int = (last_node - 1) // 2
    # 从倒数第一个非叶子结点开始遍历(从右到左，从下到上)，建立大根堆，会遍历所有非叶子节点
    # 从左到右开始遍历倒数第二层(k-1)层的子节点，再把 当前节点 和 当前节点的子节点的最大值 做交换
    for i in range(last_node_not_leaf, -1, -1):
        heapify(input_numbers, size, i)

    # Step.2 开始真正的堆排序，过程是先将根节点(最大值)与最后的叶节点交换，
    # 然后"剔除"最后的子叶节点，重新heapify根节点(因为发生变化)
    # 由于每次大的都会放到后面，因此最后的input_numbers是从小到大排
    for i in range(size - 1):
        # 根节点(最大值)与最后的叶节点交换
        input_numbers[0], input_numbers[size - 1 - i] = input_numbers[size - 1 - i], input_numbers[0]
        # 由于根节点发生变化，需要重新heapify，注意重新heapify时不要包括已剔除的叶节点
        heapify(input_numbers, size - 1 - i, 0)

    return input_numbers


def insertion_sort(nums: List[int]) -> List[int]:
    """
    插入排序类型斗地主发牌时，将新的牌插入到已经有序的手牌中
    优化算法是通过binary_search找到插入的索引
    「希尔排序」是插入排序的更高效算法
    由于二分/折半查找只是减少了比较的次数，插入元素时元素的移动也耗费O(n)的时间，所以时间复杂度跟冒泡排序一样
    平均O(n^2)，最好O(n)，最坏O(n^2)；稳定排序
    Worst Case: 入参是反序的
    FIXME 我写的二分插入有点问题，还是用不加二分查找的原始插入排序更好
    """
    def binary_search(nums: List[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1
        middle: int
        while left < right and right > 1:
            # 如果middle是(left+right) // 2
            # 遇到([1, 2, 3], 4)的测试用例时会陷入死循环(left, right = 1, 2)
            middle = (left + right) // 2
            if nums[middle] == target:
                print("nums[middle] == target")
                return middle
            elif nums[middle] > target:
                print("nums[middle] > target")
                right = min(middle, right - 1)
            else:
                print("nums[middle] < target")
                left = max(middle, left + 1)
        print(f"left, right = {left}, {right}")
        # 一般的二分查找找不到是返回return -1
        # 这里我想模仿Rust的二分查找，无论找不找得到，都返回一个应当插入位置的索引
        if nums[left] > target:
            return left
        else:
            return right
    length: int = len(nums)
    current_num: int
    for i in range(1, length):
        print()
        p('==' * 10)
        p((nums[:i], nums[i]))
        binary_search_index = binary_search(nums[:i], nums[i])
        p(f"binary_search_index, i = {binary_search_index}, {i}")
        if binary_search_index < i and nums[binary_search_index] > nums[i]:
            current_num = nums[i]
            # 将比nums[i]更大的元素往右移一格
            for j in range(i, binary_search_index, -1):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            nums[binary_search_index] = current_num
        # List[int]不需要pretty print
        p(nums)
        p('==' * 10)
        print()
    return nums


def shell_sort(numbers: List[int]):
    """
    理解希尔排序的话看图
    https://cnblogs.com/chengxiao/p/6104371.html
    基本思路在于先将间距较大元素进行排序，先保证整体有序
    gap迭代的算法有很多种，这里仅介绍折半式迭代gap
    动态gap的参考代码
    def shell_sort(nums):
        lens = len(nums)
        gap = 1  
        while gap < lens // 3:
            gap = gap * 3 + 1  # 动态定义间隔序列
        while gap > 0:
            for i in range(gap, lens):
                cur_num, pre_index = nums[i], i - gap  # cur_num 保存当前待插入的数
                while pre_index >= 0 and cur_num < nums[pre_index]:
                    nums[pre_index + gap] = nums[pre_index] # 将比 cur_num 大的元素向后移动
                    pre_index -= gap
                nums[pre_index + gap] = cur_num  # 待插入的数的正确位置
            gap //= 3  # 下一个动态间隔
        return nums
    """
    length: int = len(numbers)
    if length < 2:
        return numbers

    gap: int = length // 2

    while gap > 0:
        for i in range(gap, length):
            current_number, left = numbers[i], i - gap
            while left >= 0 and current_number < numbers[left]:
                # 将比current_number大的元素往后移动
                numbers[left + gap] = numbers[left]
                left -= gap
            # 将current_number插入到正确位置
            numbers[left + gap] = current_number
        gap //= 2


# TODO 正统归并排序建议看我leetcode第四题的Rust解法
def merge_sort_best(nums: List[int], start: int, end: int, temp: List[int]):
    if start >= end:
        return
    mid = start + (end - start) // 2

    merge_sort_best(nums, start, mid, temp)
    merge_sort_best(nums, mid + 1, end, temp)

    left, right = start, mid + 1
    temp_index = start
    while left <= mid and right <= end:
        if nums[left] < nums[right]:
            temp[temp_index] = nums[left]
            left += 1
        else:
            temp[temp_index] = nums[right]
            right += 1
        temp_index += 1
    while left <= mid:
        temp[temp_index] = nums[left]
        left += 1
        temp_index += 1
    while right <= end:
        temp[temp_index] = nums[right]
        right += 1
        temp_index += 1
    # 下次归并排序时，temp的值很可能被覆盖掉，此时需要将排好序的temp[start:end+1]赋给nums，使得nums局部有序
    # 其次原因是，先让num部分有序，下次归并排序要排的个数就变少
    # 最后不仅是nums有序，temp也是有序的
    nums[start:end+1] = temp[start:end+1]
    # for i in range(start, end + 1):
    #     nums[i] = temp[i]


def quick_sort_simple(numbers: List[int]) -> List[int]:
    """
    即便是简单版本的快排，速度也是归并排序的10倍，所以同样是nlogn的时间复杂度，差距也会很大
    快排的优化算法(分区)看别人博客: https://jianshu.com/p/bbbab7fa77a2
    ## Q: 如果面试官问代码如何进一步优化
    1. 可以在一次遍历(1次for循环)内生成left_part和right_part
    2. 基准值的取法(不懂的话不要乱回答)
    平均时间复杂度O(nlogn)，实际上比merge_sort快得多，最坏情况是数组完全逆序O(n^2)
    """
    n: int = len(numbers)
    # 递归结束条件
    if n <= 1:
        return numbers
    # 基准值
    pivot: int = numbers[0]
    left_part = [numbers[i] for i in range(1, n) if numbers[i] <= pivot]
    right_part = [numbers[i] for i in range(1, n) if numbers[i] > pivot]

    # 优化点的分区写法，仍是有额外空间，面试时要背In-place的算法
    # for i in range(size):
    #     # 注意right多会放入pivot
    #     if nums[i] >= pivot:
    #         right.append(nums[i])
    #     else:
    #         left.append(nums[i])n
    #
    return quick_sort_simple(left_part) + [pivot] + quick_sort_simple(right_part)


# 在数组内部进行排序，不需要额外开辟存储空间
def quick_sort_in_place(nums: List[int], start, end):
    if start >= end:
        return
    left, right = start, end
    pivot = nums[start + (end - start) // 2]
    while left <= right:
        while left <= right and nums[left] < pivot:
            left += 1
        while left <= right and nums[right] > pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    quick_sort_in_place(nums, start, right)
    quick_sort_in_place(nums, left, end)


class TestSorting(unittest.TestCase):
    NUMS_TEST_CASES: List[List[int]] = [
        [5, 2, 3, 1],
        [5, 3, 4, 2],
        [3, 2, 1, 4, 5],
        [4, 10, 3, 5, 1, 2],
    ]

    def test_heap_sort_iterative(self):
        for nums in deepcopy(self.NUMS_TEST_CASES):
            heap_sort_iterative(nums)
            self.assertListEqual(sorted(nums), nums)

    def test_shell_sort(self):
        for nums in deepcopy(self.NUMS_TEST_CASES):
            sorted_nums = sorted(nums)
            shell_sort(nums)
            self.assertEqual(sorted_nums, nums)

    def test_merge_sort_best(self):
        for nums in deepcopy(self.NUMS_TEST_CASES):
            size = len(nums)
            temp = [-1] * size
            merge_sort_best(nums, 0, size - 1, temp)
            self.assertListEqual(sorted(nums), temp)
            self.assertListEqual(sorted(nums), nums)

    def test_quick_sort_in_place(self):
        for nums in deepcopy(self.NUMS_TEST_CASES):
            quick_sort_in_place(nums, 0, len(nums) - 1)
            self.assertListEqual(sorted(nums), nums)
