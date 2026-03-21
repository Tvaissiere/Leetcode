from typing import List

digits = [1,2,3]

digits = [4,3,2,1]

digits = [9]    

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = str(int(("".join(map(str, digits)))) + 1)
        digits = []
        for i in range(len(ans)):
            digits.append(int(ans[i]))
        return digits

print(Solution().plusOne(digits))
