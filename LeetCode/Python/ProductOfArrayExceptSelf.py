class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for x in range(len(nums)):
            res[x] = prefix
            prefix *= nums[x]
        print(res)

        postfix = 1
        for x in range(len(nums) - 1, -1, -1):
            res[x] *= postfix 
            postfix *= nums[x]
        print(res)

        return res
        # First Attempt, TIme Limit Exceeded
        # res = []
        # for num in range(len(nums)):
        #     clone = list(nums)
        #     del clone[num]
        #     res.append(reduce(lambda x, y: x * y, clone))
        # return res
