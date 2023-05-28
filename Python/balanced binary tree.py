class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if abs(self.height(root.left)-self.height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right))+1