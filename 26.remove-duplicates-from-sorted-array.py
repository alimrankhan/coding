#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k= len(set(nums))
        le= len(nums)
        idx= 0
        curr= nums[0]
        for pos in range(0,le):
            if nums[pos]==curr:
                continue
            idx= idx+1
            nums[idx]= nums[pos]
            curr= nums[pos]


        return k
        
# @lc code=end
li= [1,2,2,2,3,3,4,5,5]
print(Solution().removeDuplicates(li), li)  # Output: 5