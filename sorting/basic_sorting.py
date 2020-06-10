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
from typing import List
from pprint import pprint as p
# parent folder的py文件都能被导入... 我还是喜欢Rust的跟文件结构保持一致的包管理
# 我理解为import的root在项目文件夹，所以mydbg能被找到
from mydbg import dbg
# from pydbg import dbg as pydbg


def bubble_sort(numbers: List[int]) -> List[int]:
    """
    平均O(n^2)，最好O(n)，最坏O(n^2)；稳定排序
    Worst Case: 入参是反序的
    """
    length: int = len(numbers)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


def selection_sort(numbers: List[int]) -> List[int]:
    """
    遍历n-1次，第一次遍历找到最小值与索引0进行互换，第二次遍历找到次小值......
    选择排序比冒泡蠢在，当前遍历没有利用上次遍历的结果，而冒泡排序遍历时不断将更大的数换到后面，所以冒泡排序最后的几次遍历耗时很短
    平均/最好/最坏都是O(n^2)；不稳定排序
    「堆排序」是选择排序的更高效算法
    """
    length: int = len(numbers)
    min_index: int
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


def heap_sort(input_numbers: List[int]) -> List[int]:
    """
    ## 堆排序学习资料
    https://www.youtube.com/watch?v=j-DqQcNPGbE

    ## heapq
    有人把上述视频中的build_heap 叫做heapify
    Python heapq 的heapify就是把整个array变成heap
    视频中的heapify 有人喜欢叫成bubble down，因为是value从parent往children走
    然后视频没有cover bubble up。heappop的时候用bubble down
    如果implement heappush的话是需要bubble up

    ## 堆排序的几个概念
    - 完全二叉树: 从上到下，从左到右生成的二叉树
    - 堆的规则/特征: 1. 是个完全二叉树 2. 父节点的数值比子节点大
    - heapify: 将一个完全二叉树的某个节点按堆的规则进行重排，常用于堆的数据发生变化时，需要对变化的节点进行重排

    ## 用数组模拟堆(完全二叉树)
    1. 用数组模拟完全二叉树，从上到下从左到右地编号，假设节点的索引为i，有如下规律
    1.1 i的父节点索引parent=(i-1)/2
    1.2 i的左子节点索引c1=2*i+1
    1.3 i的右子节点索引c2=2*i+2

    ## 时间复杂度分析
    时间复杂度：O(nlog n)O(nlogn)。初始化建堆的时间复杂度为 O(n)O(n)，建完堆以后需要进行 n-1n−1 次调整，
    一次调整（即 maxHeapify）的时间复杂度为 O(logn)O(logn)，
    那么 n-1n−1 次调整即需要 O(nlog n)O(nlogn) 的时间复杂度。因此，总时间复杂度为 O(n+nlog n)=O(nlog n)O(n+nlogn)=O(nlogn)。
    平均/最好/最坏都是O(nlogn)；不稳定排序
    """

    def heapify(nums: List[int], length: int, index: int):
        """
        调整完全二叉树，使二叉树满足堆的第二个条件(父节点的数值比子节点大)
        """
        children_left: int = 2 * index + 1
        children_right: int = 2 * index + 2
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
    last_node_parent: int = (last_node - 1) // 2
    # 从倒数第一个非叶子结点开始遍历(从右到左，从下到上)，建立大根堆，会遍历所有非叶子节点
    # 从左到右开始遍历倒数第二层(k-1)层的子节点，再把 当前节点 和 当前节点的子节点的最大值 做交换
    for i in range(last_node_parent, -1, -1):
        heapify(input_numbers, size, i)
    # p(input_numbers)

    # Step.2 开始真正的堆排序
    # 过程是先将根节点(最大值)与最后的叶节点交换，
    # 然后"剔除"最后的子叶节点，重新heapify根节点(因为发生变化)
    # 由于每次大的都会放到后面，因此最后的input_numbers是从小到大排
    for i in range(size - 1):
        # 根节点(最大值)与最后的叶节点交换
        input_numbers[0], input_numbers[size - 1 - i] = input_numbers[size - 1 - i], input_numbers[0]
        # 由于根节点发生变化，需要重新heapify，注意重新heapify时不要包括已剔除的叶节点
        heapify(input_numbers, size - 1 - i, 0)

    # p(input_numbers)
    return input_numbers


def binary_search(nums: List[int], target: int) -> int:
    left: int = 0
    right: int = len(nums) - 1
    middle: int
    while left < right and right > 1:
        # 如果middle是(left+right) // 2
        # 遇到([1, 2, 3], 4)的测试用例时会陷入死循环(left, right = 1, 2)
        middle = (left + right) // 2
        dbg((left, middle, right))
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


def shell_sort(numbers: List[int]) -> List[int]:
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

    return numbers


def merge_sort(numbers: List[int]) -> List[int]:
    """
    leetcode上耗时 444ms
    官方解答中有一种很巧妙的，借助额外存储空间，直接在原数组上挪位置的解法
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


def quick_sort(nums):
    """
    应对面试时手写快排的背诵版本，所以变量名都用缩写
    """
    size: int = len(nums)
    if size <= 1:
        return nums
    pivot = nums[0]
    left = [nums[i] for i in range(1, size) if nums[i] <= pivot]
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


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([5, 2, 3, 1], [1, 2, 3, 5]),
        ([5, 3, 4, 2], [2, 3, 4, 5]),
        ([3, 2, 1, 4, 5], [1, 2, 3, 4, 5]),
        ([4, 10, 3, 5, 1, 2], [1, 2, 3, 4, 5, 10])
    ]
    BINARY_SEARCH_CASES = [
        {
            "input": ([1, 2, 3], 0),
            "expected": 0
        },
        {
            "input": ([1, 2, 3], 1),
            "expected": 0
        },
        {
            "input": ([1, 2, 3], 2),
            "expected": 1
        },
        {
            "input": ([1, 2, 3], 3),
            "expected": 2
        },
        {
            "input": ([1, 2, 3], 4),
            "expected": 2
        },
    ]

    def test_bubble_sort(self):
        for case in self.TEST_CASES[:]:
            # assertEqual(Expected, Actual)
            # rust的assert_eq!比较直观，不限定左边还是右边放期待值，assert_eq!(Left, Right)
            self.assertEqual(case[1], bubble_sort(case[0]))

    def test_selection_sort(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[1], selection_sort(case[0]))

    def test_heap_sort(self):
        for case in self.TEST_CASES[:]:
            nums = case[0][:]
            heap_sort(nums)
            self.assertEqual(case[1], nums)

    def test_binary_search(self):
        for case in self.BINARY_SEARCH_CASES[:]:
            dbg(case)
            self.assertEqual(case["expected"], binary_search(*case["input"]))

    def test_insertion_sort(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[1], insertion_sort(case[0]))

    def test_shell_sort(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[1], shell_sort(case[0]))

    def test_merge_sort(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[1], merge_sort(case[0]))

    def test_quick_sort_simple(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[1], quick_sort_simple(case[0]))
