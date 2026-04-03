class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = {}
        result = False
        for i in nums:
            if i in list(check.keys()):
                check[i] += 1
            else:
                check[i] = 1
        if sum(check.values()) != len(check.keys()):
            result = True
        return result
