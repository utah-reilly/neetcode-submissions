class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        
        
        # res = []
        # total = 1
        # nztotal = 1
        # for n in nums:
        #     total *= n
        #     if n != 0:
        #         nztotal *= n      
        # for n in nums:
        #     if n == 0:
        #         res.append(nztotal)
        #     else:
        #         res.append(total // n)
        
        # return res
 