"""
01型号背包问题，每个物品只能有选或不选两种状态
在n个物品中挑选若干物品装入容量为m的背包，最多能装多满
dp[i][j]表示从前i个物品中能否装成容量为j的组合
这题的状态转移方程有点像jump game
也可以用状态压缩性DP，每个物品的选或不选刚好是一个二进制，不过时间复杂度n*2^n

01背包问题的题型归纳(小于背包容量的最大值):
1. lintcode_92.Backpack
2.1 某厂面试题<石头碰撞>: 给N个石头，每次选两个碰撞，最后剩余小石头的大小是abs(x-y)，请问最后剩下1个石头的大小是？
其实石头碰撞问题可以想成把数组的数尽可能均分放在两个桶内，然后求两个桶的石头体积之差
2.2 美团最低满减金额: 假设您有一张满X元立减的满减优惠券，请问要怎么点餐才能花钱最少又能享受满减
通常的背包模板要求<=m的最大值，而这题要求>=m的最小值，所以这样转换一下 m=sum(nums)-X
2.3 Google问过的 lintcode_724.Minimum Partition: 和LC416类似，只不过返回值是两部分差值的最小值
2.4 leetcode_416.Partition Equal Subset Sum: 问你能否均分数组，使得两部分的和相等
这题这是问能不能，如果和为奇数就可以提前返回False，然后使用布尔值DP数组即可

以leetcode_416分析0-1背包问题的状态压缩
1. 滚动数组压缩成两行
由于填表时当前行的值只依赖与上一行的值，可以通过「滚动数组」的思路将dp数组压缩成2行
2. 一行状态的压缩方法(需要倒着遍历避免填表时被覆盖掉)
实际上连“滚动数组”都不必，在“填表格”的时候，当前行总是参考了它上面一行 “头顶上” 那个位置和“左上角”某个位置的值。
因此，我们可以只开一个一维数组，从后向前依次填表即可
"""
import unittest
from typing import List


class Solution:

    # noinspection PyMethodMayBeStatic,PyPep8Naming
    @staticmethod
    def backPack(m: int, A: List[int]) -> int:
        """
        @param m: An integer m denotes the size of a backpack
        @param A: Given n items with size A[i]
        @return: The maximum size
        """
        size = len(A)
        # 注意「前缀型」动态规划，i表示前i个物品选或不选，i的长度是len(nums)+1
        dp = [[False] * (m + 1) for _ in range(size + 1)]  # 注意range里面的是行，也就是i
        dp[0][0] = True
        # 开始填表
        for i in range(1, size + 1):
            dp[i][0] = True
            for j in range(1, m + 1):
                # A[i-1]是第i个数的下标
                if j >= A[i - 1]:
                    # 要么前i个数凑出了j的和(第i个数不选的情况) or 前i个数里凑出了j-第i个数的大小的和(第i个数选上的情况)
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
                else:
                    # dp[i - 1][j - A[i - 1]]中j-A[i-1]小于0越界
                    # 既第i个数的物品太大了，放进去超过背包容量j，所以没有将第i个数选上的分支
                    dp[i][j] = dp[i - 1][j]
        for j in range(m, -1, -1):
            if dp[size][j]:
                return j
        return -1

    @staticmethod
    def dp_state_max_capacity_from_ith_num(m: int, nums: List[int]) -> int:
        # dp[i][j]表示前i个数凑出<=j的最大和是多少
        size = len(nums)
        dp = [[0] * (m + 1) for _ in range(size + 1)]
        for i in range(1, size + 1):
            for j in range(1, m + 1):
                if j >= nums[i - 1]:
                    # 这种状态表示不如布尔值之间或运算快
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i - 1]] + nums[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[size][m]

    @staticmethod
    def min_partition(nums: List[int]) -> int:
        """
        本题要求将数组任意分成两部分，要求两部分之和 的差值最小(leetcode 416问你能不能均分)
        实际上可以转化为01背包问题: 从数组中选任意个数，使得和尽可能接近sum(nums)//2
        不过这题的dp状态只能用dp[i][j]表示前i个数凑出<=j的最大和是多少，不能用布尔值

        如果用这种DP方程在lintcode上要特判`if size==209: return 1`和`if size>300: return 0`
        这题size * half_sum的数组太大了，有另一种优化DP数组空间复杂度的思路:
        TODO dpi表示两个集合之差为i的构造方法是否存在, i的范围是0-1, j的范围是sum*2+10(为什么是这样的长度?加滚动数组)
        """
        full_sum = sum(nums)
        half_sum = full_sum // 2
        # sum_a=sum(nums)-dp[size][m], sum_b=sum(nums)-dp[size][m]
        return abs(full_sum - 2 * Solution.dp_state_max_capacity_from_ith_num(half_sum, nums))
        # leetcode 416. Partition Equal Subset Sum
        # return full_sum == 2 * dp[size][half_sum]

    @staticmethod
    def can_partition_sum_equal_rolling_array(nums: List[int]) -> bool:
        """
        滚动数组时间上(1632ms,38%)，比不用滚动数组的(6500ms,垫底)好很多
        """
        size = 0
        total_sum = 0
        for num in nums:
            size += 1
            total_sum += num
        # 如果总和是奇数，怎么分都不相等
        if total_sum % 2 == 1:
            return False
        half_sum = total_sum // 2

        # 实际上dp的值只跟上一行有关，用一个两行的滚动dp数组就够了
        # dp[i][j]表示前i个数能否凑出和为j的组合
        dp = [[False] * (half_sum + 1) for _ in range(2)]

        # 先填好第一行, 然后第二行可以先照抄第一行的值(滚动数组), 第三行抄第二行...
        dp[0][0], dp[1][0] = True, True

        # 0/1 交替出现，这样用两行的dp数组也不会越界
        i, last_i = 0, 1
        # 注意i和row不能弄混，row是数组的下标，i是dp数组的下标(只有0和1)
        for row in range(1, size + 1):
            i, last_i = last_i, i
            for j in range(1, half_sum + 1):
                if j >= nums[row - 1]:
                    dp[i][j] = dp[last_i][j] or dp[last_i][j - nums[row - 1]]
                else:
                    dp[i][j] = dp[last_i][j]
        return dp[size % 2][half_sum]


class Testing(unittest.TestCase):
    TEST_CASES = [
        (10, [3, 4, 8, 5], 9),
        (12, [2, 3, 5, 7], 12),
    ]

    def test(self):
        for m, nums, max_size in self.TEST_CASES:
            self.assertEqual(max_size, Solution.backPack(m, nums))

    def test_min_partition(self):
        self.assertEqual(1, Solution.min_partition([1, 6, 11, 5]))
        self.assertEqual(0, Solution.min_partition([1, 2, 3, 4]))

    def test_can_partition_sum_equal_rolling_array(self):
        self.assertFalse(Solution.can_partition_sum_equal_rolling_array([1, 3, 4, 4]))
        self.assertFalse(Solution.can_partition_sum_equal_rolling_array([2, 2, 3, 5]))
        self.assertTrue(Solution.can_partition_sum_equal_rolling_array([1, 5, 11, 5]))
        self.assertFalse(Solution.can_partition_sum_equal_rolling_array([1, 2, 3, 5]))
