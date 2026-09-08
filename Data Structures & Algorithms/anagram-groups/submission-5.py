class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        res = []

        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in anagrams:
                anagrams[sortedWord] = [word]
            else:
                anagrams[sortedWord].append(word)

        for key, val in anagrams.items():
            res.append(val)
    
        return res

        # strs = ["act","pots","tops","cat","stop","hat"]