class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val 
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        ans = []

        if root is None:
            return []
        
        def traverse(root: TreeNode) -> None:
            if root.left is None and root.right is None:
                ans.append(root.val)
                return

            if root.left:
                traverse(root.left)
            
            ans.append(root.val)

            if root.right:
                traverse(root.right)

            return
        
        traverse(root)
        
        return ans
