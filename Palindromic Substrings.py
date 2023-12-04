class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        le = len(s)
        for i in range(le):
            l=r=i
            while(r<le and l>=0 and s[l]==s[r]):
                res+=1 
                r+=1
                l-=1
            l,r=i,i+1
            while(r<le and l>=0 and s[l]==s[r]):
                res+=1 
                r+=1
                l-=1
        return res

a = Solution()
print(a.countSubstrings("aaaaa"))