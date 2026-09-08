class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0

        freqMap = {}
        longest = 0

        for right in range(len(s)):
            if s[right] in freqMap:
                freqMap[s[right]] += 1
            else:
                freqMap[s[right]] = 1

            windowSize = (right - left) + 1
            replacementsNeeded = windowSize - max(freqMap.values())
            if replacementsNeeded <= k:
                longest = max(longest, windowSize)
            else:
                freqMap[s[left]] -= 1
                left += 1
        return longest

        