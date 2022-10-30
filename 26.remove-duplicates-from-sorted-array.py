#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
# @lc code=end
# @lc code=end
# @lc code=end
#  nums = [1,1,2]Output: 2, nums = [1,2,_]
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums= list(set(nums)) 
        return len(nums)

# @lc code=end

