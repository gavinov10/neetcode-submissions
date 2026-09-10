class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqDict = {}
        
        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1 # --> {num: freq}

        sortedVals = sorted(freqDict.items(), key=lambda item:item[1], reverse=True)
        
        return [num for num, freq in sortedVals[:k]]
        