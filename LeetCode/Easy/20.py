# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for c in s:
            if c not in table:
                stack.append(c)
            elif not stack or table[c] != stack.pop():
                return False

        return len(stack) == 0

        
if __name__ == '__main__':
    test_case = "()[]{}"
    print(Solution().isValid(test_case))