# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        cur = head.next
        prev = head
        prev_uniq = None
        while cur!=None:
            if prev.val==cur.val:
                while cur!=None and cur.val==prev.val:
                    cur=cur.next
                if prev_uniq==None:
                    head=cur
                else:
                    prev_uniq.next=cur
                prev=prev_uniq
            prev_uniq = prev
            prev=cur
            if cur!=None:
                cur=cur.next
        return head
        
        
