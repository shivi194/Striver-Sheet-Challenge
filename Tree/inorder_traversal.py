'''
    Following is the Binary Tree node structure:
    class TreeNode:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
'''


def getInOrderTraversal(root):
    if root==None:
        return []
    return getInOrderTraversal(root.left)+[root.data]+getInOrderTraversal(root.right)
    
