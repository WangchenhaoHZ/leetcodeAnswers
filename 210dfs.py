# full dfs for toplogical order of DAG of a forest
from typing import List

class Course():
    def __init__(self, course_num) -> None:
        self.fanouts = []
        self.num =course_num
        self.has_prerequisite = False
        
    def add_fanout(self, fanout):
        self.fanouts.append(fanout)

NOT_VISITED =  100
VISITING = 200
VISITED = 300

class Solution:
    
    def dfs(self,course: Course):
        self.has_visited[course.num] = VISITING
        for fanout in course.fanouts:
            if self.has_visited[fanout.num] == NOT_VISITED:
               self.dfs(fanout)
            elif self.has_visited[fanout.num] == VISITING: 
                self.top_order = [-1]
                return
            else: continue
            if self.top_order == [-1]: return
        self.top_order.append(course.num)
        self.has_visited[course.num] = VISITED
        
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_table: list[Course] = [None] * numCourses
        for num in range(numCourses):
            course_table[num] = Course(num)
        for p, c in prerequisites:
            course_table[p].add_fanout(course_table[c])
            course_table[c].has_prerequisite = True
        self.top_order = []
        self.has_visited = [NOT_VISITED] * numCourses
        for course in course_table:
            if not course.has_prerequisite:
                self.dfs(course)
            if self.top_order == [-1]: return []
        if len(self.top_order) == numCourses:
            return self.top_order
        else:
            return []
    
print(
    Solution().findOrder(
        numCourses = 8, prerequisites = [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]]
    )
)