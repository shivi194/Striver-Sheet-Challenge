'''
    Following is the Binary Tree node structure:
    class TreeNode:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
'''


def getPostOrderTraversal(root):
    # Write your code here.
    if root==None:
        return []
    return getPostOrderTraversal(root.left)+getPostOrderTraversal(root.right)+[root.data]
