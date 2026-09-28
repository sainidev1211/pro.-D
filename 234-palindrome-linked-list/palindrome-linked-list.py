class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        vals = []
        current = head
        
        # Store all list node values in a Python list
        while current:
            vals.append(current.val)
            current = current.next
            
        # Check if the list of values is equal to its reverse
        return vals == vals[::-1]