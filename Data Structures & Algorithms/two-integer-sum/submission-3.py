class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # sorted_nums = nums.copy()
        # sorted_nums.sort()
        # for i in range(0, len(sorted_nums), 1):
        #     diff = sorted_nums[i] - target
        #     if diff in nums:
        #         j = nums.index(diff)

        for i in range(0, len(nums), 1):
            curr = nums[i]
            diff = target - curr
            cp_nums = nums.copy()
            cp_nums.remove(curr)
            if diff in cp_nums:
                j = cp_nums.index(diff) + 1
                break
        res = [i, j]
        res.sort()
        return res