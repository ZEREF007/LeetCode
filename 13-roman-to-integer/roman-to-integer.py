class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {'I':1, 'V':5,'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        total,prev = 0,0
        for char in reversed(s): # OR s[::-1] 
            current= hash_map[char]
            total += current if current >= prev else -current
            prev = current
        return total