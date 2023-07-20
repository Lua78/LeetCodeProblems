class Solution:
    def myAtoi(self, s:str):
        neg = None
        ans = []
        i = 0
        while(i< len(s) and (s[i].isdigit() or s[i]=='-' or s[i]=='+' or s[i]==' ')):
            if s[i]=='-':
                if neg == False:
                    return 0
                neg = True
            elif s[i]=='+':
                if neg == True or (neg==' ' and not s[i+1].isdigit()):
                    return 0
                neg = False
            elif s[i]==' ':
                if neg == True or neg ==False:
                    return 0
                neg = ' '
            if(s[i].isdigit()):
                k=i
                while(k<len(s) and s[k].isdigit()):
                    ans.append(str(s[k]))
                    k+=1
                ans = ''.join(ans)
                ans = int(ans)
                if neg==True:
                    ans = ans*-1
                if ans<-2147483648:
                    return -2147483648
                elif ans>2147483647:
                    return 2147483647
                else:
                    return ans
            i+=1
        return 0

a = Solution()
print(a.myAtoi(" +999999999999"))