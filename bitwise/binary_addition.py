# https://leetcode.com/problems/sum-of-two-integers/
# https://leetcode-cn.com/problems/sum-of-two-integers/solution/wei-yun-suan-xiang-jie-yi-ji-zai-python-zhong-xu-y/
def addition(a: int, b: int) -> int:
    """
    可以将加法拆分为两部分:
    1. 无进位加法-异或: a ^ b
    2. a & b << 1 获取进位
    """
    # 2^32
    MASK = 0x100000000
    # 整型最大值
    MAX_INT = 0x7FFFFFFF
    MIN_INT = MAX_INT + 1
    while b != 0:
        # 计算进位
        carry = (a & b) << 1
        # 取余范围限制在 [0, 2^32-1] 范围内
        a = (a ^ b) % MASK
        b = carry % MASK
    return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
