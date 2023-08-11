# STILL IN PROGESS
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for x in range(len(nums)):
            res[x] = prefix * nums[x]
            prefix = res[x]
        print(res)

        postfix = 1
        for x in range(len(nums) - 1, -1, -1):
            res[x] *= postfix 
            postfix *= nums[x]
        print(res)

        
        # First Attempt, TIme Limit Exceeded
        # res = []
        # for num in range(len(nums)):
        #     clone = list(nums)
        #     del clone[num]
        #     res.append(reduce(lambda x, y: x * y, clone))
        # return res
