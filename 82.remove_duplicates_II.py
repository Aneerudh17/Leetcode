# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        #using a dummmy pointer
        dummy = ListNode(0,head)
        prev = dummy
        current = head

        while current:
            is_duplicate = False

            while current.next and current.val == current.next.val:
                is_duplicate = True
                current= current.next

            if is_duplicate:
                prev.next = current.next
            else:
                prev = prev.next
            
            current = current.next

        return dummy.next
        

'''
js solution
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    if (!head || !head.next) return head;
    
    const dummy = new ListNode(0,head);
    let prev = dummy;
    let current = head;

    while (current){
        let isduplicate = false;
        while (current.next && current.val == current.next.val){
            isduplicate = true;
            current = current.next;
        }
        if (isduplicate){
            prev.next = current.next;

        }
        else{
            prev = prev.next
        }
        current = current.next
    }
    return dummy.next;
};
'''