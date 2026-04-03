class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        freqMap = {}
        res = []

        for i in range(0, len(nums), 1):
            curr_num = nums[i]
            curr_keys = list(freqMap.keys())

            if curr_num in curr_keys:
                freqMap[curr_num] += 1
            else:
                freqMap[curr_num] = 1
        
        freq_list = list(freqMap.values())
        freq_list.sort(reverse=True)
        
        for j in range(0, k, 1):
            append_item = [k for k, v in freqMap.items() if v == freq_list[j]][0]
            freqMap.pop(append_item)
            res.append(append_item)
        return res