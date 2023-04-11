# Definition for a binary tree node.
from collections import deque

def build_tree(leet_code_input: str, should_print_tree_code_to_console=False):
    """
    Credit to LeetCode user 'bqrkhn' for this function

    Given the typical leet code input string for
    a tree, where the tree is defined level by
    level such that input[i] has nodes defined
    for a level as input[i+1:nodes_in_level],
    this builds that tree!

    Explicitly, it prints out the code for the tree structure if
    should_print_tree_code_to_console=True,
    and returns the root of the constructed tree regardless
    """
    leet_code_input = leet_code_input[1:-1].split(',')
    if len(leet_code_input) == 0:
        return
    nodes = [('root', leet_code_input[0])]
    for index, current_node in enumerate(leet_code_input[1:]):
        if current_node != 'null':
            if index & 1:
                nodes.append((nodes[index // 2][0] + '.right', current_node))
            else:
                nodes.append((nodes[index // 2][0] + '.left', current_node))
    root = TreeNode(int(nodes[0][1]))
    for node in nodes:
        execution_statement: str = node[0] + ' = TreeNode(' + node[1] + ')'
        if should_print_tree_code_to_console:
            print(execution_statement)
        exec(execution_statement)
    return root

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

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        node_q = deque([root])
        level = 0

        while node_q:
            for i in range(len(node_q)):
                this_node = node_q.popleft();
                if this_node.left:
                    node_q.append(this_node.left)
                if this_node.right:
                    node_q.append(this_node.right)
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

root = build_tree('[3,9,20,null,null,15,7]', True)
print(s.maxDepth(root))

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