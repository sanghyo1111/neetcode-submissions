class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [0]*len(nums)
        mult = 1
        flag = False
        ind = -1
        for i in range(len(nums)):
            
            if(nums[i]==0):
                if(flag):
                    return ret
                flag = True
                ind = i
            else:
                mult = mult*nums[i]

        
           
        
        
        if(flag):
            ret[ind] = mult
            return ret
            
        else:
            for i in range(len(nums)):
                ret[i] = int(mult/nums[i])

        return ret

