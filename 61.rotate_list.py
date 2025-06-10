# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #check if the list is empty and k is 0
        if not head or k == 0:
            return head
        
        length = 1
        #finding the length of linked list
        tail = head
        while tail.next:
            #traversing till the last node by checking if next is None
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head      
        
        tail.next = head 
        #converting it into a circular list
        new_head = length -k
        new_tail = tail
        while new_head:
            new_tail = new_tail.next
            new_head -= 1

        new_head = new_tail.next
        new_tail.next = None
        return new_head
        