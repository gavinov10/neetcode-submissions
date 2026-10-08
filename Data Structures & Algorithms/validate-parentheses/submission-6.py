class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        pairs = {"{": "}",
                 "[": "]",
                 "(": ")"}

        for c in s:
            if c in pairs:
                stack.append(c)
            elif c in "}])" and stack:
                popped = stack.pop()
                if pairs[popped] != c:
                    return False
            else:
                return False

        return len(stack) == 0
                    