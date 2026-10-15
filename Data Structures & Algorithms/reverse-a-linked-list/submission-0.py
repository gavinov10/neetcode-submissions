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
            temp = curr.next # stores next node -> (1)
            curr.next = prev # changes arrow to None
            prev = curr # saves curr as the prev
            curr = temp

        return prev