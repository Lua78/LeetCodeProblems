class Solution:
    def isPalindrome(self, x: int):
        st = str(x)
        le = len(st)
        for i in range(le//2):
            if st[i]!=st[le-i-1]:
                return False
        return True

a =  Solution()

print(a.isPalindrome(8988))