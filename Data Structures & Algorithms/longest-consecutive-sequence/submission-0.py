class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        max_len = 0

        for n in nums:
            if n-1 not in my_set:
                curr = n
                length = 1

                while curr+1 in my_set:
                    curr += 1
                    length += 1
                
                max_len = max(max_len, length)
        return max_len



 





