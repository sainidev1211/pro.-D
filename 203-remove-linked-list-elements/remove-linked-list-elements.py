class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # Remove matching nodes from the very start of the list
        while head is not None and head.val == val:
            head = head.next

        # Initialize curr and prev to traverse the rest
        prev = None
        curr = head

        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
       
            curr = curr.next

        return head