class Solution:
    def PredictTheWinner(self, nums:list):
        l,r = 0, len(nums)-1
        p1, p2 = 0,0
        turn  = True
        while(l<=r):
            if l<r-1:
                if nums[r-1]>nums[l+1]:
                    if nums[r]>=nums[r-1] and nums[r]>nums[l]:
                        points = nums[r]
                        r-=1
                    else:
                        points = nums[l]
                        l+=1
                else:
                    if nums[l]>=nums[l+1] and nums[l]>nums[r]:
                        points=nums[l]
                        l+=1
                    else:
                        points = nums[r]
                        r-=1
            else:
                if nums[l]>nums[r]:
                    points=nums[l]
                    l+=1
                else:
                    points = nums[r]
                    r-=1
            if turn:
                p1+=points
                print("p1 - ", points)
                turn = False
            else:
                print("p2 - ", points)
                turn = True
                p2+=points
        print(p1,p2)
        if p1>=p2:
            return True
        return False


a = Solution()

print(a.PredictTheWinner([1,6,7,5]))