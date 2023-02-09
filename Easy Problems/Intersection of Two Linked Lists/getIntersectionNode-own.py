# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if headA==None:
            return None
        if headB==None:
            return None
        
        hashSet = set()

        while(headA):
            hashSet.add(headA)
            headA=headA.next

        while(headB):
            if headB in hashSet:
                return headB
            headB=headB.next
        
        return None