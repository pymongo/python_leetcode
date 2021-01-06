# https://lintcode.com/problem/digit-counts/description
# noinspection PyPep8Naming
def digitCounts(k: int, n: int) -> int:
    """
    计算数字 k 在 0 到 n 中的出现的次数，k 可能是 0~9 的一个值

    k = 1, n = 12
    输出：5
    解释：在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 中，我们发现 1 出现了 5 次 (1, 10, 11, 12)(注意11中有两个1)。

    例如想批量地数10*k..10*(k+1)，难以找到迭代代码，难以解决边界或特殊的k=0
    最终还是直接把0..n+1拼成字符串，再去数更好
    """
    return str(list(range(n + 1))).count(str(k))
