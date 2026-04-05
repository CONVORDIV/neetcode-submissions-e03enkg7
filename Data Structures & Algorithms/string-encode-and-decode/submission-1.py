import json
class Solution:

    def encode(self, strs: List[str]) -> str:
        
        
        # res = '['
        # for item in strs:
        #     if len(res) == 1:
        #         res += "\"" + item + "\""
        #     else:
        #         res += ",\"" + item + "\""
        return json.dumps(strs)

    def decode(self, s: str) -> List[str]:
        return json.loads(s)
        
        # else:
        #     items_str = s[1:-1].split("\'")
        #     res = [x for x in items_str if x not in ["", ", "]]
        #     return res
        