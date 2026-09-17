class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = "".join(char for char in s if char.isalnum()).lower()
        l, r = 0, len(cleanS) - 1

        while l < r:
            if cleanS[l] != cleanS[r]:
                return False
            l += 1
            r -= 1
        
        return True
