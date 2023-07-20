class Solution:
    def putMarbles(self, weights:list, k: int):
        if k==1:
            return 0
        sums = []
        for i in range(len(weights)-1):
            sums.append(weights[i] + weights[i+1])
        sums.sort()
        value = sum(sums[-k+1:]) - sum(sums[:k-1])
        return value

a = Solution()
print(a.putMarbles([1,3,5,1],2))