class Solution:
    def getIntersectionNode(self, headA, headB):
        d = {}
        curr = headA

        while curr:
            d[curr] = True
            curr = curr.next

        curr = headB

        while curr:
            if curr in d:
                return curr
            curr = curr.next

        return None