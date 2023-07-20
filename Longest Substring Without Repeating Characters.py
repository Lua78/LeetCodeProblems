class Solution:
    def lengthOfLongestSubstring(self,s):
        if len(s)<=1:
            return len(s)
        buff = set()
        res = 0
        for i in range(len(s)):
            buff.add(s[i])
            k = i+1
            while(k<len(s) and s[k] not in buff):
                buff.add(s[k])
                k+=1
            res = max(res, len(buff))
            print(buff)
            buff.clear()
        return res
    
a = Solution()
print(a.lengthOfLongestSubstring("aux"))