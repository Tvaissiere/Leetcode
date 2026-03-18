from typing import List

strs = ["flower","flow","flight"]

strs = ["dog","racecar","car"]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lst = []
        for i in range(len(strs)):
            if strs[i]=="":
                return ""
            for x in range(len(strs[i])):
                if i == 0:
                    for j in range(1, len(strs)):
                        if x >= len(strs[j]) or strs[j][x] != strs[i][x]:
                            return "".join(lst)
                    lst.append(strs[i][x])
        return "".join(lst)
    
print(Solution().longestCommonPrefix(strs))