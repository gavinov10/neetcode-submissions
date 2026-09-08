class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        U -
            I - [nums], int(k)
            O - k elements --> top k elements of freq
            C - 
            E - empty list, tie contraints [1, 1, 2, 2, 3, 3] k(2)
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

        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        
        my_tuple = tuple(my_dict.items())
        sorted_tuple = sorted(my_tuple, key=lambda x: -x[1])

        res_k = []

        for num, value in sorted_tuple:
            res_k.append(num)
        
        return res_k[:k]
