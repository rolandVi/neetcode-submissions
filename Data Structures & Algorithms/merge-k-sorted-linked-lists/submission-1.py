# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = ListNode()
        result = node

        pq = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(pq, (l.val, i, l))

        if not lists or not pq:
            return None

        while pq:
            value, i, l = heapq.heappop(pq)

            node.val = value
            if not pq and not l.next:
                break
            next_node = ListNode()
            node.next = next_node
            node = next_node
            
            if l.next:
                l = l.next
                heapq.heappush(pq, (l.val, i, l))

        return result
