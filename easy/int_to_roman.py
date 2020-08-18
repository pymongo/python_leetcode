int_to_roman = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}

roman_to_int = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}


class Solution:
    @staticmethod
    def integer_to_roman(num: int) -> str:
        res = ''
        # 贪心法: 根据罗马数字对应表，每次尽可能匹配更大的罗马字母
        # Python能保证有序地从大到小的遍历字典
        for integer in int_to_roman:
            if num >= integer:
                count = num // integer
                res += int_to_roman[integer] * count
                num %= integer
        return res

    @staticmethod
    def roman_to_integer(s: str) -> int:
        res = 0
        for roman in roman_to_int:
            while s.startswith(roman):
                res += roman_to_int[roman]
                s = s[len(roman):]
        return res
