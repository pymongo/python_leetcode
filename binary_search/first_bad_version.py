"""
本题有点像扔鸡蛋、故障检测的题目
这题写单元测试太麻烦了，思路也很简单，我直接在网页上写就AC掉了
"""

# 击败了99.79%
# class Solution:
#     def firstBadVersion(self, n):
#         start, end = 0, n
#         while start < end:
#             mid = start + (end - start) // 2
#             if isBadVersion(mid):
#                 end = mid
#             else:
#                 start = mid + 1
#         return start

