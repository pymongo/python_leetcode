"""
## Relative Problems
- [冒泡/选择/插入](https://lintcode.com/problem/sort-integers)
- https://lintcode.com/problem/sort-integers-ii
- https://leetcode.com/problems/sort-an-array/
- https://leetcode-cn.com/problems/sort-an-array/solution/pai-xu-shu-zu-by-leetcode-solution/

## Reference:
https://www.jianshu.com/p/bbbab7fa77a2

## 算法的稳定性概念
稳定排序，如果a原本在b前面，而a=b，排序之后a仍然在b的前面；而不稳定排序可能出现在b之后

## 十大排序算法的空间复杂度
除了三大桶排序和归并排序需要额外的空间，其余排序算法都是O(1)而且能在数组内直接排序(in-place)

## 为什么不看桶排序
桶排序平均时间复杂度O(n+k)看似很美，在leetcode上桶排序的速度不如快速排序
计数排序和基数排序的思想跟桶排序类似，可以归为桶排序一类
"""
import unittest
from typing import List, Tuple
from pprint import pprint as p
from binary_tree.binary_tree import dbg
from copy import deepcopy


# from pydbg import dbg as pydbg


def bubble_sort(nums: List[int]):
    """
    平均O(n^2)，最好O(n)，最坏O(n^2)；稳定排序
    Worst Case: 入参是反序的
    """
    length: int = len(nums)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


def selection_sort(nums: List[int]):
    """
    遍历n-1次，第一次遍历找到最小值与索引0进行互换，第二次遍历找到次小值......
    选择排序比冒泡蠢在，当前遍历没有利用上次遍历的结果，而冒泡排序遍历时不断将更大的数换到后面，所以冒泡排序最后的几次遍历耗时很短
    平均/最好/最坏都是O(n^2)；不稳定排序
    小o表示最好时间复杂度，大O表示最坏时间复杂度
    「堆排序」是选择排序的更高效算法
    """
    length: int = len(nums)
    min_index: int
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]


