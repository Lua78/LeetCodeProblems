
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int):
        if n%2==0:
            return []
        dp = {0:[], 1:[TreeNode()]}

        def makeTree(n):
            if n in dp:
                return dp[n]
            res = []
            for l in range(n):
                r = n-l-1
                leftT, RighT = makeTree(l),makeTree(r)
                for t1 in leftT:
                    for t2 in RighT:
                        res.append(TreeNode(0,t1,t2))
            dp[n]=res
            return res
        return makeTree(n)

a = Solution()
print(a.allPossibleFBT(7))


        