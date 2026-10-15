# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next # temp saves the next node
            curr.next = prev # curr.next points to previous
            prev = curr # update prev to curr
            curr = temp # curr is now the next one

        return prev