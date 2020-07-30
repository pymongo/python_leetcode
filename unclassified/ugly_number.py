import unittest


def my_is_ugly_number(num: int) -> bool:
    if num == 0:
        return False
    for factor in (2, 3, 5):
        while num % factor == 0:
            num //= factor
    return num == 1
    # if num == 0:
    #     return False
    # while num % 2 == 0:
    #     num //= 2
    # while num % 3 == 0:
    #     num //= 3
    # while num % 5 == 0:
    #     num //= 5
    # return num == 1


class Testing(unittest.TestCase):
    TEST_CASES = [
        (14, False), (6, True), (8, True)
    ]

    def test_my_is_ugly_number(self):
        for num, is_ugly in self.TEST_CASES:
            print(num, is_ugly)
            self.assertEqual(is_ugly, my_is_ugly_number(num))
