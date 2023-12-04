class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

def makeList(elements:list):
     head = ListNode(elements[0],None)
     aux = head
     for i in range(1,len(elements)):
        aux.next = ListNode(elements[i],None)
        aux = aux.next
     return head





a = Solution()
li = makeList([1,2,3,5,6,4])
#res =  a.SolutionFunction(li...)
