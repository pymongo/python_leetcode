"""
https://leetcode.com/problems/super-egg-drop
https://lintcode.com/problem/drop-eggs-ii/description
https://nowcoder.com/test/question/done?tid=33908902&qid=368104
"""
import sys
import math


class Solution:
    # 尝试次数=n, height = n(n+1)/2，然后用求根公式
    @staticmethod
    def try_times(height: int) -> int:
        return math.ceil((-1 + math.sqrt(1 + 8 * height)) / 2)

    @staticmethod
    def newcoder_paypal_2019_1(k: int, h: int) -> int:
        """
        k=1 ,h=1000 => 1000
        k=15,h=1000 => 10
        k=2 ,h=1000 => 45
        k=2 ,h=1100 => 47
        k=5 ,h=1000 => 11
        k=5 ,h=1100 => 12
        :param k: 试验鸡蛋的个数
        :param h: 楼层高度
        :return: 最坏需要测试的次数
        """
        expected_times = math.ceil(math.log2(h))
        if k >= expected_times:
            return expected_times
        else:
            return h // k


if __name__ == '__main__':
    # stdin_input: List[str]
    stdin_input = sys.stdin.readlines()
    times, input_height = stdin_input[0].split(' ')
    times = int(times)
    input_height = int(input_height.replace('\n', ''))
    assert isinstance(times, int)
    assert isinstance(input_height, int)

    print(Solution.newcoder_paypal_2019_1(times, input_height))

'''标准答案
k, h = [int(x) for x in input().split()]
dp = [1]*(k+1)
cnt = 1
while dp[k] < h:
    cnt += 1
    dp_i_1 = dp[:]
    dp[1] = cnt
    for j in range(2,k+1):
        dp[j] = dp_i_1[j-1] + dp_i_1[j] + 1
print(cnt)
'''
