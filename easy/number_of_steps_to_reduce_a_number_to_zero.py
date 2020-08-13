# 给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1
# 挑战: 只用位运算的与、或、异或、移位，不用任何四则运算
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num != 0:
            if num % 2 == 1:
                num -= 1
            else:
                num //= 2
            count += 1
        return count

    @staticmethod
    def bitwise_solution(num: int) -> int:
        count = 0
        while num != 0:
            if (num & 1) == 1:
                # num^1 和 num&-2 都表示 num -= 1
                num ^= 1
            else:
                # 移位运算比乘2或除2都要快
                num >>= 1
            count += 1
        return count
