class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hash = { i:[] for i in range(numCourses)}
        for i,r in prerequisites:
            hash[i].append(r)
        visited = set()

        def dfs(curr):
            if curr in visited:
                return False
            if curr == []:
                return  True
            visited.add(curr)
            for i in hash[curr]:
                if not dfs(i):
                    return False
            visited.remove(curr)
            hash[curr] = []
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True