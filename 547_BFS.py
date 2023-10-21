from typing import List

# using full BFS to find out the clique number of undirected map

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        city_num = len(isConnected)
        if_counted_list = [False] * city_num
        province_num = 0
        for city_index, if_counted in enumerate(if_counted_list):
            if if_counted: continue
            cities_in_province = [city_index]
            if_counted_list[city_index] = True
            head = 0
            tail = 0
            while tail >= head:
                for linked_city in range(city_num):
                    if linked_city == cities_in_province[head]: continue
                    if (not if_counted_list[linked_city]) and isConnected[cities_in_province[head]][linked_city]:
                        tail += 1
                        cities_in_province.append(linked_city)
                        if_counted_list[linked_city] = True
                head += 1
            province_num += 1
        return province_num

print(
    Solution().findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]])
)