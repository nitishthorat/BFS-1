'''
    Time Complexity: O(n^2)
    Space Complexity: O(2n)
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not len(prerequisites):
            return True

        preMap = {}
        dependents = [0 for i in range(numCourses)]
        completed = 0

        for prereq in prerequisites:
            dep = prereq[0]
            pre = prereq[1]

            if pre in preMap:
                preMap[pre].append(dep)
            else:
                preMap[pre] = [dep]

            dependents[dep] += 1

        queue = deque()

        for i in range(numCourses):
            if dependents[i] == 0:
                queue.append(i)

        while len(queue):
            course = queue.popleft()
            completed += 1
            courses = preMap[course] if course in preMap else []

            for j in range(len(courses)):
                dependents[courses[j]] -= 1
                
                if dependents[courses[j]] == 0:
                    queue.append(courses[j])

        if completed == numCourses:
            return True
        
        return False