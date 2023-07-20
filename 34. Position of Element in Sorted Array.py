class Solution:
    def searchRange(self, nums:list, target: int):
        res = [-1,-1]
        l,r = 0,len(nums)-1
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid]==target:
                ma = mid
                while(ma+1<len(nums) and nums[ma+1]==target):
                    ma+=1
                mi = mid
                while mi-1>=0 and nums[mi-1]==target:
                    mi-=1
                res = [mi,ma]
            if nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return res
        
a = Solution()
print(a.searchRange([1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3],3))