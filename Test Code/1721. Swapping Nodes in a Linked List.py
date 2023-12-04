# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head:ListNode, k: int):
        arr = []
        aux = head
        while(aux):
            arr.append(aux.val)
            aux = aux.next
        val1, val2 = arr[k-1],arr[len(arr)-k]
        arr[k-1] = val2
        arr[len(arr)-k] = val1
        aux = head
        index = 0
        while(aux):
            aux.val = arr[index]
            index+=1
            aux = aux.next
        return head