from typing import List


class Solution:
    @staticmethod
    def is_straight(nums: List[int]) -> bool:
        # 可以将大小王(0)理解成百变卡，可以变成任意数字
        min_card, max_card = 14, 0
        seen = set()
        for num in nums:
            if num == 0:
                # 暂时忽略百变卡-大小王
                continue
            if num in seen:
                # 顺子中不能有重复的
                return False
            min_card = min(min_card, num)
            max_card = max(max_card, num)
            seen.add(num)
        # 这里要考虑百变卡，所以只要最大的牌-最小的牌<5，如果有空位百变卡就能填充空位，如果没有百变卡那就是顺子了
        return max_card - min_card < 5
