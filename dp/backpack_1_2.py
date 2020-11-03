"""
01型号背包问题，每个物品只能有选或不选两种状态
在n个物品中挑选若干物品装入容量为m的背包，最多能装多满
dp[i][j]表示从前i个物品中能否装成容量为j的组合
这题的状态转移方程有点像jump game
也可以用状态压缩性DP，每个物品的选或不选刚好是一个二进制，不过时间复杂度n*2^n

01背包问题的题型归纳(小于背包容量的最大值):
1.1 lintcode_92.Backpack
1.2 最低满减金额: 假设您有一张满X元立减的满减优惠券，请问要怎么点餐才能花钱最少又能享受满减
通常的背包模板要求<=m的最大值，而这题要求>=m的最小值，所以这样转换一下 m=sum(nums)-X

# 2.x leetcode: 1049,416,494 和 lintcode: 724这三题几乎一样
2.1 leetcode_1049.Last Stone Weight II: 给N个石头，每次选两个碰撞，最后剩余小石头的大小是abs(x-y)，请问最后剩下1个石头的大小是？
其实石头碰撞问题可以想成把数组的数尽可能均分放在两个桶内，然后求两个桶的石头体积之差
2.2 lintcode_724.Minimum Partition: 和LC416类似，只不过返回值是两部分差值的最小值
2.3 leetcode_416/lintcode_588.Partition Equal Subset Sum: 问你能否均分数组，使得两部分的和相等
这题这是问能不能，如果和为奇数就可以提前返回False，然后使用布尔值DP数组即可
2.4 leetcode_496: 这题跟1049石头碰撞一样

3. 0-1背包问题物品带价值(lintcode_backpack_2)
4. 多重背包问题物品带价值且可以选多次(lintcode_backpack_3)
此时最佳算法应该是计算单位体积下最贵的物品，先放入最贵重的直到放不下，再放次贵重的，直到放满(贪心)

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

    # backpack问题2: 物品带价值的背包问题
    # noinspection PyMethodMayBeStatic,PyPep8Naming
    @staticmethod
    def back_pack_with_value(m: int, nums: List[int], values: List[int]) -> int:
        size = len(nums)
        # dp[j] 表示凑出容量<=j的物品组合中的最大价值
        dp = [0] * (m + 1)
        dp[0] = 0
        for i in range(size):
            curr_num = nums[i]
            # Python倒着遍历就用while循环吧，多写几行至少不容易出错
            j = m
            while j >= curr_num:
                # 状态转移方程的唯一区别是选择第i个物品的情况要加上values[i]
                # 所以状态是容量时选择第i个物品加上容量nums[i]，状态是价值时就加上价值values[i]
                # TODO 展开写法是 dp[j] = max(dp[j-0*nums[i]]+0*values[i], dp[j-1*nums[i]]+1*values[i])
                dp[j] = max(dp[j], dp[j - curr_num] + values[i])
                j -= 1
        return dp[m]

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
    def stone_weight_2(nums: List[int]) -> int:
        """
        本题要求将数组任意分成两部分，要求两部分之和 的差值最小(leetcode 416问你能不能均分)
        实际上可以转化为01背包问题: 从数组中选任意个数，使得和尽可能接近sum(nums)//2
        不过这题的dp状态只能用dp[i][j]表示前i个数凑出<=j的最大和是多少，不能用布尔值

        如果用这种DP方程在lintcode上要特判`if size==209: return 1`和`if size>300: return 0`
        这题size * half_sum的数组太大了，有另一种优化DP数组空间复杂度的思路:
        """
        full_sum = sum(nums)
        half_sum = full_sum // 2
        # sum_a=sum(nums)-dp[size][m], sum_b=sum(nums)-dp[size][m]
        return abs(full_sum - 2 * Solution.dp_state_max_capacity_from_ith_num(half_sum, nums))
        # leetcode 416. Partition Equal Subset Sum
        # return full_sum == 2 * dp[size][half_sum]

    @staticmethod
    def min_partition_traverse(nums: List[int]) -> int:
        # 有点脑筋急转弯的遍历/迭代解法, 不断将x+y弄大到接近sum(nums)//2
        # 这种解法不能用地板除
        target = sum(nums) / 2.0
        candidates = set()
        candidates.add(0)
        for num in nums:
            addition = set()
            for candidate in candidates:
                temp_sum = num + candidate
                if temp_sum == target:
                    return 0
                elif temp_sum < target:
                    addition.add(temp_sum)
            # 有点像穷举所有加的情况，组合数的树状图扩散，例如一开始只有0+1，然后第二层是0+2和1+2等等
            candidates = candidates.union(addition)
        return int(2 * (target - max(candidates)))

    @staticmethod
    def min_partition_best_one_row_dp(nums: List[int]) -> int:
        size, total_sum = len(nums), sum(nums)
        half_sum = total_sum // 2
        dp = [0] * (half_sum + 1)
        for num in nums:
            for j in range(half_sum, num - 1, -1):
                dp[j] = max(dp[j], dp[j - num] + num)
        return total_sum - 2 * dp[half_sum]

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
        # FIXME 一定要区分开dp数组的下标和原数组的下标
        for row in range(1, size + 1):
            i, last_i = last_i, i
            for j in range(1, half_sum + 1):
                if j >= nums[row - 1]:
                    dp[i][j] = dp[last_i][j] or dp[last_i][j - nums[row - 1]]
                else:
                    dp[i][j] = dp[last_i][j]
        return dp[size % 2][half_sum]

    @staticmethod
    def can_partition_one_row_dp(nums: List[int]) -> bool:
        size, total_sum = len(nums), sum(nums)
        # 如果总和是奇数，怎么分都不相等
        if total_sum % 2 == 1:
            return False
        half_sum = total_sum // 2

        # dp[i][j]表示前i个数能否凑出和为j的组合
        dp = [False] * (half_sum + 1)
        dp[0] = True
        for i in range(1, size):
            # 「倒着遍历」的好处: 新的值依赖靠左部分老的值，不会出现覆盖现象
            # 遍历范围: j in [half_sum..=half_sum-nums[i] for (int j = half_sum; nums[i] <= j; j--)
            j = half_sum
            curr_num = nums[i]
            while j >= curr_num:
                dp[j] = dp[j] or dp[j - curr_num]
                if dp[half_sum]:
                    return True
                j -= 1
        # return dp[half_sum]
        return False

    @staticmethod
    def can_partition_dfs_solution(nums: List[int]) -> bool:
        """
        DFS思路: 数组逆序排好后，能以最少的递归次数找到 K sum = target
        将本题变向转为k sum = target, 这是本题最快的思路，比DP一维状态还要快20多倍
        TODO 实在想不到DP的状态转移方程，用DFS也是一种不错的选择
        """
        size, full_sum = len(nums), sum(nums)
        if full_sum % 2 == 1:
            return False
        half_sum = full_sum // 2
        nums.sort(reverse=True)
        # 如果是一头大一头小，也找不到均分方案
        if nums[0] > half_sum:
            return False

        def dfs(start_index: int, target: int) -> bool:
            if target == 0:
                return True
            if start_index == size:
                return False

            for i in range(start_index, size):
                next_target = target - nums[i]
                if next_target < 0:
                    break
                # 这里类似于DFS组合数的搜索
                if dfs(i + 1, next_target):
                    return True
            return False

        return dfs(0, half_sum)

    @staticmethod
    def lintcode_backpack_1(m: int, nums: List[int]) -> int:
        """
        求容量为m的背包最大能装多少
        """
        # dp[i]表示容量为i的背包最大能装多少
        dp = [0] * (m + 1)
        for num in nums:
            for j in range(m, num - 1, -1):
                dp[j] = max(dp[j], dp[j - num] + num)
        return dp[m]

    @staticmethod
    def lintcode_backpack_2(m: int, nums: List[int], values: List[int]) -> int:
        """
        求容量为m的背包最大能装的最大物品价值
        """
        dp = [0] * (m + 1)
        for i, num in enumerate(nums):
            for j in range(m, num - 1, -1):
                dp[j] = max(dp[j], dp[j - num] + values[i])
        return dp[m]

    @staticmethod
    def lintcode_backpack_3(capacities: List[int], values: List[int], m: int) -> int:
        """
        物品可选多次，求容量为m的背包最大能装的最大物品价值
        TODO 注意完全背包问题的滚动数组一般都可以正常顺序填表(参考零钱兑换问题)
        """
        dp = [0] * (m + 1)
        for capacity, value in zip(capacities, values):
            # 内层第一次遍历能考虑到物品1选0-k次后最大价值的情况，依次叠加多选一个物品的影响
            for j in range(capacity, m + 1):
                # 如果上次选了物品1的是最大值，那么这次就能选到两次物品1
                dp[j] = max(dp[j], dp[j - capacity] + value)
        return dp[m]

    @staticmethod
    def lintcode_backpack_4(nums: List[int], m: int) -> int:
        """
        物品可选多次，求装满容量为m的背包的方案总数
        此题与零钱兑换2完全一样
        """
        dp = [0] * (m + 1)
        dp[0] = 1
        for num in nums:
            for i in range(num, m + 1):
                dp[i] += dp[i - num]
        return dp[m]

    @staticmethod
    def lintcode_backpack_5(nums: List[int], m: int) -> int:
        """
        求装满容量为m的背包的方案总数
        此题与backpack_4的区别在于物品最多选1次，所以只能倒着遍历
        """
        dp = [0] * (m + 1)
        dp[0] = 1
        for num in nums:
            for j in range(m, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[m]

    @staticmethod
    def lintcode_backpack_6(nums: List[int], m: int) -> int:
        """
        此题与 combination sum IV相同
        TODO 可以先背结论: dp数组下标->coins的遍历顺序能得到更多的方案数，会把[1,2]和[2,1]当作组合数的两种方案
        """
        dp = [0] * (m + 1)
        dp[0] = 1

        for i in range(1, m + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[m]


class Testing(unittest.TestCase):
    TESTCASES = [
        (10, [3, 4, 8, 5], 9),
        (12, [2, 3, 5, 7], 12),
    ]

    MIN_PARTITION_CASES = [
        ([1, 6, 11, 5], 1),
        ([1, 2, 3, 4], 0),
    ]

    CAN_PARTITIONS_CASES = [
        ([1, 3, 4, 4], False),
        ([3, 3, 3, 4, 5], True),
        ([1, 2, 5], False),
        ([2, 2, 3, 5], False),
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
    ]

    def test_backpack(self):
        for m, nums, max_size in self.TESTCASES:
            self.assertEqual(max_size, Solution.backPack(m, nums))

    def test_backpack_with_value(self):
        self.assertEqual(133, Solution.back_pack_with_value(100, [77, 22, 29, 50, 99], [92, 22, 87, 46, 90]))
        self.assertEqual(9, Solution.back_pack_with_value(10, [2, 3, 5, 7], [1, 5, 2, 4]))
        self.assertEqual(10, Solution.back_pack_with_value(10, [2, 3, 8], [2, 5, 8]))

    def test_min_partition(self):
        for nums, min_diff in self.MIN_PARTITION_CASES:
            self.assertEqual(min_diff, Solution.stone_weight_2(nums))

    def test_min_partition_one_row_dp(self):
        for nums, min_diff in self.MIN_PARTITION_CASES:
            self.assertEqual(min_diff, Solution.min_partition_best_one_row_dp(nums))

    def test_can_partition_sum_equal_rolling_array(self):
        for nums, can_partition in self.CAN_PARTITIONS_CASES:
            self.assertEqual(can_partition, Solution.can_partition_sum_equal_rolling_array(nums))

    def test_can_partition_one_row_dp(self):
        for nums, can_partition in self.CAN_PARTITIONS_CASES:
            self.assertEqual(can_partition, Solution.can_partition_one_row_dp(nums))

    def test_can_partition_dfs(self):
        for nums, can_partition in self.CAN_PARTITIONS_CASES:
            print(nums)
            self.assertEqual(can_partition, Solution.can_partition_dfs_solution(nums))
