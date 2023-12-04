import math

class Solution:
    def minSpeedOnTime(self, dist:list, hour: float):
        if len(dist)>math.ceil(hour):
            return -1
        def check(mid):
            res = 0
            i = 0
            for i in range(len(dist)-1):
                res += dist[i]//mid
                if dist[i]%mid:
                    res+=1
            if i+1<len(dist):
                i+=1
            res += dist[i]/mid
            if res<=hour:
                return  True
            else:
                return False
                
        l,r = 1,10000000
        while(l<r):
            mid=(r+l)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        return int(l)
    




a = Solution()
print(a.minSpeedOnTime([1,3,2],4))