

from typing import List
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        route_not_in_queue = [True for _ in range(500)]
        stop_not_in_queue = [True for _ in range(1000000)]
        stop_has_route = [[] for _ in range(1000000)]
        for i_route, route in enumerate(routes):
            for stop in route:
                stop_has_route[stop].append(i_route)
        queue = []
        queue.append(source)
        stop_not_in_queue[source] = False
        ans = 1
        i_start = 0
        i_end = len(queue) -1
        while i_start<=i_end:
            for i_queue in range(i_start,i_end+1):
                stop = queue[i_queue]
                if stop == target: return ans -1
                for i_route in stop_has_route[stop]:
                    if route_not_in_queue[i_route]:
                        for new_stop in routes[i_route]:
                            if stop_not_in_queue[new_stop]:
                                queue.append(new_stop)
                                stop_not_in_queue[new_stop] = False
                        route_not_in_queue[i_route] = False
            i_start = i_end+1
            i_end = len(queue) -1
            ans += 1
        return -1

print(
    Solution().numBusesToDestination(
        [[1,7,5],[3,5],[4,5]],
        1,
        6
    )
)