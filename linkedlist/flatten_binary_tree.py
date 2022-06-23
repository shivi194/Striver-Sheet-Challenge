# Following is the TreeNode class structure.
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def flattenBinaryTree(root):
    A = root
    st = []
    ans = A
    while (A != None or len(st) != 0):
        if (A.right != None):
            st.append(A.right)
        A.right = A.left
        A.left = None
        if (A.right == None and len(st) != 0):
            A.right = st[-1]
            st.pop()
        A = A.right
    return ans