class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list):
        res = []
        l1, l2 = len(nums1),len(nums2)
        m1,m2 = 0,0
        while(m1<l1 or m2<l2):
            #print(m1,m2)
            if m1<l1 and m2<l2:
                if nums1[m1]<=nums2[m2]:
                    res.append(nums1[m1])
                    m1+=1
                elif nums2[m2]<=nums1[m1]:
                    res.append(nums2[m2])
                    m2+=1
            elif m1<l1:
                for i in range(l1-m1):
                    res.append(nums1[m1+i])
                break
            elif m2<l2:
                for i in range(l2-m2):
                    res.append(nums2[m2+i])
                break
            else:
                break
        if (l1+l2)%2==0:
            return (res[((l1+l2)//2)-1]+res[(l1+l2)//2])/2
        return (res[((l1+l2)//2)])

a = Solution()
print(a.findMedianSortedArrays([1,3,6],[2,3,7]))
