class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Pointer:
    def __init__(self, value):
        self.value = value
    def setValue(self, value):
        self.value = value

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parentX = Pointer(0)
        parentY = Pointer(0)
        depthX = getDepthOfValue(root, x, parentX)
        depthY = getDepthOfValue(root, y, parentY)
        return True if depthX == depthY and parentX.value != parentY.value else False

def getDepthOfValue(root: TreeNode, value: int, parent: Pointer, depth=0):
    if root is None:
        return 0
    elif root.val == value:
        return depth

    parent.setValue(root.val)
    left = getDepthOfValue(root.left, value, parent, depth+1)
    if left and left != 0:
        return left

    parent.setValue(root.val)
    right = getDepthOfValue(root.right, value, parent, depth+1)
    if right != 0:
        return right
