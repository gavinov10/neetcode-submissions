class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        setS = set()
        longest = 0
        

        for right in range(len(s)):
            while s[right] in setS:
                setS.remove(s[left])
                left += 1

            setS.add(s[right])
            currLength = (right - left) + 1
            longest = max(currLength, longest)
        
        return longest