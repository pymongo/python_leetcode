from typing import List


# 看到shuffle我还以为要用随机数算法洗牌数组
# 没想到只是把[x1, x2, y1, y2]换成[x1, y1, x2, y2]
# 没有特别好的In-Place算法，In-Place算法至少要遍历2n次
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        p1, p2 = 0, n
        size = len(nums)
        while p2 < size:
            res.append(nums[p1])
            res.append(nums[p2])
            p1 += 1
            p2 += 1
        return res

    def better_solution(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n + i])
        return result


"""
impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        let n: usize = n as usize;
        let mut result: Vec<i32> = Vec::with_capacity(2 * n);
        for i in 0..n {
            result.push(nums[i]);
            result.push(nums[i+n]);
        }
        return result;
    }
}
"""
