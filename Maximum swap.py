class Solution:
    def maximumSwap(self, num: int):
        if len(str(num))==1:
            return num
        n = [ int(x) for x in str(num)]
        m = 0
        for i in range (len(n)):
            part = n[i:]
            curr = max(part)
            if n[i] < curr:
                index = 0
                j = len(part)-1
                while j>0:
                    if part[j]==curr:
                        index = j
                        break
                    j-=1
                aux = part[index]
                n[index+i] = n[i]
                n[i] = aux
                break 

        return int("".join(str(x) for x in n))


a = Solution()
print(a.maximumSwap(1995))
