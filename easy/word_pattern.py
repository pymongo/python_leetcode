import unittest


class Solution(unittest.TestCase):
    TESTCASES = [
        ("abba", "dog cat cat fish", False),
        ("abba", "dog cat cat dog", True),
        ("abba", "dog dog dog dog", False),
    ]

    @staticmethod
    def is_match(p: str, s: str) -> bool:
        words = s.split()
        if len(p) != len(words):
            return False
        hashmap = dict()
        used_words = set()
        for pat, word in zip(p, words):
            # print(pat, word)
            if pat not in hashmap:
                if word in used_words:
                    # ("abba", "dog dog dog dog", False)
                    return False
                hashmap[pat] = word
                used_words.add(word)
            elif word != hashmap[pat]:
                return False
        return True

    def test_is_match(self):
        for s, p, is_match in self.TESTCASES:
            print(s, p)
            self.assertEqual(is_match, self.is_match(s, p))
