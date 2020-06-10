# 第二讲：最长回文子串

本讲是互动课，互动课指的是提前录制好的若干个短视频，中间穿插单选题和编程题组成的课程

## Subsequence子序列

子序列可以是非连续的字符

对于长度为n的字符串的子序列，每个字符都有选或不选两种可能。 

因此其子序列的数量是指数级别O(2^n)的

## Java和Python刷题要对入参作校验

这个是给面试官的加分项

对于非基本类型的入参，例如String

Java的第一行要写上 if s==null

Python则写上 if not isinstance(s, str)

## Python初始化二维布尔值数组

不能用 [[False]*3]*3 的方式定义一个3*3的数组

否则第二行和第三行都是第一行的shallow copy

有经验的做法是

dp = [[[False]*3] for _ in range(3)]