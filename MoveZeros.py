def moveZeros(li):
    l,r = 0, len(li)-1
    while l<r:
        if li[r]!=0:
            li[l] , li[r] = li[r], li[l]
            l+=1
        else:
            r-=1
    return li

li =  [0,1,0,12,3,11,1]
li.sort()
print(moveZeros(li))