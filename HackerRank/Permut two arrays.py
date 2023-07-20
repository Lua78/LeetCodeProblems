def twoArrays(k, A, B):
    # Write your code here
    a = set()
    B.sort()
    for i in range(len(A)):
        num = k-A[i]
        for j in range (0,len(B)):
            if B[j]>=num:
                B.pop(j)
                break
        if len(B)==0:
            return True
    return False

