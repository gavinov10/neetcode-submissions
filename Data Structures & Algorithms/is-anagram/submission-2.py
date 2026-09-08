class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input: s/t -> string
        # output: boolean if they are anagrams of eachother

        # we can first check to see if s and t are the length
        if len(s) != len(t):
            return False

        # we count the frequency of the letters in s and t
        # and return true if the freq in both strings are same
        countS, countT = defaultdict(int), defaultdict(int)

        # count the freq of s
        for letter in s:
            countS[letter] += 1
        
        # count the freq of s
        for letter in t:
            countT[letter] += 1
        
        return countS == countT




       