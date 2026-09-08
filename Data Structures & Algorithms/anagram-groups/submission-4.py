# create a hashMap = {}
# create keys and save the values with its corresponded keys into a sublist
# print the values of hashMap

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a defaultdict to store a key
        # that represents each words diagram
        res = defaultdict(list)

        # loop through and add each key + word to dict
        for word in strs:
            sortedWord = ''.join(sorted(word))
            res[sortedWord].append(word)
        return list(res.values())