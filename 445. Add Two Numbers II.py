# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pila1 = []
        pila2 = []
        res = []
        while(l1):
            pila1.append(l1.val)
            l1 = l1.next
        while(l2):
            pila2.append(l2.val)
            l2 = l2.next
        pila1.reverse()
        pila2.reverse()
        residuo = 0
        while(pila1 and pila2):
            num = pila1[0]+pila2[0]
            pila1.pop(0)
            pila2.pop(0)
            num+=residuo
            residuo = 0
            if num > 9:
                residuo = 1*(num//10)
                num = num%10
            res.append(num)

        if pila1:
            while(pila1):
                num = pila1[0]+residuo
                pila1.pop(0)
                residuo = 0
                if num>9:
                    residuo=num//10
                    num = num%10
                res.append(num)  
        elif pila2:
            while(pila2):
                num = pila2[0]+residuo
                pila2.pop(0)
                residuo = 0
                if num>9:
                    residuo=num//10
                    num = num%10
                res.append(num)
        if residuo:
            res.append(residuo)  
        res.reverse()
        head = ListNode(res[0],None)
        res.pop(0)
        aux = head
        while(res):
            aux.next = ListNode(res[0],None)
            res.pop(0)
            aux = aux.next
        return head