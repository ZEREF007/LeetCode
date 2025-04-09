class Solution:

    def romanToInt(self, inp: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        for i in range(len(inp)):
            if i + 1 < len(inp) and roman[inp[i]] < roman[inp[i + 1]]:
                result -= roman[inp[i]]
            else:
                result += roman[inp[i]]
                
        return result