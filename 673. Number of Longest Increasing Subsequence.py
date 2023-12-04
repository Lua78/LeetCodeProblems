class Solution:
    def findNumberOfLIS(self, nums:list):
        dp = {len(nums)-1:1}
        pointer = {}
        indexs = {}
        def dfs(index):
            if index in dp:
                return  dp[index]
            res = dfs(index+1)
            curSub = 0
            for i in range(index+1,len(nums)):
                if nums[index]<nums[i]:
                    curSub = max(curSub,dp[i])
            dp[index] = curSub+1
            res =  max(res,curSub+1)
            pointer[res]=index
            indexs[res]=index

            return res
        res = dfs(0)
        curr=res
        ind = indexs[res]
        subseq=0
        while(curr):
            count = 0
            multiply = 1
            for i in range(ind+1,len(nums)):
                if dp[i]==curr+1:
                    multiply+=1
                if dp[i]==curr:
                    count +=1*multiply

            curr-=1
            subseq = max(subseq,count)

        print(dp)
        print(res)
        if subseq>1:
            return subseq
        return res

a = Solution()
print(a.findNumberOfLIS([1,4,3,2,5]))
#Not solved yet