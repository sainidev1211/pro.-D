class Solution(object):
    def reverseList(self, head):
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        new_head = None

        for x in arr:
            new_head = ListNode(x, new_head)

        return new_head