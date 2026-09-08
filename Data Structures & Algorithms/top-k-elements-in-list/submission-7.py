class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        P - create a dict frequency --> {1:1,
                                         2:2,
                                         3:3}
            convert freq_dict --> my_tuple(freq_dict)
            res_k = []

            sorted_tuple = sorted(my_tuple, key=lambda x: x[1])
            for num, value in sorted_tuple:
                res_k.append(num)
            
            return res_k[:k]
        I -
        """
        freqDict = defaultdict(int)
        for num in nums:
            freqDict[num] += 1

        sortedDict = sorted(freqDict.items(), key=lambda x: x[1], reverse=True)
        return [key for key, _ in sortedDict[:k]]