class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        hashmap = {}
        longestSubstring = 0

        while r < len(s):
            if s[r] in hashmap:
                l = max(l, hashmap[s[r]] + 1)
            hashmap[s[r]] = r
            longestSubstring = max(longestSubstring, r - l + 1)
            r += 1

        return longestSubstring