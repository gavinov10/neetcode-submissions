class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        curr = 1

        for i in range(len(nums)):
            output[i] = curr
            curr *= nums[i]
        
        curr = 1
        for i in range(len(nums) -1, -1, -1): # output --> [1, 1, 2, 8]
            output[i] *= curr
            curr *= nums[i]
        
        return output 

            
        

