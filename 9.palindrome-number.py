#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
def int_to_list(n):
    return [int(d) for d in str(n)]
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_list = int_to_list(x)
        if x_list == x_list[::-1]:
            return True
        return False
# @lc code=end

obj= Solution()
print(obj.isPalindrome(2))