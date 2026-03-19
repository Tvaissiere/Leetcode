from typing import List

nums = [1,1,2]

nums = [0,0,1,1,1,2,2,3,3,4]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_lst = []
        for i in range(len(nums)):
            if nums[i] in new_lst:
                pass
            else:
                new_lst.append(nums[i])
        for i in range(len(new_lst)):
            nums[i] = new_lst[i]
        return len(new_lst)
    
print(Solution().removeDuplicates(nums))