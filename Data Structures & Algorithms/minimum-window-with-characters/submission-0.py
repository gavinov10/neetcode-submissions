class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        tFreq, window = {}, {}
        res = ""

        for char in t:
            if char not in tFreq:
                tFreq[char] = 1
            else:
                tFreq[char] += 1

        have, need = 0, len(tFreq)
        for right in range(len(s)):
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1

            if s[right] in tFreq and window[s[right]] == tFreq[s[right]]:
                have += 1

            while have == need:
                # update result
                if len(res) == 0 or (right - left + 1) < len(res):
                    res = s[left: right + 1]
                window[s[left]] -= 1
                if s[left] in tFreq and window[s[left]] < tFreq[s[left]]:
                    have -= 1
                left += 1

        return res

             