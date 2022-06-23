'''
	 
	 Following is the Binary Tree node structure:
	 
	 class TreeNode:
	     def __init__(self, data=0, left=None, right=None):
	         self.data = data
	         self.left = left
	         self.right = right
'''

def getPreOrderTraversal(root):
    # Write your code here.
    if root==None:
        return []
    return [root.data]+getPreOrderTraversal(root.left)+getPreOrderTraversal(root.right)
