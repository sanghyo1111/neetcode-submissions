class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for i in nums:
            dic[i] = dic[i]+1
        
        ret = []
        l=0
        la=0
        v = 0
        index = -1
        while(l != k):
            for x, y in dic.items():
                if(y > la):
                    la = y
                    v = x
            la=0
            ret.append(v)
            dic.pop(v)
            l = l+1

        
        return ret