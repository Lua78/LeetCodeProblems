# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        targetGraph = None
        res = []
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
            if head == None:
                return
            if deep == k:
                res.append(head.val)
            search(head.left,deep+1)
            search(head.right,deep+1)
            search(head.last,deep+1)
        
        return res