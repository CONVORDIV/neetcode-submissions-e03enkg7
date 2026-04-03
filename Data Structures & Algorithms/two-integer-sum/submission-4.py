class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0, len(nums), 1):
        #     curr = nums[i]
        #     diff = target - curr
        #     cp_nums = nums.copy()
        #     cp_nums.remove(curr)
        #     if diff in cp_nums:
        #         j = cp_nums.index(diff) + 1
        #         break
        # res = [i, j]
        # res.sort()
        # return res

        prevMap = {}

        for i, v in enumerate(nums):
            diff = target - v
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[v] = i
        

