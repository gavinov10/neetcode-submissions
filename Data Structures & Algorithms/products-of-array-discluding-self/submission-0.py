class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1 # -> 1 -> 2 -> 8 [1,2,4,6]
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]
            # [1, 1, 2, 8]
            #. 0  1  2  3

        postfix = 1 # -> 6 -> 24 -> 48
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
            

                    