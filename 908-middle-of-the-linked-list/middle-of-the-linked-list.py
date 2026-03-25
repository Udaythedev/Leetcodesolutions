# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = head
        nodesize=1
        LLV=[]
        while(newhead != None):
            LLV.append(newhead.val)
            newhead = newhead.next
            nodesize+=1
        if nodesize%2 ==0:
            mid = nodesize//2-1
        else:
            mid = nodesize//2
        while(mid!=0):
            head = head.next
            mid-=1
        return head

