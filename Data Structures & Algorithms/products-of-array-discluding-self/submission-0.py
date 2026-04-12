class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        preP, postP = [1], [1]

        for i in range(0, len(nums), 1):
            preP.append(preP[i] * nums[i])
        
        for j in range(len(nums)-1, -1, -1):
            postP.insert(0, nums[j]*postP[0])
        
        # preP.pop(0)
        # postP.pop(-1)
        # print(pre)

        for k in range(0, len(nums), 1):
            res.append(int(preP[k]*postP[k+1]))
        return res
        


        # total_product = 1
        # for num in nums:
        #     total_product *= num
        
        # res = []
        # for num in nums:
        #     if num == 0:
        #         res.append(int())
        #     else:
        #         res.append(int(total_product / num))
        # return res

