class Solution:
    def subsets(self, nums:list):
        res = []
        curr = []
        def dfs(index):
            if index>=len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[index])
            dfs(index+1)
            curr.pop()
            dfs(index+1)
        dfs(0)
        return res

a=Solution()
print(a.subsets([1,2,3]))