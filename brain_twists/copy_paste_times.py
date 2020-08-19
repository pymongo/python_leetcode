"""
初次看到这题，我还以为是用倍增法，例如要生成9个字符，我以我是2**3+1，最后一下鼠标复制一个字符再粘贴
结果这题只能是「全选后复制粘贴」
所以如果n是质数，那就只能就最初的1个字母复制1次，粘贴n-1次
如果n是非质数: 答案就是n分解质因数的因子之和，例如6=2*3，次数是5
"""


class Solution:
    def minSteps(self, n: int) -> int:
        factor_sum = 0
        factor = 2
        while n > 1:
            while n % factor == 0:
                n //= factor
                factor_sum += factor
            factor += 1
        return factor_sum
