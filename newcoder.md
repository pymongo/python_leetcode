# 牛客网刷题的注意事项

考虑Python3在lintcode、牛客网、leetcode都支持，代码精简而且编写单元测试也相对比Java容易，支持typehint(这也是不选ruby的原因)

所以为了应对bytedance在牛客网上远程编程题考试，而且九章算法网课主讲python，所以要先把python用熟练

## typing问题

牛客网(截止20年6月)的python3版本是3.5，刚开始支持typehint，但在函数入参和返回值中支持

[variable annotations](https://docs.python.org/3/whatsnew/3.6.html)

```
PEP 526: Syntax for variable annotations
PEP 484 introduced the standard for type annotations of function parameters, a.k.a. type hints. This PEP adds syntax to Python for annotating the types of variables including class variables and instance variables:

primes: List[int] = []

captain: str  # Note: no initial value!

class Starship:
    stats: Dict[str, int] = {}
```

牛客网上写代码要注意！typehint/variable annotations只能用于函数的入参和返回值