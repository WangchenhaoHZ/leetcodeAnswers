from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0 for _ in range(500)]
        for task in tasks:
            counts[ord(task)] +=1
        l = []
        for count in counts:
            if count >0: l.append(count)
        l.sort(reverse= True)
        
        if n == 0: return sum(l)

        max_count = 1
        while max_count<len(l) and (l[max_count]) == l[0]:
            max_count +=1
        ans = 0
        other_task_sum = sum(l[max_count:])
    #    ans += max_count // (n+1) * (n+1) * l[0]
    #    max_count = max_count % (n+1)
        ans += (l[0]-1) * (n-max_count+1) + max_count * l[0]
        idel_count = (l[0]-1) * (n-max_count+1)
        ans += max(0, other_task_sum-idel_count)
        return ans


print(
    Solution().leastInterval(
        tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
    )
)