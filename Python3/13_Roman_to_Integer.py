s = "III"

s = "LVIII"

s = "MCMXCIV"

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        calculation = []
        negative_calculation = []
        for i in range(len(s)):
            if i == 0:
                calculation.append(values[s[i]])
            elif values[s[i-1]] < values[s[i]]:
                negative_calculation.append(2 * values[s[i-1]])
                calculation.append(values[s[i]])
            else:
                calculation.append(values[s[i]])

        return sum(calculation) - sum(negative_calculation)
    
print(Solution().romanToInt(s))