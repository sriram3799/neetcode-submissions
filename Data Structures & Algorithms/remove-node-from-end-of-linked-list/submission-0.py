class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Reverse the list
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head = prev  # Reversed list
        
        # Step 2: Remove nth node from beginning of reversed list
        if n == 1:
            # Remove first node
            head = head.next
        else:
            # Find node BEFORE the one to remove
            curr = head
            for i in range(n - 2):  # Move n-2 steps
                if curr:
                    curr = curr.next
            
            # Remove the node
            if curr and curr.next:
                curr.next = curr.next.next
        
        # Step 3: Reverse back to original order
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev