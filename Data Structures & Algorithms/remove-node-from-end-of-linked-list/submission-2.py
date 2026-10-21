# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        nthNode = len(nodes) - n

        if nthNode != 0:
            nodes[nthNode - 1].next = nodes[nthNode].next
            return nodes[0]

        if nthNode == 0:
            if len(nodes) == 1:
                return None
            return nodes[1]
        