class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isHeight(self, root):
        if not root:
            return -1
        return 1 + max(self.isHeight(root.left), self.isHeight(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return abs(self.isHeight(root.left) - self.isHeight(root.right)) <= 1 \
               and self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
################################################################################Official Solution ,height redudant calculation->
#    Time  complexity: O(n * log(n))
#    Space complexity: O(n)
    def height(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalancedO(self, root: TreeNode) -> bool:
        # An empty tree satisfies the definition of a balanced tree
        if not root:
            return True
        # Check if subtrees have height within 1. If they do, check if the
        # subtrees are balanced
        return abs(self.height(root.left) - self.height(root.right)) < 2 \
               and self.isBalanced(root.left) \
               and self.isBalanced(root.right)
#########################################################################################################Better official solution
#    Time complexity : O(n)
#    For every subtree, we compute its height in constant time as well as compare the height of its children.
#    Space complexity : O(n)
#    Return whether or not the tree at root is balanced while also returning
#    the tree's height
    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1
        # Check subtrees to see if they are balanced.
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0
        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]


"""
110. Balanced Binary Tree
Easy

7128

369

Add to List

Share
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
Accepted
905,993
Submissions
1,892,181
"""