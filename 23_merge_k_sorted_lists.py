from typing import List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
    # def mergeKLists(self, lists:List[ListNode]):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lenth = len(lists)
        if lenth == 0: return None
        if lenth == 1: return lists[0]
        if lenth == 2:
            list_a = lists[0]
            list_b = lists[1]
        if lenth> 2:
            mid = lenth // 2
            list_a = self.mergeKLists(lists[:mid])
            list_b = self.mergeKLists(lists[mid:])
        answer = None
        before = None
        while (list_a != None) or (list_b != None):
            if (list_a != None) and ((list_b == None) or (list_a.val <= list_b.val)):
                present = ListNode(val = list_a.val, next = None)
                list_a = list_a.next
            else:
                present = ListNode(val = list_b.val, next = None)
                list_b = list_b.next
            if answer == None: answer = present
            if before != None: before.next = present
            before = present
        return answer
    
    def input(self, lists:List[List[int]]):
        linked_lists = []
        for list in lists:
            linked_head = None
            before = None
            for num in list:
                present = ListNode(val = num, next=None)
                if linked_head == None: linked_head = present
                if before != None: before.next = present
                before = present
            linked_lists.append(linked_head)
        return linked_lists

lists = Solution().input(lists = [[]])
print(Solution().mergeKLists(lists))