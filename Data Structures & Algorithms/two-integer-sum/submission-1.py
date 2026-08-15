class Solution:
    


    def twoSum(self, nums: List[int], target: int) -> List[int]:

        def indexOf(s: List[int] , tgt: int) -> int:
            for i in range(len(s)):
                if tgt == s[i]:
                    return i
            return -1
        l = len(nums)
        for i in range(l):
            narr = nums[i+1:]
            tg = indexOf(narr,target-nums[i])
            if(tg!=-1):
                return [i,tg+i+1]
            
        return []