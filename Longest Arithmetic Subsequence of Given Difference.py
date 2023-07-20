class Solution:
    def longestSubsequence(self, arr: list, difference: int) -> int:
        arr.sort()
        res = 0
        searched = set()
        searched.add(0)
        print(arr)
        def bfs(number,index):
            if number in searched:
                return 0
            searched.add(number)
            count = 1
            for i in range(index,len(arr)):
                if number == arr[i]-difference :
                    searched.add(arr[i])
                    count +=1
                    number = arr[i]
            return count
            
        for i in range(len(arr)):
            res = max(res,bfs(arr[i],i))
        return res


a = Solution()
print(a.longestSubsequence([3,4,-3,-2,-4],-5))


