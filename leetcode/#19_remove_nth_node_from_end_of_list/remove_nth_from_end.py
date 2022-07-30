# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        
        # build up stack
        while head != None:
            stack.insert(0, head)
            head = head.next
        
        
        i = 1
        
        # work backwards and remove the nth node
        while len(stack) > 0:
            if i == n:
                next_node = stack[0].next
                if(len(stack) > 1):
                    stack[1].next = next_node
                stack.pop(0)
            else:
                head = stack.pop(0)
            
            i += 1
        
        return head