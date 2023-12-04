class Solution:
    def peakIndexInMountainArray(self, arr:list):
        l,r = 0,len(arr)
        while(l<r):
            target = l+(r-l)//2
            if arr[target]>arr[target-1] and  arr[target] > arr[target+1]:
                return  target
            if  arr[target]<=arr[target-1]:
                r = target
            else:
                l = target
            


        pass


a = Solution()
print(a.peakIndexInMountainArray([0,10,11,12,5,2]))