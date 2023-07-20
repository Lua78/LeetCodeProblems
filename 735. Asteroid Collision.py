class Solution:
    def asteroidCollision(self, asteroids: list):
        if len(asteroids)<=0:
            return asteroids
        def checkAste():
            for i in range(len(asteroids)-1):
                if asteroids[i]>0 and asteroids[i+1]<0:
                    if asteroids[i]==abs(asteroids[i+1]):
                        asteroids.pop(i)
                        asteroids.pop(i)
                    elif asteroids[i]<abs(asteroids[i+1]):
                        asteroids.pop(i)
                    else:
                        asteroids.pop(i+1)
                    return True
            return False
        while(checkAste()):
            pass
        return asteroids


a = Solution()

print(a.asteroidCollision([5,10,-5]))