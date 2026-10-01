class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
# hashset에서는 in 확인이 O(1)임
        if(len(nums) == 0 ):
            return 0
        if(len(nums) == 1 ):
            return 1
        
        hashSet =  set(nums)
        
        MaxStreak = 1
        for i in hashSet:
            
            if(i-1 not in hashSet):
                cur = i
                streak = 1
                while(cur+1 in hashSet):
                    cur = cur+1
                    streak = streak+1
                
                if(MaxStreak < streak):
                    MaxStreak = streak
                
        return MaxStreak
            
           



