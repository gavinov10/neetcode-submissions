class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if they aren't the same length --> not an anagram
        if len(s) != len(t):
            return False
        # count the frequency for each
        countS, countT = defaultdict(int), defaultdict(int)

        # freq for S
        for char in s:
            countS[char] += 1
            # if char in countS:
            #     countS[char] += 1
            # else:
            #     countS[char] = 1

        # freq for T
        for char in t:
            countT[char] += 1

        return True if countS == countT else False
        
       