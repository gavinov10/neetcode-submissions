class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if length of s and t != same, return False
        if len(s) != len(t):
            return False
        
        # create a dict for s and t to count letters
        countS, countT = {}, {}

        # # loop through s and append each letter to dict, if seen 
        # # add 1 to the value
        for letter in s:
            if letter in countS:
                # if letter in countS already, add +1 to the freq of letter
                countS[letter] += 1
            else:
                # if letter not in countS, assign letter value to 1
                countS[letter] = 1

        # # same process with string T
        for letter in t:
            if letter in countT:
                countT[letter] += 1
            else:
                countT[letter] = 1

        # # compare the values of each letter in countS and countT
        return countS == countT

        # second approach
        # return sorted(s) == sorted(t)