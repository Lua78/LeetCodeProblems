class Solution:
    def intToRoman(self, num: int):
        res = ""
        while(num>0):
            print (res,num)
            if num>=1000:
                res = res+"M"
                num = num-1000
            elif num>=900:
                res = res+"CM"
                num -=900
            elif num>=500:
                res = res+"D"
                num = num-500
            elif num>=400:
                res = res+"CD"
                num=num-400
            elif num>=100:
                res = res+"C"
                num=num-100
            elif num>=90:
                res = res+"XC"
                num=num-90
            elif num>=50:
                res = res+"L"
                num = num-50
            elif num>=40:
                res = res+"XL"
                num-=40
            elif num>=10:
                res = res+"X"
                num=num-10
            elif num>=9:
                res = res+"IX"
                num=num-9
            elif num>=5:
                res = res+"V"
                num=num-5
            elif num>=4:
                res = res+"IV"
                num=num-4
            elif num>=1:
                res = res+"I"*num
                num = 0
        return res

a = Solution()
print(a.intToRoman(444))