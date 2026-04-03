class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        strMap = {}
        
        for i in range(0, len(strs), 1):
            curr_key = str(sorted(list(strs[i])))
            if curr_key not in list(strMap.keys()):
                strMap[curr_key] = [i]
            else:
                strMap[curr_key].append(i)
        
        mapValues = list(strMap.values())
        for v in mapValues:
            each = []
            for w in v:
                each.append(strs[w])
            res.append(each)
        return res


        # for i in range(0, len(strs), 1):
        #     key_list = strMap.keys()
        #     curr_str = strs[i]
        #     print(f"curr_str: {curr_str}")
        #     print(f"strMap: {strMap}")
        #     if sorted(list(curr_str)) in key_list:
        #         res.append([strs[key_list[curr_str]], i])
        #         strMap.pop(curr_str)
        #     else:
        #         strMap[sorted(list(curr_str))] = i
        #     print(f"res: {res}")
        # return res

