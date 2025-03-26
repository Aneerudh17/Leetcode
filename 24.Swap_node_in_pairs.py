class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: 
            return head
        
        head.next = self.swapPairs(temp.next)  
        temp.next = head  
        
        return temp 