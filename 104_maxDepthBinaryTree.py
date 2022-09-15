# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return level

    def maxDepthbfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_q = deque([root])
        level = 0
        while node_q:
            for i in range(len(node_q)):
                node = node_q.popleft()
                if node.left:
                    node_q.append(node.left)
                if node.right:
                    node_q.append(node.right)
            level += 1
        return level

    def maxDepthdfs(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, level = stack.pop()
            if node:
                res = max(res, level)
                stack.append([node.left, level + 1])
                stack.append([node.right, level + 1])

        return res

s = Solution()
r = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(s.maxDepth(r))

r = TreeNode(3, TreeNode(9, None, None ), TreeNode(20, TreeNode(15), TreeNode(7)))
print(s.maxDepth(r))

r = TreeNode(1, None, TreeNode(2))
print(s.maxDepth(r))


"""
104. Maximum Depth of Binary Tree
Easy

8298

137

Add to List

Share
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
Accepted
1,905,015
Submissions
2,616,203"""