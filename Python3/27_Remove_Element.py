from typing import List

nums = [3,2,2,3]
val = 3

nums = [0,1,2,2,3,0,4,2] 
val = 2

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i]==val:
                nums.remove(nums[i])
            else:
                i+=1
        return len(nums)
    
print(Solution().removeElement(nums, val))