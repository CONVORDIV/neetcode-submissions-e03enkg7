class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            
            sMap, tMap = {}, {}
            
            for i in range(0, len(s), 1):
                sMap[s[i]] = sMap.get(s[i], 0) + 1
                tMap[t[i]] = tMap.get(t[i], 0) + 1
            
            if sMap == tMap:
                return True
            else:
                return False
    
    
    
    
    
    
    
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     else:
    #         s_dict = self.toDict(s)
    #         t_dict = self.toDict(t)
    #         if s_dict == t_dict:
    #             return True
    #         else:
    #             return False

    # def toDict(self, s: str) -> bool:
    #     res = {}
    #     for i in range(0, len(s), 1):
    #         if s[i] in list(res.keys()):
    #             res[s[i]] += 1
    #         else:
    #             res[s[i]] = 1
    #     return res


            