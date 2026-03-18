from typing import List

nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            answer = target - nums[i]
            if answer in nums:
                for x in range(len(nums)):
                    if answer == nums[x]:
                        if i == x:
                            pass
                        else:
                            return [i, x]

print(Solution().twoSum(nums,target))