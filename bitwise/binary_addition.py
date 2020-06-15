"""
// 主要利用异或运算来完成
// 异或运算有一个别名叫做：不进位加法
// 那么a ^ b就是a和b相加之后，该进位的地方不进位的结果
// 然后下面考虑哪些地方要进位，自然是a和b里都是1的地方
// a & b就是a和b里都是1的那些位置，a & b << 1 就是进位
// 之后的结果。所以：a + b = (a ^ b) + (a & b << 1)
// 令a' = a ^ b, b' = (a & b) << 1
// 可以知道，这个过程是在模拟加法的运算过程，进位不可能
// 一直持续，所以b最终会变为0。因此重复做上述操作就可以
// 求得a + b的值。
while (b != 0) {
    int _a = a ^ b;
    int _b = (a & b) << 1;
    a = _a;
    b = _b;
}
return a;
"""
import unittest


class Test(unittest.TestCase):
    TEST_CASES = [(-100, 100, 0)]

    def test(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(addition(case[0], case[1]), case[2])


def addition(a: int, b: int) -> int:
    # FIXME a或b是负数时，二进制运算会选入死循环，Java中int都是signed的可能就没有这个问题
    if a < 0 or b < 0:
        return a + b
    while b != 0:
        # 异或运算: 不进位加法
        _a: int = a ^ b
        # 获取刚刚运算中的进位
        _b: int = (a & b) << 1
        a, b = _a, _b
    return a
