class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longestSubstring = 0
        mostFrequent = defaultdict(int)

        for right in range(len(s)):
            mostFrequent[s[right]] = mostFrequent.get(s[right], 0) + 1
            currWindow = (right - left) + 1
            replacements = currWindow - max(mostFrequent.values())
            while replacements > k:
                mostFrequent[s[left]] -= 1
                left += 1
                currWindow = (right - left) + 1
                replacements = currWindow - max(mostFrequent.values())
            
            longestSubstring = max(currWindow, longestSubstring)

        return longestSubstring