from bisect import bisect,bisect
class Solution:
    def maxValue(self, events: list, k: int):
        events.sort(key=lambda ans:ans[1])
        dp=[[0,0]]
        dp2=[[0,0]]
        for x in range(k):
            for s,e,v in events:
                i=bisect.bisect(dp,[s])-1
                if dp[i][1]+v>dp2[-1][1]:
                    dp2.append([e,dp[i][1]+v])

            dp=dp2
            dp2=[[0,0]]

        return dp[-1][-1]  


a = Solution()
print(a.maxValue([[1,3,4],[2,4,1],[1,1,4],[3,5,1],[2,5,5]],3))