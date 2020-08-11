import unittest


def match(p: str, s: str) -> bool:
    p_len = len(p)
    if p_len == 0:
        return False
    if p_len == 1:
        return True
    s_len = len(s)
    p_to_word = dict()
    used_words = set()

    def dfs(pi: int, si: int) -> bool:
        # 这里不能处理pattern刚好长度为1的情况
        if pi >= p_len:
            # 判断最后一个匹配字符是否等于s最后一个单词
            return si >= s_len

        pat = p[pi]
        if pat in p_to_word:
            word = p_to_word[pat]
            word_len = len(word)
            # for i in range(word_len):
            #     if si + i >= s_len:
            #         return False
            #     if s[si+i] != word[i]:
            #         return False
            if not s[si:].startswith(word):
                return False
            return dfs(pi + 1, si + word_len)

        # 当前pattern还未存入字典中，从小到大搜索哪个单词匹配pattern更合适
        for i in range(si + 1, s_len+1):
            word = s[si:i]
            if word in used_words:
                continue

            used_words.add(word)
            p_to_word[pat] = word

            # 注意单词是截取到i-1，所以这里si的下标是i
            if dfs(pi+1, i):
                return True

            used_words.remove(word)
            p_to_word.pop(pat)
        return False

    return dfs(0, 0)


# 这个题不能使用动态规划或者记忆化搜索，因为参数列表中 mapping 和 used 无法记录到记忆化的哈希表中
class Testing(unittest.TestCase):
    TEST_CASE = [
        ("wqojxmdc", "zgodhogujnsluwgnadxlgw", True),
        ("aaaa", "dogdogdogdog", True),
        ("d", "ef", True),
        ("abab", "catdogcatdog", True),
        ("aabb", "xyzabcxzyabc", False),
    ]

    def test_match(self):
        for p, s, is_match in self.TEST_CASE:
            print(p, s)
            self.assertEqual(is_match, match(p, s))
