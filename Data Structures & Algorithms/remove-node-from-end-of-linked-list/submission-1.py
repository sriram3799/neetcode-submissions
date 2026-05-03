class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        
        # Create gap of n
        for _ in range(n):
            fast = fast.next
        
        # Move both until fast reaches end
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Remove node
        slow.next = slow.next.next
        
        return dummy.next