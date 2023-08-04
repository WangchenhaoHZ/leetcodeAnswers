from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0 for _ in range(500)]
        for task in tasks:
            counts[ord(task)] +=1
        l = []
        for count in counts:
            if count >0: l.append(count)
        l.sort()
        counts = l
        if len(counts) < n + 1:
            ans = (counts[-1] - 1) * (n + 1)
            num_max_count = 0
            for count in counts:
                if count == counts[-1]:
                    num_max_count +=1
            ans += num_max_count
            return ans
        expidiency_sum = sum(counts[:len(counts)-n-1])
        counts = counts[len(counts)-n-1:]
        min_count = counts[0]
        min_count_first_index = 0
        next_larger_count_index = 1
        while (expidiency_sum>0) and (min_count < counts[-1]):
            for i in range(min_count_first_index+1, n+1):
                count = counts[i]
                if count > counts[0]: break
            next_larger_count_index = i
            next_larger_count = count
            if (next_larger_count_index) * (next_larger_count-min_count) < expidiency_sum:
                expidiency_sum -= (next_larger_count_index) * (next_larger_count-min_count)
                min_count = next_larger_count
                min_count_first_index = next_larger_count_index
            else:
                break
        dividence = expidiency_sum // next_larger_count_index
        modulo = expidiency_sum % next_larger_count_index
        ans = 0
        if min_count == counts[-1] : ans = expidiency_sum
        ans += (counts[-1] - 1) * (n + 1)
        if (min_count == counts[-1]) and (expidiency_sum >0):
            ans += n+1
        else:
            num_max_count = 0
            if dividence + min_count == counts[-1]:
                ans += n+1
                return ans
            for count in counts:
                if count == counts[-1]:
                    num_max_count +=1
            ans += num_max_count
            if dividence + min_count == counts[-1] - 1:
                ans += modulo
        return(ans)

print(
    Solution().leastInterval(
        ["A","B","C","D","A","B","V"], n = 3
    )
)