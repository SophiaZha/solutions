from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            second.next, second, prev  = prev, second.next, second

        first, second = head, prev
        while second:
            tmp_first, tmp_second = first.next, second.next
            first.next, second.next = second, first.next
            first, second = tmp_first, tmp_second

    def to_linked_list(self,iterable):
        head = None
        for val in reversed(iterable):
            head = ListNode(val, head)
        return head

    def to_native_list(self,head):
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst

sol = Solution()
l1 = sol.to_linked_list([1,2,3,4])
Solution().reorderList(l1)
print(sol.to_native_list(l1))


"""
143. Reorder List
Medium

7041

240

Add to List

Share
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
Accepted
557,081
Submissions
1,109,854
"""