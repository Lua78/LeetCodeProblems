# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head:ListNode):
        aux = head
        index = 1
        last = None
        while(aux):
            if aux.next and index%2!=0:
                index+=1
                helper = aux.next.next
                sig = aux.next
                sig.next = aux
                aux.next = helper
                if last:
                    last.next = sig
                else:
                    head = sig
            last = aux
            index +=1
            aux = aux.next
        return head