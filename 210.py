from typing import List

class Course:
    def __init__(self, lable) -> None:
        self.lable = lable
        self.next = []
        self.num_pre = 0

    def append_next(self, c):
        self.next.append(c)
        c.num_pre += 1

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses: List[Course] = []
        for i in range(numCourses):
            courses.append(Course(i))

        for i_target, i_prerequisite in prerequisites:
            courses[i_prerequisite].append_next(courses[i_target])
        
        queue: list[Course] = []
        ans = []
        for c in courses:
            if c.num_pre == 0: 
                queue.append(c)
        while queue:
            present = queue[0]
            ans.append(present.lable)
            queue = queue[1:]
            for next_course in present.next:
                next_course.num_pre -= 1
                if next_course.num_pre ==0: queue.append(next_course)
        if len(ans) == numCourses:
            return ans
        else:
            return []
    
print(
    Solution().findOrder(
        numCourses = 7, prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
    )
)