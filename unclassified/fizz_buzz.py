# TODO 由于这题逻辑比较简单，还有一个多线程版本的follow up，适合用来入门Leetcode多线程题
# TODO lintcode没有多线程题，leetcode上多线程题只有C、Java、Python三种语言，没有Rust/Go
# TODO 多线程题不用过多准备，牛客网上估计都不支持多线程
class Solution:
    def fizzBuzz(self, n):
        result = []
        for num in range(1, n + 1):
            if num % 3 == 0:
                if num % 5 == 0:
                    result.append("fizz buzz")
                else:
                    result.append("fizz")
            elif num % 5 == 0:
                result.append("buzz")
            else:
                result.append(str(num))
        return result
