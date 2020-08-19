class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum, product = 0, 1
        while n != 0:
            digit = n % 10
            # 尽管题目要求逆序(左往右)累加累乘每位，
            # 但是由于加法和乘法的各项可以互换，所以我右往左遍历每位也是可以的
            sum += digit
            product *= digit
            n //= 10
        return product-sum