# 明明是循环移位，感觉英文叫rotate不太合适
from typing import List


def reverse(s: List[str], start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


# lintcode上的rotate_string确实是字符串反转三次这种题
def rotate_string(s: str, size: int, offset: int) -> str:
    # 向左循环移位的偷懒写法: s[n:] + s[:n]
    chars = list(s)
    # 如果是lintcode上的这题，要加 offset %= size
    reverse(chars, 0, size - 1)
    reverse(chars, 0, offset - 1)
    reverse(chars, offset, size - 1)
    return "".join(chars)


# 我的穷举法弱爆了...
def leetcode_rotate_string(a: str, b: str) -> bool:
    size = len(a)
    if size == 0:
        return a == b
    for offset in range(size - 1):
        if b == rotate_string(a, size, offset):
            return True
    # 旋转排序数组、循环数组的一个通用技巧是原数组翻倍，也就是后面再接上一个原数组
    # for s in range(len(A)):
    #     if all(A[(s + i) % len(A)] == B[i] for i in range(len(A))):
    #         return True
    return False

# 就当做复习一遍rolling hash算法
# 由于a的循环移位的结果必在a+a字符串内，本题可以抽象成判断b是否在a+a字符串内，可以使用rolling_hash或kmp算法把O(N^2)的搜索过程优化成O(N)
def rolling_hash(a: str, b: str) -> bool:
    len_a = len(a)
    len_b = len(b)
    if len_b == 0:
        return len_a == len_b
    if len_b != len_a:
        return False
    source = a + a
    source_len = 2 * len_a
    target = b
    target_len = len_b

    BASE = 26  # 幂的基数取31或26都行
    MOD = 10 ** 5
    CHAR_OFFSET = ord('a')

    source_hash = 0
    target_hash = 0
    for i in range(target_len):
        # rolling_hash背诵点1: hash更新的公式
        source_hash = (source_hash * BASE + ord(source[i]) - CHAR_OFFSET) % MOD
        target_hash = (target_hash * BASE + ord(target[i]) - CHAR_OFFSET) % MOD
    if source_hash == target_hash:
        return True
    for i in range(source_len - target_len):
        # rolling_hash背诵点2: source_hash先往右扩展一位，然后再剔除掉第一个字母所占的Hash的代码模板
        source_hash = (source_hash * BASE + ord(source[i + target_len]) - CHAR_OFFSET) % MOD
        source_hash = source_hash - ((ord(source[i]) - CHAR_OFFSET) * (BASE ** target_len) % MOD)
        if source_hash < 0:
            source_hash += MOD
        if source_hash == target_hash:
            # TODO double check substr
            return True
    return False
