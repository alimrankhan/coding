##def removeDuplicates(li:list):
##    le= len(li)
##    ans= [0]*le
##
##    return ans

li= [1,1,3]
li2= [1,1,1,2,3,3]
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l= len(nums)
        le= len(set(nums))
        for pos in range(l):
            for train in range(pos+1, l):
                
                if nums[pos] != nums [train]:
                    pos +=1
                    nums[pos]= nums[train];
        return le
obj= Solution()
print(obj.removeDuplicates(li2))
print(li2)
