# create a hashMap = {}
# create keys and save the values with its corresponded keys into a sublist
# print the values of hashMap

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        
        for word in strs:
            key = tuple(sorted(word))
            myDict[key].append(word)

        res = []
        
        for val in myDict.values():
            res.append(val)
        return res

        