# dis函数查看某函数的底层指令执行过程
from dis import dis
import timeit
# from inspect import getsource
# 自带的更安全的eval(ast.literal_eval)
# import ast


def swap1(a: int, b: int) -> (int, int):
    temp = a
    a = b
    b = temp
    return a, b


def swap2(a: int, b: int) -> (int, int):
    a, b = b, a
    return a, b


def swap_xor(a: int, b: int) -> (int, int):
    a = a ^ b
    b = a ^ b
    a = a ^ a
    return a, b


if __name__ == '__main__':
    dis(swap1)  # 使用临时变量交换变量指令反而更长了
    print('========\n' * 3)
    dis(swap2)

    swap1_timer = timeit.Timer("swap1(1,2)", "from __main__ import swap1")
    print(swap1_timer.timeit(number=10 ** 6))
    swap2_timer = timeit.Timer("swap2(1,2)", "from __main__ import swap2")
    print(swap2_timer.timeit(number=10 ** 6))
    swap_xor_timer = timeit.Timer("swap_xor(1,2)", "from __main__ import swap_xor")
    print(swap_xor_timer.timeit(number=10 ** 6))  # 牺牲空间复杂度的xor_swap，结果慢一倍多
