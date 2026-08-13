class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # O(N^2)
        # for i in nums:
        #     cnt = 0
        #     for j in nums:
        #         if(j==i):
        #             cnt = cnt+1
        #         if(cnt == 2):
        #             return True
        # return False

        log = []
        for i in nums:
            if(i in log):
                return True
            log.append(i)
        return False
