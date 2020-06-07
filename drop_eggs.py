import sys
import math
from typing import List

stdin_input: List[str] = sys.stdin.readlines()
print(stdin_input)
times, input_height = stdin_input[0].split(' ')
times = int(times)
input_height = int(input_height.replace('\n', ''))
# assert type(times) == 'int'
assert isinstance(times, int)
assert isinstance(input_height, int)


class Solution:
    @staticmethod
    def try_times(height: int) -> int:
        return math.ceil((-1 + math.sqrt(1 + 8 * height)) / 2)


if __name__ == '__main__':
    print(min(times, Solution.try_times(input_height)))
