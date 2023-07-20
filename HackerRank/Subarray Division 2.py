
def birthday(s, d, m):
    if m==1:
        if d in s:
            return 1
        else:
            return 0
    res = 0

    for i in range(len(s)-m+1):
        sum = 0
        for j in range(i,m+i):
            sum += s[j]
        if sum==d: res+=1

    return res

print(birthday([4, 5, 4, 2, 4, 5, 2, 3, 2, 1, 1, 5, 4],15,1))