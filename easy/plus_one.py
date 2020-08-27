from typing import List


class Solution:
    @staticmethod
    def plus_one(digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                continue
            digits[i] += 1
            return digits
        # [9] -> [1,0]
        digits.insert(0, 1)
        return digits