# sift_down过程
def heapify_iterative(nums: List[int], size: int, index: int):
    while True:
        left = index * 2 + 1
        right = index * 2 + 2
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
# 优先队列/堆的常见应用:
# 1. Dijkstra’s algorithm(单源最短路问题中需要在邻接表中找到某一点的最短邻接边，这可以将复杂度降低)
# 2. Huffman coding(出现频率高的字符权重更高)(贪心算法的一个典型例子，采用优先队列构建最优的前缀编码树(prefixEncodeTree))
# 3. Prim’s algorithm for minimum spanning tree
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
    用内置库heapq进行堆排序的过程:
    heap_nums = []
    for num in nums: heapq.heappush(heap_nums, num)
    sorted_nums = [heapq.heappop(heap_nums) for _ in range(len(heap_nums))]
    """
    heap_size = len(nums)
    # 从倒数第一个非叶子结点开始遍历(从右到左，从下到上)，并进行heapify
    # 照抄了heapq内部实现，实际上开始位置的索引是size//2 - 1(最深的左叶子节点)
    # step.1 从最后一个非叶子节点往上heapify
    for i in reversed(range(heap_size // 2)):
        # sift/bubble up
        heapify_iterative(nums, heap_size, i)
    # 将heap_size减1使之与heap内最后一个元素的下标值相等，方便下标访问
    heap_size -= 1
    # step.2 heappop: 每次将堆顶(堆的根)弹出与堆最后一个值交换，然后堆的大小减1进行heapify维护堆的特性，数组就划分成两个区域前面是堆，后面是排序好的部分
    while heap_size > 0:
        nums[0], nums[heap_size] = nums[heap_size], nums[0]
        # sift/bubble down
        heapify_iterative(nums, heap_size, 0)
        heap_size -= 1
    # for i in range(heap_size - 1):
    #     nums[0], nums[heap_size - 1 - i] = nums[heap_size - 1 - i], nums[0]
    #     heapify_iterative(nums, heap_size - 1 - i, 0)


def heap_sort(input_numbers: List[int]) -> List[int]:
    """
    https://www.youtube.com/watch?v=j-DqQcNPGbE
    ## 堆排序的几个概念
    - 完全二叉树: 从上到下，从左到右生成的二叉树
    - 堆的规则/特征: 1. 是个完全二叉树 2. 父节点的数值比子节点大
    - heapify: 将一个完全二叉树的某个节点按堆的规则进行重排，常用于堆的数据发生变化时(例如堆顶被扔掉)，需要对变化的节点进行重排

    ## 时间复杂度分析
    初始化heappush的时间复杂度为O(n*logn)，建完堆以后"排序"heapop需要n-1次，每次需要logn时间复杂度
    那么 n-1n−1 次调整即需要 O(nlog n)O(nlogn) 的时间复杂度。因此，总时间复杂度为 O(n+nlog n)=O(nlog n)O(n+nlogn)=O(nlogn)。
    平均/最好/最坏都是O(nlogn)；不稳定排序
    """

    # sift_down过程
    def heapify(nums: List[int], length: int, index: int):
        """
        调整完全二叉树，使二叉树满足堆的第二个条件(父节点的数值比子节点大)
        """
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
    # p(input_numbers)

    # Step.2 开始真正的堆排序，过程是先将根节点(最大值)与最后的叶节点交换，
    # 然后"剔除"最后的子叶节点，重新heapify根节点(因为发生变化)
    # 由于每次大的都会放到后面，因此最后的input_numbers是从小到大排
    for i in range(size - 1):
        # 根节点(最大值)与最后的叶节点交换
        input_numbers[0], input_numbers[size - 1 - i] = input_numbers[size - 1 - i], input_numbers[0]
        # 由于根节点发生变化，需要重新heapify，注意重新heapify时不要包括已剔除的叶节点
        heapify(input_numbers, size - 1 - i, 0)

    return input_numbers


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
    https://www.cnblogs.com/chengxiao/p/6104371.html
    基本思路在于先将间距较大元素进行排序，先保证整体有序
    gap迭代的算法有很多种，这里仅介绍折半式迭代gap
    动态gap的参考代码
    ```python
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
    ```
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


def merge_sort(numbers: List[int]) -> List[int]:
    """
    leetcode上耗时 444ms
    官方解答中有一种很巧妙的，借助额外存储空间，直接在原数组上挪位置的解法
    Meger Sort的后半部分(归并)又是leetcode上merge two sorted array这题
    """
    length: int = len(numbers)
    # 递归结束条件
    if length <= 1:
        return numbers

    middle = length // 2
    left_arr = merge_sort(numbers[:middle])
    right_arr = merge_sort(numbers[middle:])

    # 通过双指针合并左右两半的有序数组
    # 合并两个有序数组的算法可以参考leetcode上merge-sorted-array这题
    # https://leetcode.com/problems/merge-sorted-array/
    left_ptr, right_ptr = 0, 0
    left_len, right_len = len(left_arr), len(right_arr)
    result: List[int] = []
    while left_ptr < left_len and right_ptr < right_len:
        if left_arr[left_ptr] < right_arr[right_ptr]:
            result.append(left_arr[left_ptr])
            left_ptr += 1
        else:
            result.append(right_arr[right_ptr])
            right_ptr += 1
    # 剩余的元素直接添加到末尾
    result = result + left_arr[left_ptr:] + right_arr[right_ptr:]

    return result


def merge_sort_2(nums: List[int], start: int, end: int, temp: List[int]):
    if start >= end:
        return
    mid = start + (end - start) // 2

    merge_sort_2(nums, start, mid, temp)
    merge_sort_2(nums, mid+1, end, temp)

    left, right = start, mid+1
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
    for i in range(start, end+1):
        nums[i] = temp[i]

def quick_sort(nums):
    """
    应对面试时手写快排的背诵版本，所以变量名都用缩写
    平均时间复杂度O(nlogn)，实际上比merge_sort快得多，最坏情况是数组完全逆序O(n^2)
    """
    size: int = len(nums)
    if size <= 1:
        return nums
    pivot = nums[0]
    left = [nums[i] for i in range(1, size) if nums[i] <= pivot]
    # 注意分区时要考虑[1,1,1,1,1,2]这样的极端情况，左半部分一定要 <= pivot才能避免这种极端情况，避免左边分区和右边分区没有交集
    right = [nums[i] for i in range(1, size) if nums[i] > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort_simple(numbers: List[int]) -> List[int]:
    """
    leetcode上耗时 44ms
    即便是简单版本的快排，速度也是归并排序的10倍，所以同样是nlogn的时间复杂度，差距也会很大
    快排的优化算法(分区)看别人博客
    https://www.jianshu.com/p/bbbab7fa77a2
    ## Q: 如果面试官问代码如何进一步优化
    1. 可以在一次遍历(1次for循环)内生成left_part和right_part
    2. 基准值的取法(不懂的话不要乱回答)
    """
    length: int = len(numbers)
    # 递归结束条件
    if length <= 1:
        return numbers
    # 基准值
    pivot: int = numbers[0]
    left_part = [numbers[i] for i in range(1, length) if numbers[i] <= pivot]
    right_part = [numbers[i] for i in range(1, length) if numbers[i] > pivot]
    return quick_sort_simple(left_part) + [pivot] + quick_sort_simple(right_part)


def quick_sort_recipe(nums: List[int]) -> List[int]:
    size = len(nums)
    # 递归结束条件
    if size <= 1:
        return nums
    pivot = nums[0]
    left = []
    right = []

    for i in range(size):
        # 注意right多会放入pivot
        if nums[i] >= pivot:
            # 如果是Rust，clippy会提示这里用enumerate性能更好
            right.append(nums[i])
        else:
            left.append(nums[i])
    return quick_sort_recipe(left) + [pivot] + quick_sort_recipe(right[1:])


# 在数组内部进行排序，不需要额外开辟存储空间
def quick_sort_in_place(nums: List[int], start, end):
    if start >= end:
        return
    left, right = start, end
    pivot = nums[(left + right) // 2]
    while left <= right:
        while left <= right and nums[left] < pivot:
            left += 1
        while left <= right and nums[right] > pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    print(start, end, left, right)
    quick_sort_in_place(nums, start, right)
    quick_sort_in_place(nums, left, end)


class TestSorting(unittest.TestCase):
    NUMS_TEST_CASES: List[List[int]] = [
        [5, 2, 3, 1],
        [5, 3, 4, 2],
        [3, 2, 1, 4, 5],
        [4, 10, 3, 5, 1, 2],
    ]
    BINARY_SEARCH_TEST_CASES: List[Tuple[List[int], int, int]] = [
        ([1, 2, 3], 0, 0),
        ([1, 2, 3], 1, 0),
        ([1, 2, 3], 2, 1),
        ([1, 2, 3], 3, 2),
        ([1, 2, 3], 4, 2),
    ]

    def test_bubble_sort(self):
        print("test_bubble_sort")
        for nums in deepcopy(self.NUMS_TEST_CASES):
            dbg(nums)
            sorted_nums = sorted(nums)
            bubble_sort(nums)
            dbg(nums)
            self.assertListEqual(sorted_nums, nums)

    def test_selection_sort(self):
        for nums in deepcopy(self.NUMS_TEST_CASES):
            bubble_sort(nums)
            self.assertListEqual(sorted(nums), nums)

    def test_heap_sort_iterative(self):
        for nums in deepcopy(self.NUMS_TEST_CASES):
            heap_sort_iterative(nums)
            self.assertListEqual(sorted(nums), nums)

    def test_heap_sort(self):
        for nums in deepcopy(self.NUMS_TEST_CASES):
            sorted_nums = sorted(nums)
            heap_sort(nums)
            self.assertListEqual(sorted_nums, nums)

    @unittest.skip("跟Rust的binary_search的行为不一致")
    def test_binary_search(self):
        for nums, target, expected in deepcopy(self.BINARY_SEARCH_TEST_CASES):
            self.assertListEqual(expected, binary_search(nums, target))

    @unittest.skip("二分查找有问题，插入排序用到了二分查找的函数，等待修复")
    def test_insertion_sort(self):
        for nums, expected in deepcopy(self.NUMS_TEST_CASES):
            self.assertEqual(expected, insertion_sort(nums))

    def test_shell_sort(self):
        for nums in deepcopy(self.NUMS_TEST_CASES):
            sorted_nums = sorted(nums)
            shell_sort(nums)
            self.assertEqual(sorted_nums, nums)

    @unittest.skip("修复中")
    def test_merge_sort(self):
        for nums in deepcopy(self.NUMS_TEST_CASES):
            self.assertEqual(nums, merge_sort(nums))

    def test_merge_sort_2(self):
        for nums in deepcopy(self.NUMS_TEST_CASES):
            size = len(nums)
            temp = [-1] * size
            merge_sort_2(nums, 0, size-1, temp)
            self.assertListEqual(sorted(nums), temp)
            self.assertListEqual(sorted(nums), nums)

    @unittest.skip("修复中")
    def test_quick_sort_simple(self):
        import sys
        print('python import paths:')
        for path in sys.path:
            print(path)
        for nums, expected in deepcopy(self.NUMS_TEST_CASES):
            self.assertEqual(expected, quick_sort_simple(nums))

    @unittest.skip("修复中")
    def test_quick_sort_recipe(self):
        for nums, expected in deepcopy(self.NUMS_TEST_CASES):
            self.assertEqual(expected, quick_sort_recipe(nums))

    def test_quick_sort_in_place(self):
        for nums in deepcopy(self.NUMS_TEST_CASES):
            quick_sort_in_place(nums, 0, len(nums) - 1)
            self.assertListEqual(sorted(nums), nums)
