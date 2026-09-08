class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array, loop through nums once, assign l, r pointers
        res = []
        nums.sort() # -> [-4, -1, -1, 0, 1, 2]
                              #F.     l  r

        for i, num in enumerate(nums):
            if num > 0:
                break
                
            if i > 0 and num == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                if num + nums[l] + nums[r] > 0:
                    r -= 1
                elif num + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res
