from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEndL(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        len = 1
        while dummy.next:
            len += 1
            dummy = dummy.next
        if len == 1:
            return None

        dummy = head
        while len - n - 1 > 0:
            dummy = dummy.next
            len -= 1

        dummy.next = dummy.next.next

        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

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
l1 = sol.to_linked_list([1,2,3,4,5])
l1 = sol.removeNthFromEndL(l1, 2)
print(sol.to_native_list(l1))


"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?

Accepted
1,612,823
Submissions
4,120,630
Seen this question in a real interview before?

Yes

No
"""