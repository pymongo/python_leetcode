import unittest
from typing import List, Tuple

class Testing(unittest.TestCase):
    TEST_CASES: List[Tuple[str, str]] = [
        ("babad", "bab"),
        ("abadd", "aba"),
        ("cbbd", "bb"),
        ("aba", "aba"),
        ("ac", "a"),
        ("ccc", "ccc"),
    ]
    def test(self):
        pass




