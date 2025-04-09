class Solution:
    def isValid(self, string: str) -> bool:
        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []

        for i in string:
            if i in bracket_map:
                if stack and stack[-1] == bracket_map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False  

