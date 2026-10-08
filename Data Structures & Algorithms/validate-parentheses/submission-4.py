class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {"{": "}",
                 "[": "]",
                 "(": ")"}
        stack = []

        for char in s:
            if char in pairs:
                stack.append(char)
            if char in ")}]":
                if stack:
                    popped = stack.pop()
                    if pairs[popped] != char:
                        return False
                else:
                    return False

        return len(stack) == 0
        
