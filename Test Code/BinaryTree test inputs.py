class TreeNode(object):
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None
    
def newNode(numbers:list):
    r = TreeNode()
    r.val = numbers[0]
    numbers.pop(0)
    return r

def push(numbers:list):
    def insertNode(head):
        if len(numbers):
            head.right = newNode(numbers)
            if len(numbers):
                head.left= newNode(numbers)
                insertNode(head.right)
                insertNode(head.left)
    if numbers:
        head = newNode(numbers)
        insertNode(head)
        return head
    return None
      

#Build the test tree
tree  = push([1,2,4,5,6,8,7,9])

#
class GraphNode(object):
    def __init__(self):
        self.val = 0
        self.last = None
        self.left = None
        self.right = None

def TreeToGraph(tree,head):
    if tree==None:
        return
    head = GraphNode()
    head.val = tree.val
    TreeToGraph(tree.right,head.right)
    TreeToGraph(tree.left,head.left)



class Solution(object):
    def distanceK(self, root, target, k):
        targetGraph = None
        res = []
        visited = set()

        def TreeToGraph(tree,head):
            if tree==None:
                return
            head = GraphNode()
            head.val = tree.val
            if head.val ==  target.val:
                targetGraph = head
            TreeToGraph(tree.right,head.right)
            TreeToGraph(tree.left,head.left)
        
        def search(head,deep):
            if head == None or head.val in visited:
                return
            if deep == k:
                res.append(head.val)
                visited.add(head.val)
            search(head.left,deep+1)
            search(head.right,deep+1)
            search(head.last,deep+1)
            
        TreeToGraph(root,graphRoot)
        search(targetGraph)
        return res
