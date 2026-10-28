#
# @lc app=leetcode id=3536 lang=python3
#
# [3536] Maximum Product of Two Digits
#

# @lc code=start

def intTostr(n):
    return [int(d) for d in str(n)]
class Solution:
    def maxProduct(self, n: int) -> int:
        n_list = intTostr(n)
        n_list.sort()
        return n_list[-1] * n_list[-2]
# @lc code=end

