import unittest

# 判断某个排列的前面有几个排列
class Solution(unittest.TestCase):
    TESTCASES = [
        ([3,2,1],6)
    ]

    def test(self):
        for nums, output in self.TESTCASES:
            self.assertEqual(output, self.permutation_index(nums))

    @staticmethod
    def permutation_index(nums) -> int:
        n = len(nums)
        factorial = 1
        # 从第一个开始编号
        res = 1

        # 从右往左扫
        # 例如[3,2,1]
        #       ^
        # 2后面有1个比2小: res+=1 * 1!
        # 3后面有2个比3小: res+=2 * 2!
        # 最后res=1+1+4
        for i in range(n - 1, -1, -1):
            smaller_count = 0
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    smaller_count += 1
            res += factorial * smaller_count
            factorial *= (n - i)
        return res
