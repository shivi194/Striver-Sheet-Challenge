class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getLeftView(root)->list:
    if not root:
        return []
    q = []
    q.append(root)
    ans = []
    while (len(q)):
        n = len(q)
        for i in range(1, n + 1):
            temp = q[0]
            q.pop(0)
            
            if (i == 1):
                ans.append(temp.data)
 
            # Add left node to queue
            if (temp.left != None):
                q.append(temp.left)
 
            # Add right node to queue
            if (temp.right != None):
                q.append(temp.right)
       
    return ans     
        
