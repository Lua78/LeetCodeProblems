class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        zeros = 1

        for r in range(len(nums)):
            zeros -= nums[r]==0

            if zeros<0:
                zeros += nums[l] == 0
                l+=1
        return r - l


print (longestSubarray([0,1,0,1,1,0,1,1,1,0,1,1,1]))